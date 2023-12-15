// 성공, 2032KB, 8ms
#include <iostream>
#include <cmath>
using namespace std;

double calc_dist(int x1, int x2, int y1, int y2){
    unsigned buf = pow(x1-x2, 2) + pow(y1-y2, 2);
    return sqrt(buf);
}

void swap(int& a, int& b){
    int buf = a;
    a = b;
    b = buf;
}

void sort_coord(int& x1, int& y1, int& r1, int& x2, int& y2, int& r2){
    if(r1 <= r2){
        swap(r1, r2);
        swap(x1, x2);
        swap(y1, y2);
    }
}

int main(){
    
    int N(0);
    int x1, y1, r1, x2, y2, r2;
    double dist(0);
    
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
    
        sort_coord(x1, y1, r1, x2, y2, r2);
    
        dist = calc_dist(x1, x2, y1, y2);
    
        if( dist != 0 ){
            if( r1 > dist+r2 )
                cout << "0" << endl;
            else if( r1+r2 < dist )
                cout << "0" << endl;
            else if( r1+r2 == dist )
                cout << "1" << endl;
            else if( dist+r2 == r1 )
                cout << "1" << endl;
            else
                cout << "2" << endl;
        }
        else{
            if( r1==r2 )
                cout << "-1" << endl;
            else
                cout << "0" << endl;
        }
    }
    
    return 0;
}
