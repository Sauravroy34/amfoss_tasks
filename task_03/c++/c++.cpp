#include <iostream>
using namespace std;
bool check(int num ) {
    if (num ==2) {
        return true;
    }
    for (int i = 2 ; i < num; i ++) {
        if (num % i == 0) {
            return false;
        }

    }

    return true;

}

int main() {
    int x;
    cout << "enter number";
    cin >> x;
    if (x<=1){
        cout << "prime number not definde";
    }
    else{
        for (int j = 2 ;j<=x;j++){
            if (check(j)){
                cout<< "prime number "<<j<<endl;
            }
        }
    }
}