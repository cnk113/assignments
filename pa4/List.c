/*
 * List.c
 * Chang Kim
 * cnkim
 * pa2
 */
// Doubly linked list ADT 


#include<stdio.h>
#include<stdlib.h>
#include "List.h"

typedef struct NodeObj{
   int data;
   struct NodeObj* next;
   struct NodeObj* previous;
} NodeObj;

typedef NodeObj* Node;

typedef struct ListObj{
   Node cursor;
   Node front;
   Node back;
   int length;
   int index;
} ListObj;

Node newNode(int data){
   Node N = malloc(sizeof(NodeObj));
   N->data = data;
   N->next = NULL;
   N->previous = NULL;
   return (N);
}

void freeNode(Node* pN){
   if(pN!=NULL && *pN!=NULL){
      free(*pN);
      *pN = NULL;
   }
}

List newList(void){
   List L;
   L = malloc(sizeof(ListObj));
   L->cursor = NULL;
   L->front = NULL;
   L->back = NULL;
   L->length = 0;
   L->index = -1;
   return L;
}
void freeList(List* pL){
   if(pL!=NULL && *pL!=NULL){
      clear(*pL);
      free(*pL);
      *pL = NULL;
   }
}

int length(List L){
   if(L==NULL){
      printf("List Error: NULL list\n");
      exit(1);
   }
   return(L->length);
}

int index(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   return (L->index);
}

int front(List L){
   if(L==NULL){
      printf("List Error: calling front() on NULL List reference\n");
      exit(1);
   }
   if(L->length == 0){
      printf("List Error: calling empty List\n");
      exit(1);
   }
   return (L->front->data);
}

int back(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length == 0){
      printf("List Error: calling empty List\n");
      exit(1);
   }
   return (L->back->data);
}

int get(List L){
   if(L==NULL){
      printf("List Error: NULL List Reference\n");
      exit(1);
   }
   if(L->cursor==NULL){
      printf("List Error: NULL cursor\n");
      exit(1);
   }
   return (L->cursor->data);
}

int equals(List A, List B){
   if(A==NULL || B==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   int eq = 0;
   Node N = NULL;
   Node M = NULL;
   eq = (A->length == B->length);
   N = A->front;
   M = B->front;
   while(eq && N!=NULL){
      eq = (N->data == M->data);
      N = N->next;
      M = M->next;
   }
   return eq;
}

void clear(List L){
   if(L==NULL){
      printf("ListError: NULL List reference\n");
      exit(1);
   }
   while(L->length != 0){
      deleteFront(L);
   }
   L->length = 0;
   L->index = -1;
}

void moveFront(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   L->cursor = L->front;
   if(L->length != 0){
      L->index = 0;
   }
}

void moveBack(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length==0){
      printf("List Error: Empty List\n");
      exit(1);
   } 
   L->cursor = L->back;
   L->index = L->length-1;
}

void movePrev(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->cursor==NULL){
      printf("List Error: NULL cursor\n");
      exit(1);
   }
   if(L->cursor==L->front){
      L->cursor = NULL;
      L->index = -1;
   }
   else{
      L->cursor = L->cursor->previous;
      L->index--;
   }
}

void moveNext(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->cursor==NULL){
      printf("List Error: NULL cursor\n");
      exit(1);
   }
   if(L->cursor==L->back){
      L->cursor = NULL;
      L->index = -1;
   }
   else{
      L->cursor = L->cursor->next;
      L->index++;
   }
}

void prepend(List L, int data){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   Node N = newNode(data);
   if(L->length==0){
      L->back = N;
   }
   else{
      N->next = L->front;
      L->front->previous = N;
   }
   L->front = N;
   L->length++;
   if(L->index!=-1){
      L->index++;
   }
}

void append(List L, int data){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   Node N = newNode(data);
   if(L->length==0){
      L->front = N;
   }
   else{
      N->previous = L->back;
      L->back->next = N;
   }
   L-> back = N;
   L->length++;
}

void insertBefore(List L, int data){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length==0){
      append(L,data);
      return;
   }
   if(L->index==0){
      prepend(L,data);
   }
   else{
      Node N = newNode(data);
      N->next = L->cursor;
      N->previous = L->cursor->previous;
      L->cursor->previous->next = N;
      L->cursor->previous = N;
      L->length++;
      L->index++;
   }
}

void insertAfter(List L, int data){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length==0 || L->index==L->length-1){
      append(L,data);
   }
   else{
      Node N = newNode(data);
      N->previous = L->cursor;
      N->next = L->cursor->next;
      L->cursor->next->previous = N;
      L->cursor->next = N;
      L->length++;
   }
}
void deleteFront(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length==0){
      printf("List Error: Empty List\n");
      exit(1);
   } 
   Node N = NULL;
   N = L->front;
   if(L->length==1){
      L->back = NULL;
      L->front = NULL;
   }
   else{
      L->front = L->front->next;
      L->front->previous = NULL;
   }
   if(L->index==0){
      L->cursor->previous = NULL;
      L->cursor->next = NULL;
      L->cursor = NULL;
      L->index = -1;
   }
   else if(L->cursor!=NULL){
      L->index--;
   }
   L->length--;
   freeNode(&N);
}

void deleteBack(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length==0){
      printf("List Error: Empty List\n");
      exit(1);
   }
   Node N = NULL;
   N = L->back;
   if(L->length==1){
      L->front = NULL;
      L->back = NULL;
   }
   else{
      L->back = L->back->previous;
      L->back->next = NULL;
   }
   if(L->index==L->length-1){
      L->cursor->next = NULL;
      L->cursor->previous = NULL;
      L->cursor = NULL;
      L->index = -1;
   }
   L->length--;
   freeNode(&N);
}

void delete(List L){
   if(L==NULL){
      printf("List Error: NULL List reference\n");
      exit(1);
   }
   if(L->length==0){
      printf("List Error: List is empty\n");
      exit(1);
   }
   if(L->cursor==NULL){
      printf("List Error: NULL cursor\n");
      exit(1);
   }
   if(L->index==L->length-1){
      deleteBack(L);
   }
   else if(L->index==0){
      deleteFront(L);
   }
   else{
      Node N = NULL;
      N = L->cursor;
      L->cursor->previous->next = L->cursor->next;
      L->cursor->next->previous = L->cursor->previous;
      L->length--;
      L->index = -1;
      freeNode(&N); 
   }
}

void printList(FILE* out, List L){
   if(L==NULL){
      printf("List Error: NULL List reference");
      exit(1);
   }
   Node N = NULL;
   for(N=L->front; N!=NULL; N=N->next){
      fprintf(out,"%d ", N->data);
   }
}

List copyList(List L){
   if(L==NULL){
      printf("List Error: NULL List reference");
      exit(1);
   }
   List L2 = newList();
   Node N = NULL;
   for(N=L->front; N!=NULL; N=N->next){
      append(L2,N->data);
   }
   return L2;
}
