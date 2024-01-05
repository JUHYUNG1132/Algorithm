# 성공
#include<iostream>
#include<string>
using namespace std;

int Instr(char ch, string tar){
    if(tar.find(ch) != string::npos)
        return 1;
    else 
        return 0;
}

int main(){
    string tar[] = {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
    string str;
    cin >> str;
    int len = str.length();
    int cnt{0};
    for(int i=0; i<len; i++){
        for(int j=0; j<8; j++)
            if(Instr(str[i], tar[j]))
                cnt += (3+j);
    }
    cout << cnt;
    return 0;
}