// 성공, 2180KB, 1772ms
#include <iostream>
using namespace std;

#define MAXN 10001

int main(){
    
    ios::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    int* list = new int[MAXN];
    
    int N(0);
    int buff(0);
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> buff;
        list[buff]++;
    }
        
    
    for(int i=1; i<MAXN; i++){
        buff = list[i];
        for(int j=0; j<buff; j++)
            cout << i << '\n';
    }
    
    
    delete[] list;
    return 0;
}
