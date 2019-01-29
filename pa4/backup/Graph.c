// Chang Kim
// cnkim
// pa4

#include<stdio.h>
#include<stdlib.h>
#include "Graph.h"
#include "List.h"

typedef struct GraphObj{
   List *neighbors;
   int *color;
   int *distance;
   int *parent;
   int order;
   int size;
   int source;
} GraphObj;

typedef GraphObj* Graph;

Graph newGraph(int n){
   Graph G = malloc(sizeof(GraphObj));
   G->neighbors = calloc(n+1,sizeof(List));
   G->color = calloc(n+1,sizeof(int));
   G->distance = calloc(n+1,sizeof(int));
   G->parent = calloc(n+1,sizeof(int));
   G->order = n;
   G->size = 0;
   G->source = NIL;
   for(int i=1; i<n+1; i++){
      G->color[i] = white;
      G->parent[i] = NIL;
      G->distance[i] = INF;
      G->neighbors[i] = newList();
   }
   return G;
}

void freeGraph(Graph* pG){
   if(*pG == NULL || pG == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   Graph G = *pG;
   for(int i=1; i<getOrder(G)+1; i++){
      freeList(&(G->neighbors[i]));
   }
   free(G->neighbors);
   free(G->color);
   free(G->parent);
   free(G->distance);
   free(G);
   G = NULL;
}

int getOrder(Graph G){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   return G->order;
}

int getSize(Graph G){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   return G->size;
}

int getSource(Graph G){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   return G->source;
}

int getParent(Graph G, int u){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   if(u < 1 || getOrder(G) < u){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   return G->parent[u];
}

int getDist(Graph G, int u){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   if(getOrder(G) < u || u < 1){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   if(getSource(G) == NIL){
      return INF;
   }
   else{
      return G->distance[u];
   }
}

void getPath(List L, Graph G, int u){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   if(getOrder(G) < u || u < 1){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   if(G->source == u){
      append(L,u);
   }
   else if(G->parent[u] != NIL){
      getPath(L,G,G->parent[u]);
      append(L,u);
   }
   else{
      append(L,NIL);
   }
}

void makeNull(Graph G){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   for(int i=1; i<getOrder(G)+1; i++){
      freeList(&(G->neighbors[i]));
      G->neighbors[i] = newList();
      //G->color[i] = white;
      //G->parent[i] = NIL;
      //G->distance[i] = INF;
   }
   G->size = 0;
   G->source = NIL;
}

void addEdge(Graph G, int u, int v){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   if(v<1 || v>getOrder(G)){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   else if(u<1 || u>getOrder(G)){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   List L = G->neighbors[u];
   List L2 = G->neighbors[v];
   for(moveFront(L);index(L)!=-1;moveNext(L)){
      if(get(L) >= v){
         break;
      }
   }
   if(index(L) == -1 || length(L) == 0){
      append(L,v);
   }
   else{
      insertBefore(L,v);
   }
   for(moveFront(L2);index(L2)!=-1;moveNext(L2)){
      if(get(L2) >= u){
         break;
      }
   }
   if(index(L2) == -1 || length(L2) == 0){
      append(L2,u);
   }
   else{
      insertBefore(L2,u);
   }
   G->size++;
}

void addArc(Graph G, int u, int v){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   if(v<1 || v>getOrder(G)){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   else if(u<1 || u>getOrder(G)){
      printf("Graph Error: Order out of bounds\n");
      exit(1);
   }
   List L = G->neighbors[u];
   for(moveFront(L);index(L)!=-1;moveNext(L)){
      if(get(L) >= v){
         break;
      }
   }
   if(index(L) == -1 || length(L) == 0){
      append(L,v);
   }
   else{
      insertBefore(L,v);
   }
   G->size++;
}

void BFS(Graph G, int s){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   for(int i=0; i<getOrder(G)+1; i++){
      G->distance[i] = INF;
      G->color[i] = white;
   }
   List Q = newList();
   G->color[s] = gray;
   G->parent[s] = NIL;
   G->distance[s] = 0;
   G->source = s;
   append(Q,s);
   while(length(Q) != 0){
      int i = front(Q);
      deleteFront(Q);
      List L = G->neighbors[i];
      for(moveFront(L);index(L)!=-1;moveNext(L)){
         if(G->color[get(L)]==white){
            G->color[get(L)] = gray;
            G->distance[get(L)] = G->distance[i]+1;
            G->parent[get(L)] = i;
            append(Q,get(L));
         }
      }
      G->color[i] = black;
   }
   freeList(&Q);
}

void printGraph(FILE* out, Graph G){
   if(G == NULL){
      printf("Graph Error: NULL Graph\n");
      exit(1);
   }
   for(int i=1; i<G->order+1; i++){
      List L = G->neighbors[i];
      fprintf(out,"%d: ",i);
      printList(out,L);
      fprintf(out,"\n");
   }
}
