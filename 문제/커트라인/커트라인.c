#include <stdio.h>
#include <stdlib.h>

int compare(int* a, int* b);

int main(){
    int N, k;
    scanf("%d %d", &N, &k);
    
    int* arr = (int*)malloc(sizeof(int)*N);

    for(int j;j<N;j++){
        scanf("%d", &arr[j]);
    }

    qsort(arr, N, sizeof(int), compare);

    printf("%d", arr[k-1]);

    return 0;
}

int compare(int* a, int* b){
    if(*(int*)a < *(int*)b)
        return 1;
    else if(*(int*)a > *(int*)b)
        return -1;
    else
        return 0;
}