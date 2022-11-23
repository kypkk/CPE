#include <iostream>

using namespace std;

int sol(int i);

int main(){
    int i, j;
    while(cin >> i >> j){
        cout << i << " " << j;
        if(i > j){
            int tmp = i;
            i = j;
            j = tmp;
        }
        int ans = 0;
        for(; i <= j; i++){
            int tmp = sol(i);
            if(ans < tmp)
                ans = tmp;
        }
        cout << " " << ans << endl;
    }
    return 0;
}
int sol(int num){
    int ans = 1;
    while(num != 1){
        if(num % 2 == 0){
            num = num / 2;
        }else{
            num = 3 * num + 1;
        }
        ans++;
    }
    return ans;
}