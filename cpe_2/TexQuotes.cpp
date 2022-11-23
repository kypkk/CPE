#include <iostream>
#include <string>

using namespace std;

int main(){
    string in;
    int quote = 0;
    while(getline(cin, in)){
        
        for(char const &c: in){
            if(c == '"' && quote == 0){
                cout << "``";
                quote = 1;
            }else if(c == '"' && quote == 1){
                cout << "''";
                quote = 0;
            }else{
                cout << c;
            }
        }
        cout << "\n";
    }
}