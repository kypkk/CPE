#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void ans();

int main(){
    
    int datas;
    cin >> datas;
    while(datas--){
        ans();
    }
    

    return 0;
}

void ans(){
    int train_len;
    vector<int> train;
    cin >> train_len;
    for(int i = 0; i < train_len; i++){
        int tmp;
        cin >> tmp;
        train.push_back(tmp);
    }
    int count = 0;
    for(int i = 0; i < train_len - 1; i++){
        for(int j = 0; j < train_len - i - 1; j++){
            if(train[j] > train[j + 1]){
                swap(train[j], train[j + 1]);
                count += 1;
            }
        }
    }
    cout << "Optimal train swapping takes " << count << " swaps.\n";
}