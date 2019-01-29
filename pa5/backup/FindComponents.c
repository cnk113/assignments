// Chang Kim
// cnkim
// pa5

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "Graph.h"
#include "List.h"

int main(int argc, char* argv[]){
   FILE *in, *out;
   
   if(argc != 3){
      printf("Usage: %s <input file> <output file>\n", argv[0]);
      exit(1);
   }
   in = fopen(argv[1], "r");
   out = fopen(argv[2], "w");
   if(in==NULL){
      printf("Unable to open file %s for writing\n", argv[1]);
      exit(1);
   }
   if(out==NULL){
      printf("Unable to open file %s for writing\n", argv[2]);
      exit(1);
   }
   int n;
   fscanf(in,"%d", &n);
   Graph G = newGraph(n);
   int i,j;
   while(fscanf(in,"%d %d",&i,&j)==2){
      if(i!=0 && j!=0){
         addArc(G,i,j);
      }
      else{
         break;
      }
   }
   fprintf(out,"Adjacency list representation of G:\n");
   printGraph(out,G);
   List L = newList();
   for(int i=1;i<n+1;i++){
      append(L,i); 
   }
   DFS(G,L);
   Graph G2 = transpose(G);
   DFS(G2,L);
   moveFront(L);
   int prev = get(L);
   moveNext(L);
   int count = 1;
   for(;index(L)!=-1;moveNext(L)){
      if(getDiscover(G2,prev)>getFinish(G2,get(L))){
         prev = get(L);
         count++;
      }
   }
   fprintf(out,"\nG contains %d strongly connected components:",count);
   List L2 = newList();
   int o = 1;
   for(moveBack(L);index(L)!=-1;movePrev(L)){
      prepend(L2,get(L));
      if(getParent(G2,get(L))==NIL){
         fprintf(out,"\nComponent %d: ",o);
         printList(out,L2);
         clear(L2);
         o++;
      }
   }
   fprintf(out,"\n");
   freeGraph(&G);
   freeGraph(&G2);
   freeList(&L);
   freeList(&L2);
   fclose(in);
   fclose(out);
}
