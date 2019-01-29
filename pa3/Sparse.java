// Chang Kim
// cnkim
// pa3

import java.util.Scanner;
import java.io.*;

public class Sparse{
   public static void main(String[] args) throws IOException{
      if(args.length != 2){
         System.err.println("Usage: FileIO infile outfile");
         System.exit(1);
      }
      Scanner in = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new File(args[1]));
      String line = null;
      String[] token = null;
      int a,b,n,lineNumber = 0;
      
      line = in.nextLine()+ " ";
      token = line.split("\\s+");
      n = Integer.parseInt(token[0]);
      a = Integer.parseInt(token[1]);
      b = Integer.parseInt(token[2]);
      Matrix A = new Matrix(n);
      Matrix B = new Matrix(n);
      in.nextLine();
      while(in.hasNextLine()){
         lineNumber++;
         line = in.nextLine()+" ";
         token = line.split("\\s+");
         if(lineNumber == a+1){}
         else if(lineNumber < a+1){
            A.changeEntry(Integer.parseInt(token[0]),Integer.parseInt(token[1]),Double.parseDouble(token[2]));
         }
         else if(lineNumber > a+1 && lineNumber < a+b+2){
            B.changeEntry(Integer.parseInt(token[0]),Integer.parseInt(token[1]),Double.parseDouble(token[2]));
         }
      }
      out.println("A has "+A.getNNZ()+" non-zero entries:");
      out.println(A.toString());
      out.println("B has "+B.getNNZ() +" non-zero entries:");
      out.println(B.toString());
      out.println("(1.5)*A =");
      out.println(A.scalarMult(1.5).toString());
      out.println("A+B =");
      out.println(A.add(B).toString());
      out.println("A+A =");
      out.println(A.add(A).toString());
      out.println("B-A =");
      out.println(B.sub(A).toString());
      out.println("A-A =");
      out.println(A.sub(A).toString());
      out.println("Transpose(A) =");
      out.println(A.transpose());
      out.println("A*B =");
      out.println(A.mult(B).toString());
      out.println("B*B =");
      out.println(B.mult(B).toString());

      in.close();
      out.close();   
   }
}
