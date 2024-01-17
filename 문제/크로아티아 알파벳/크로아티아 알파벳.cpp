# 성공
#include<iostream>
#include<string>

using namespace std;

int kwrd_count(string& kwrd, string& str){
    int idx{-1};
    int cnt{0};
    while((idx = str.find(kwrd)) != string::npos){
        str[idx+1] = '0';
        cnt++;
    }
    
    return cnt;    
}

int main(){
    string kwrd[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    string asd;
    cin >> asd;
    int len = asd.length();
    int alp{len};
    for(int i=0; i<8; i++){
        alp -= kwrd_count(kwrd[i], asd) * (kwrd[i].length() - 1);
    }
    cout << alp;
    
    return 0;
}
