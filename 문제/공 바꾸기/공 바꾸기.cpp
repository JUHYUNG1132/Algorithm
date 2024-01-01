# 성공

#include <iostream>
using namespace std;

void Swap(int bucket[], int i, int j){
    int buff;
    buff = bucket[i];
    bucket[i] = bucket[j];
    bucket[j] = buff;
}

int main(){
    int N{0}, M{0};
    cin >> N >> M;
    int* bucket = new int[N];
    for(int i=0; i<N; i++)
        bucket[i] = i+1;
    int i{0}, j{0};
    for(int _=0;_<M; _++){
        cin >> i >> j;
        Swap(bucket, i-1, j-1);
    }
    for(int i=0; i<N; i++)
        cout << bucket[i] << " ";
    
    delete[] bucket;
    
    return 0;
}