// Chang Kim
// cnkim
// Lex.java
// pa1 

import java.io.*;
import java.util.Scanner;

public class Lex{
   public static void main(String[] args) throws IOException {
      if(args.length != 2){
         System.err.println("Usage: FileIO infile outfile");
         System.exit(1);
      }
      
      Scanner in = new Scanner(new File(args[0]));     
      PrintWriter out = new PrintWriter(new File(args[1]));

      // Counts the size of entries
      int count = 0;
      while(in.hasNextLine()){
         count++;
         in.nextLine();
      }
      String[] arr = new String[count]; 
      in = new Scanner(new File(args[0]));

      // Adds entries to array
      for(int i=0; i<count; i++){
         arr[i] = in.nextLine();
      }
      List newList = new List();
      // Adds first (sorted) index
      newList.append(0);
      // Insertion sort
      for(int i=1; i<count; i++){
         // Compares if inserting element is less that the node in list and if so inserts it before it
         for(newList.moveFront(); newList.index()>=0; newList.moveNext()){
            if(arr[i].compareTo(arr[newList.get()]) <= 0){
               newList.insertBefore(i);
               break;
            }
         }
         // Inserts at the end as it is the greatest value in the list
         if(newList.index() == -1)
            newList.append(i);
      }
      // Prints out the to the output file
      for(newList.moveFront(); newList.index()>=0; newList.moveNext()){
         out.println(arr[newList.get()]);
      }
      in.close();
      out.close();
   }
}
