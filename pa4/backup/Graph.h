// Chang kim
// cnkim
// pa4

#ifndef _GRAPH_H_INCLUDE_
#define _GRAPH_H_INCLUDE_
#include "List.h"
#define black -5
#define gray -4
#define white -3
#define INF -2
#define NIL -1
typedef struct GraphObj* Graph;

Graph newGraph(int n);

void freeGraph(Graph* pG);

int getOrder(Graph G);
int getSize(Graph G);
int getSource(Graph G);
int getParent(Graph G, int u);
int getDist(Graph G, int u);
void getPath(List L, Graph G, int u);

void makeNull(Graph G);
void addEdge(Graph G, int u, int v);
void addArc(Graph G, int u, int v);
void BFS(Graph G, int s);

void printGraph(FILE* out, Graph G);

#endif
