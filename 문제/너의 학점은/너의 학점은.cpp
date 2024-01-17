#include<iostream>
#include<string>
#include<map>

using namespace std;

map<string,double> Grades = {
    {"A+", 4.5},
    {"A0", 4.0},
    {"B+", 3.5},
    {"B0", 3.0},
    {"C+", 2.5},
    {"C0", 2.0},
    {"D+", 1.5},
    {"D0", 1.0},
    {"F", 0.0}
};

struct sub_info{
    string name;
    double credit;
    string grade;
};

int main(){
    
    sub_info subs[20];
    double credit_sum{0}, sums{0};
    for(int i=0;i<20;i++){
        cin >> subs[i].name >> subs[i].credit >> subs[i].grade;
        if(subs[i].grade.compare("P") == 0)
            subs[i].credit = 0.0;
    }
    
    for(int i=0; i<20;i++){
        sums += (subs[i].credit * Grades[subs[i].grade]);
        credit_sum += subs[i].credit;
    }
    cout.precision(10);
    cout << sums/credit_sum;
    return 0;
}