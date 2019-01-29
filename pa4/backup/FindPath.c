// Chang Kim
// cnkim
// pa4

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
         addEdge(G,i,j);
      }
      else{
         break;
      }
   }
   printGraph(out,G);
   int start, end;
   List L = newList();
   while(fscanf(in,"%d %d",&start,&end)==2){
      if(start==0 && end==0){
         break;
      }
      BFS(G,start);
      getPath(L,G,end);
      fprintf(out,"\nThe distance from %d to %d is ", start,end);
      if(getDist(G,end) == INF){
         fprintf(out,"infinity");
         fprintf(out,"\nNo %d-%d path exists",start,end);
      }
      else{
         fprintf(out,"%d",getDist(G,end));
         fprintf(out,"\nA shortest %d-%d path is: ",start,end);
         printList(out,L);
      }
      fprintf(out,"\n");
      clear(L);
   }
   freeGraph(&G);
   freeList(&L);
   fclose(in);
   fclose(out);
}
