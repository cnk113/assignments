/*
 * Chang Kim
 * cnkim
 * pa2
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "List.h"
#define MAX_LEN 160

int main(int argc, char* argv[]){
   FILE *in, *out;
   char line[MAX_LEN];
   int count = 0;
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
   int arrlen = 0;
   while(fgets(line,MAX_LEN,in)!=NULL){
      arrlen++;
   }
   fclose(in);
   char* array[arrlen];
   in = fopen(argv[1], "r");
   while(fgets(line,MAX_LEN,in)!=NULL){
      array[count] = malloc(strlen(line)+1);
      strcpy(array[count],line);
      count++;
   }
   List list = newList();
   append(list,0);
   for(int i=1; i<arrlen; i++) {
      for(moveFront(list); index(list)>=0; moveNext(list)){
         if(strcmp(array[i],array[get(list)]) <= 0){
            insertBefore(list,i);
            break;
         }
      }
      if(index(list) == -1){
         append(list,i);
      }
   }
   for(moveFront(list); index(list)>=0; moveNext(list)){
      fprintf(out, "%s", array[get(list)]);
      free(array[get(list)]);
   }   
   fclose(in);
   fclose(out);
   freeList(&list);
   return(0);
}
