# 성공
#include <iostream>

#define IS_MUL(year, n) (((year)%(n))?0:1)

using namespace std;

int main(){
    int year{0};
    cin >> year;
    if( IS_MUL(year, 4) && !(IS_MUL(year,100)) || IS_MUL(year, 400))
        cout << "1";
    else
        cout << "0";
    
    return 0;
}
