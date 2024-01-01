// Account.cpp
/* 외부에서 Account객체를 생성해 상호작용하려면
   반드시 비밀번호를 입력해야 한다.
   Private와 Protected 속성 활용?
*/
#include <iostream>
using namespace std;

class Account{
    public:
    void Deposit(double N, int Password){
        if(Password == 1234)
            Money += N;
    }
    void Show(int Password){
        if(Password == 1234)
            cout << Money << endl;
    }
    
    private:
    double Money{0};
    void Deposit(double N){
        Money += N;
    }
    void Show(){
        cout << Money << endl;
    }
};

int main(){
    Account* A = new Account;
    //A->Show();
    A->Deposit(10.0, 1234);
    A->Show(1234);
    Account B;
    B.Deposit(100.2,1234);
    B.Show(1234);
    return 0;
}
