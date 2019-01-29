// Chang Kim
// cnkim
// pa5
//-----------------------------------------------------------------------------
// GraphClient.c
// Test client for the Graph ADT
//-----------------------------------------------------------------------------
#include<stdio.h>
#include<stdlib.h>
#include"List.h"
#include"Graph.h"


int main(int argc, char* argv[]){
   int i, n=8;
   List S = newList();
   Graph G = newGraph(n);
   Graph T=NULL, C=NULL;

   for(i=1; i<=n; i++) append(S, i);

   addArc(G, 1,2);
   addArc(G, 1,5);
   addArc(G, 2,5);
   addArc(G, 2,6);
   addArc(G, 3,2);
   addArc(G, 3,4);
   addArc(G, 3,6);
   addArc(G, 3,7);
   addArc(G, 3,8);
   addArc(G, 6,5);
   addArc(G, 6,7);
   addArc(G, 8,4);
   addArc(G, 8,7);
   printGraph(stdout, G);

   DFS(G, S);
   fprintf(stdout, "\n");
   fprintf(stdout, "x:  d  f  p\n");
   for(i=1; i<=n; i++){
      fprintf(stdout, "%d: %2d %2d %2d\n", i, getDiscover(G, i), getFinish(G, i), getParent(G, i));
   }
   fprintf(stdout, "\n");
   printList(stdout, S);
   fprintf(stdout, "\n");

   T = transpose(G);
   C = copyGraph(G);
   fprintf(stdout, "\n");
   printGraph(stdout, C);
   fprintf(stdout, "\n");
   printGraph(stdout, T);
   fprintf(stdout, "\n");

   DFS(T, S);
   fprintf(stdout, "\n");
   fprintf(stdout, "x:  d  f  p\n");
   for(i=1; i<=n; i++){
      fprintf(stdout, "%d: %2d %2d %2d\n", i, getDiscover(T, i), getFinish(T, i), getParent(T, i));
   }
   fprintf(stdout, "\n");
   printList(stdout, S);
   fprintf(stdout, "\n");

//
   Graph G2 = newGraph(n);
   Graph T2 = NULL, C2 = NULL;
   clear(S);
   for(i=1; i<=n; i++) append(S, i);
   addEdge(G2, 1,2);
   addEdge(G2, 2,3);
   addEdge(G2, 3,4);
   addEdge(G2, 5,6);
   addEdge(G2, 6,7);
   addEdge(G2, 7,8);
   printGraph(stdout, G);
   DFS(G2,S);
   fprintf(stdout, "\n");
   fprintf(stdout, "x:  d  f  p\n");
   for(i=1; i<=n; i++){
      fprintf(stdout, "%d: %2d %2d %2d\n", i, getDiscover(G2, i), getFinish(G2, i), getParent(G2, i));
   }
   fprintf(stdout, "\n");
   printList(stdout, S);
   fprintf(stdout, "\n");

   T2 = transpose(G2);
   C2 = copyGraph(G2);
   fprintf(stdout, "\n");
   printGraph(stdout, C2);
   fprintf(stdout, "\n");
   printGraph(stdout, T2);
   fprintf(stdout, "\n");

   DFS(T2, S);
   fprintf(stdout, "\n");
   fprintf(stdout, "x:  d  f  p\n");
   for(i=1; i<=n; i++){
      fprintf(stdout, "%d: %2d %2d %2d\n", i, getDiscover(T2, i), getFinish(T2, i), getParent(T2, i));
   }
   fprintf(stdout, "\n");
   printList(stdout, S);
   fprintf(stdout, "\n");

   for(int i=1;i<n+1;i++){
      printf("Parent of %d: %d\n",i,getParent(T2,i));
   }

   freeList(&S);
   freeGraph(&G);
   freeGraph(&T);
   freeGraph(&C);
   freeGraph(&G2);
   freeGraph(&T2);
   freeGraph(&C2);
   return(0);
}

