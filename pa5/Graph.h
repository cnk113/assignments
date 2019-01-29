// Chang kim
// cnkim
// pa5

#ifndef _GRAPH_H_INCLUDE_
#define _GRAPH_H_INCLUDE_
#include "List.h"
#define black -6
#define gray -5
#define white -4
#define INF -3
#define NIL -2
#define UNDEF -1
typedef struct GraphObj* Graph;
Graph newGraph(int n);
void freeGraph(Graph* pG);
int getOrder(Graph G);
int getSize(Graph G);
int getSource(Graph G);
int getParent(Graph G, int u);
int getDiscover(Graph G, int u);
int getFinish(Graph G, int u);
int getDist(Graph G, int u);
void getPath(List L, Graph G, int u);
void makeNull(Graph G);
void addEdge(Graph G, int u, int v);
void addArc(Graph G, int u, int v);
void DFS(Graph G, List S);
void visit(Graph G, int u, List L2);
void BFS(Graph G, int s);
Graph transpose(Graph G);
Graph copyGraph(Graph G);
void printGraph(FILE* out, Graph G);

#endif
