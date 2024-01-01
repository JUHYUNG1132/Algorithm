# 성공
#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int dice[3] = {0,};
    int cnt{0};
    int buff;
    cin >> dice[0] >> dice[1] >> dice[2];
    if(dice[0] == dice[1]){
        cnt++;
        buff = dice[0];}
    if(dice[0] == dice[2]){
        cnt++;
        buff = dice[0];}
    if(dice[1] == dice[2]){
        cnt++;
        buff = dice[1];}
    
    switch(cnt){
        case 0:
            buff = *max_element(begin(dice), end(dice));
            cout << buff*100;
            break;
        case 1:
            cout << buff*100 + 1000;
            break;
        case 3:
            cout << buff*1000 + 10000;
            break;
    }
    return 0;
}