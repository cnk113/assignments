// Chang Kim
// cnkim
// List.java
// pa1

public class List{
   private int index, length;
   private Node front, back, cursor;
   private class Node{
      private Object data;
      private Node next, previous;
      private Node(Object value){
         this.data = value;
         this.next = null;
         this.previous = null;
      }
      public String toString(){
         return this.data.toString();
      }
   }
   public List(){
      this.clear();
   }
   public int length(){
      return this.length;
   }
   public int index(){
      if(this.cursor != null)
         return this.index;
      return -1;
   }
   public Object front(){
      if(this.length > 0)
         return this.front.data;
      return -1;
   }
   public Object back(){
      if(this.length > 0)
         return this.back.data;
      return -1;
   }
   public Object get(){
      if(this.length > 0 && this.index >= 0)
         return this.cursor.data;
      return null;
   }
   public boolean equals(Object L){
      String str1 = this.toString();
      String str2 = L.toString();
      if(str1.equals(str2))
         return true;
      return false;
   }
   public void clear(){
      this.index = -1;
      this.length = 0;
      this.cursor = null;
      this.back = null;
      this.front = null;  
   }
   public void moveFront(){
      if(this.length > 0){
         this.cursor = this.front;
         this.index = 0;
      }
   }
   public void moveBack(){
      if(this.length > 0){
         this.cursor = this.back;
         this.index = this.length-1;
      }
   }
   public void movePrev(){
      if(this.cursor != null){
         if(this.cursor ==  this.front){
            this.cursor = null;
            this.index = -1;
         }
         else{
            this.cursor = this.cursor.previous;
            this.index--;   
         }
      }
   }
   public void moveNext(){
      if(this.cursor != null){
         if(this.cursor == this.back){
            this.cursor = null;
            this.index = -1;
         }
         else{
            this.cursor = this.cursor.next;
            this.index++;
         }
      }
   }
   public void prepend(Object data){
      Node newNode = new Node(data);
      if(this.length == 0){
         this.front = newNode;
         this.back = newNode;
      }
      else{
         newNode.next = this.front;
         this.front.previous = newNode;
         this.front = newNode;
      }
      this.length++;
      if(this.index != -1)
         this.index++;
   }
   public void append(Object data){
      Node newNode = new Node(data);
      if(this.length == 0){
         this.front = newNode;
         this.back = newNode;
      }
      else{
         newNode.previous = this.back;
         this.back.next = newNode;
         this.back = newNode;
      }
      this.length++;
   }
   public void insertBefore(Object data){
      if(this.length > 0){
         if(this.index == 0)
            this.prepend(data);
         else{
            Node newNode = new Node(data);
            newNode.next = this.cursor;
            newNode.previous = this.cursor.previous;
            this.cursor.previous.next = newNode;
            this.cursor.previous = newNode;
            this.length++;
            this.index++;
         }
      }
      else{
         this.append(data);
      }
   }
   public void insertAfter(Object data){
      if(this.length > 0){
         if(this.index == this.length-1)
            this.append(data);
         else{
            Node newNode = new Node(data);
            newNode.previous = this.cursor;
            newNode.next = this.cursor.next;
            this.cursor.next.previous = newNode;
            this.cursor.next = newNode;
            this.length++;
         }
      }
      else{
         this.append(data);
      }
   }
   public void deleteFront(){
      if(this.length > 0){
         if(this.cursor == this.front){
            this.cursor = null;
            this.index = -1;
         }
         else if (this.cursor != null){
            this.index--;
         }
         this.front.next.previous = null;
         this.front = this.front.next;
         this.length--;
      }
   }
   public void deleteBack(){
      if(this.length > 0){
         if(this.length == 1){
            this.back = null;
            this.front = null;
         }
         else{
            this.back.previous.next = null;
            this.back = this.back.previous;
         }
         if(this.index == this.length-1){
            this.cursor = null;
            this.index = -1;
         }
         this.length--;
      }
   }
   public void delete(){
      if(this.length > 0){
         if(this.cursor == this.back)
            this.deleteBack();
         else if(this.cursor == this.front)
            this.deleteFront();
         else{
            this.cursor.previous.next = this.cursor.next;
            this.cursor.next.previous = this.cursor.previous;
            this.cursor = null;
            this.length--;
            this.index = -1;
         }
      }
   }
   public String toString(){
      Node current = this.front;
      String str = "";
      while(current != null){
         str += current.toString() + " ";
         current = current.next;
      }
      return str;
   }
}



