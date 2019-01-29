// Chang Kim
// cnkim
// pa3

public class Matrix{
   private class Entry{
      int index;
      double value;
      private Entry(int index, double value){
         this.index = index;
         this.value = value;
      }

      public boolean equals(Object o){
         if(!(o instanceof Entry))
            return false;
         Entry e = (Entry) o;
         if(this.value == e.value && this.index == e.index)
            return true;
         return false;
      }

      public String toString(){
         return "(" + this.index + ", " + this.value + ")";
      }
   }

   List[] matrix;
   int size;
   int NNZ;
   public Matrix(int n){
      this.size = n;
      this.NNZ = 0;
      this.matrix = new List[n+1];
      for(int i=1; i<n+1; i++){
         this.matrix[i] = new List();
      }
   }

   public int getSize(){
      return this.size;
   }

   public int getNNZ(){
      return this.NNZ;
   }

   public boolean equals(Object x){
      Matrix mx = (Matrix) x;
      if(this.toString().equals(mx.toString()) && this.size == mx.size)
         return true;
      return false;
   }

   public void makeZero(){
      for(int i=1; i<this.size+1; i++){
         this.matrix[i] = new List();
      }
      this.NNZ = 0;
   }

   public Matrix copy(){
      Matrix newMatrix = new Matrix(this.size);
      for(int i=1; i<this.size+1; i++){
         for(this.matrix[i].moveFront(); this.matrix[i].index()>=0; this.matrix[i].moveNext()){
            newMatrix.matrix[i].append(this.matrix[i].get());
            newMatrix.NNZ++;
         }
      } 
      return newMatrix;
   }

   public void changeEntry(int i, int j, double x){
      Entry newEntry = new Entry(j,x);
      if(this.matrix[i].length() == 0 && x != 0){
         this.matrix[i].append(newEntry);
         this.NNZ++;
         return;
      }
      this.matrix[i].moveFront();
      Entry y = null;
      while(this.matrix[i].index()>=0){
         Entry e = (Entry) this.matrix[i].get();
         if(e.index >= j){
            y = e;
            break;
         }
         this.matrix[i].moveNext(); 
      }
      if(y == null && x == 0)
         return;
      else if(y == null && x != 0){
         this.matrix[i].append(newEntry);
         this.NNZ++;
         return;
      }
      else if(y.index == j && x == 0){
         this.matrix[i].delete();
         this.NNZ--;
      }
      else if(y.index > j && x != 0){
         this.matrix[i].insertBefore(newEntry);
         this.NNZ++;
      }
      else if(y.index < j && x != 0){
         this.matrix[i].insertAfter(newEntry);
         this.NNZ++;
      }
      else{
         this.matrix[i].insertAfter(newEntry);
         this.matrix[i].delete();
      }
   }
   public Matrix scalarMult(double x){
      Matrix newMatrix = this.copy();
      for(int i=1; i<this.size+1; i++){
         for(this.matrix[i].moveFront(); this.matrix[i].index()>=0; this.matrix[i].moveNext()){
            newMatrix.changeEntry(i,((Entry)this.matrix[i].get()).index,x*((Entry)this.matrix[i].get()).value);
         }
      }
      return newMatrix;
   }

   public Matrix add(Matrix M){
      if(M.getSize() != this.size)
         return null;
      if(M == this){
         return this.scalarMult(2);
      }
      Matrix newMatrix = new Matrix(size);
      for(int i=1; i<this.size+1; i++){
         for(this.matrix[i].moveFront(), M.matrix[i].moveFront(); this.matrix[i].index() >= 0 || M.matrix[i].index() >= 0;){
            Entry e = (Entry) this.matrix[i].get();
            Entry e2 = (Entry) M.matrix[i].get();
            if(e == null && e2 != null){
               newMatrix.matrix[i].append(new Entry(e2.index, e2.value));
               newMatrix.NNZ++;
               M.matrix[i].moveNext();
            }
            else if (e != null && e2 == null){
               newMatrix.matrix[i].append(new Entry(e.index, e.value));
               newMatrix.NNZ++;       
               this.matrix[i].moveNext();     
            }
            else if(e.index == e2.index){
               if(e.value + e2.value != 0){
                  newMatrix.matrix[i].append(new Entry(e.index, (e.value + e2.value)));
                  newMatrix.NNZ++;
               }
               M.matrix[i].moveNext();
               this.matrix[i].moveNext();
            }
            else if(e.index > e2.index){
               newMatrix.matrix[i].append(new Entry(e2.index, e2.value));
               M.matrix[i].moveNext();
               newMatrix.NNZ++;
            }
            else if(e.index < e2.index){
               newMatrix.matrix[i].append(new Entry(e.index, e.value));
               this.matrix[i].moveNext();
               newMatrix.NNZ++;
            } 	
         }
      }
      return newMatrix;
   }

   public Matrix sub(Matrix M){
      if(M.getSize() != this.size)
         return null;
      Matrix newMatrix = new Matrix(this.size);
      for(int i=1; i<this.size+1; i++){
         for(this.matrix[i].moveFront(), M.matrix[i].moveFront(); this.matrix[i].index() >= 0 || M.matrix[i].index() >= 0;){
            Entry e = (Entry) this.matrix[i].get();
            Entry e2 = (Entry) M.matrix[i].get();
            if(e == null && e2 != null){
               newMatrix.matrix[i].append(new Entry(e2.index, -e2.value));
               newMatrix.NNZ++;
               M.matrix[i].moveNext();
            }
            else if(e2 == null && e != null){
               newMatrix.matrix[i].append(new Entry(e.index, e.value));
               newMatrix.NNZ++;
               this.matrix[i].moveNext();
            }
            else if(e.index == e2.index){
               if((e.value - e2.value) != 0){
                  newMatrix.matrix[i].append(new Entry(e.index, (e.value - e2.value)));
                  newMatrix.NNZ++;
               }
               M.matrix[i].moveNext();
               this.matrix[i].moveNext();
            }
            else if(e.index > e2.index){
               newMatrix.matrix[i].append(new Entry(e2.index, -e2.value));
               M.matrix[i].moveNext();
               newMatrix.NNZ++;
            }
            else if(e.index < e2.index){
               newMatrix.matrix[i].append(new Entry(e.index, e.value));
               this.matrix[i].moveNext();
               newMatrix.NNZ++;
            }
         }
      }
      return newMatrix;
   }

   public Matrix transpose(){
      Matrix newMatrix = new Matrix(this.size);
      for(int i=1; i<this.size+1; i++){
         for(this.matrix[i].moveFront(); this.matrix[i].index()>=0; this.matrix[i].moveNext()){
            Entry e = (Entry)this.matrix[i].get();
            newMatrix.changeEntry(e.index,i,e.value);
         }
      } 
      return newMatrix;
   }

   public Matrix mult(Matrix M){
      if(M.getSize() != this.size){
         return null;
      }
      Matrix newMatrix = new Matrix(this.size);
      Matrix mT = M.transpose();
      double value;
      for(int i=1; i<this.size+1; i++){
         for(int j=1; j<this.size+1; j++){
            if(this.matrix[i].length()>0 && mT.matrix[j].length()>0){
               value = dotProduct(this.matrix[i],mT.matrix[j]);
               newMatrix.changeEntry(i,j,value);
            }
         } 
      }
      return newMatrix;
   }

   public String toString(){
      String str = "";
      for(int i=1; i<this.size+1; i++){
         if(this.matrix[i].length() != 0){
            str += i+": ";
            str += this.matrix[i].toString() + "\n";
         }
      }
      return str;
   }
   private static double dotProduct(List P, List Q){
      double total = 0;
      for(P.moveFront(), Q.moveFront(); P.index()>=0 && Q.index()>=0;){
         Entry e = (Entry) P.get();
         Entry e2 = (Entry) Q.get();
         if(e.index == e2.index){
            total += e.value * e2.value;
            P.moveNext();
            Q.moveNext();
         }
         else if(e.index > e2.index){
            Q.moveNext();
         } 
         else if(e.index < e2.index){
            P.moveNext();
         }
      }
      return total;
   }
}
