// Chang Kim
// cnkim
// List.java
// pa1

public class List{
   private int index, length;
   private Node front, back, cursor;
   private class Node{
      private int data;
      private Node next, previous;
      private Node(int value){
         data = value;
         next = null;
         previous = null;
      }
      public String toString(){
         return String.valueOf(data);
      }
   }
   public List(){
      clear();
   }
   public int length(){
      return length;
   }
   public int index(){
      if(cursor != null)
         return index;
      return -1;
   }
   public int front(){
      if(length > 0)
         return front.data;
      return -1;
   }
   public int back(){
      if(length > 0)
         return back.data;
      return -1;
   }
   public int get(){
      if(length > 0 && index >= 0)
         return cursor.data;
      return -1;
   }
   public boolean equals(List L){
      String str1 = toString();
      String str2 = L.toString();
      if(str1.equals(str2))
         return true;
      return false;
   }
   public void clear(){
      index = -1;
      length = 0;
      cursor = null;
      back = null;
      front = null;  
   }
   public void moveFront(){
      if(length > 0){
         cursor = front;
         index = 0;
      }
   }
   public void moveBack(){
      if(length > 0){
         cursor = back;
         index = length-1;
      }
   }
   public void movePrev(){
      if(cursor != null){
         if(cursor ==  front){
            cursor = null;
            index = -1;
         }
         else{
            cursor = cursor.previous;
            index--;   
         }
      }
   }
   public void moveNext(){
      if(cursor != null){
         if(cursor == back){
            cursor = null;
            index = -1;
         }
         else{
            cursor = cursor.next;
            index++;
         }
      }
   }
   public void prepend(int data){
      Node newNode = new Node(data);
      if(length == 0){
         front = newNode;
         back = newNode;
      }
      else{
         newNode.next = front;
         front.previous = newNode;
         front = newNode;
      }
      length++;
      if(index != -1)
         index++;
   }
   public void append(int data){
      Node newNode = new Node(data);
      if(length == 0){
         front = newNode;
         back = newNode;
      }
      else{
         newNode.previous = back;
         back.next = newNode;
         back = newNode;
      }
      length++;
   }
   public void insertBefore(int data){
      if(length > 0){
         if(index == 0)
            prepend(data);
         else{
            Node newNode = new Node(data);
            newNode.next = cursor;
            newNode.previous = cursor.previous;
            cursor.previous.next = newNode;
            cursor.previous = newNode;
            length++;
            index++;
         }
      }
      else{
         append(data);
      }
   }
   public void insertAfter(int data){
      if(length > 0){
         if(index == length-1)
            append(data);
         else{
            Node newNode = new Node(data);
            newNode.previous = cursor;
            newNode.next = cursor.next;
            cursor.next.previous = newNode;
            cursor.next = newNode;
            length++;
         }
      }
      else{
         append(data);
      }
   }
   public void deleteFront(){
      if(length > 0){
         if(cursor == front){
            cursor = null;
            index = -1;
         }
         else if (cursor != null){
            index--;
         }
         front.next.previous = null;
         front = front.next;
         length--;
      }
   }
   public void deleteBack(){
      if(length > 0){
         if(length == 1){
            back = null;
            front = null;
         }
         else{
            back.previous.next = null;
            back = back.previous;
         }
         if(index == length-1){
            cursor = null;
            index = -1;
         }
         length--;
      }
   }
   public void delete(){
      if(length > 0){
         if(cursor == back)
            deleteBack();
         else if(cursor == front)
            deleteFront();
         else{
            cursor.previous.next = cursor.next;
            cursor.next.previous = cursor.previous;
            cursor = null;
            length--;
            index = -1;
         }
      }
   }
   public String toString(){
      Node current = front;
      String str = "";
      while(current != null){
         str += current.data + " ";
         if(current.next == null)
            break;
         current = current.next;
      }
      return str;
   }
   public List copy(){
      List newList = new List();
      if(length == 0)
         return newList;
      Node current = front;
      int value = current.data;
      while(current != null){
         newList.append(value);
         if(current.next != null){
            current = current.next;
            value = current.data;
         }
         else
            break;
      }
      return newList;
   }
//   public List concat(List L){
      
//   }   
}



