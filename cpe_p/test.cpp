#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
// #include <bits/stdc++.h>
#define fastio cin.tie(0);cout.tie(0);

using namespace std;

// Bicoloring
// int main(){
//     int stop = 0;
//     while (stop == 0){
//         int points;
//         int sides;
//         cin >> points;
//         if (points == 0) break;
//         cin >> sides;
//         int arr[200] = {0};
//         bool ans = true;
//         for(int i = 0; i < sides; i++){
//             int a, b;
//             cin >> a >> b;
//             if(!arr[a] && !arr[b]){
//                 arr[a] = 1;
//                 arr[b] = 2;
//             }
//             if(arr[a] && arr[a] == 1 && !arr[b]){
//                 arr[b] = 2;
//             }
//             if(arr[a] && arr[a] == 2 && !arr[b]){
//                 arr[b] = 1;
//             }
//             if(arr[b] && arr[b] == 1 && !arr[a]){
//                 arr[a] = 2;
//             }
//             if(arr[b] && arr[a] == 2 && !arr[a]){
//                 arr[b] = 1;
//             }
//             if(arr[a] && arr[b] && arr[a] == arr[b]){
//                 ans = false;
//             }
//         }
//         if( ans == true){
//             cout << "BICOLORABLE." << endl;
//         }else{
//             cout << "NOT BICOLORABLE." << endl;
//         }
//     }
// }

// the 3n +1 problem
// int cycle_length(int n){
//     if (n == 1) return 1;
//     if( n % 2 == 1) {
//         return cycle_length(3 * n + 1) + 1;
//     }else{
//         return cycle_length(n / 2) + 1;
//     }
// }

// int main(){
//     int a, b;
//     while(cin >> a >> b){
//         int l = min(a, b);
//         int r = max(a, b);
//         int ans = 0;
//         for(int i = l; i <= r; i++){
//             ans = max(ans, cycle_length(i));
//         }
//         cout << a << " " << b << " " << ans << endl;
//     }
// }

// hashmat the brave warrior

// int main(){
//     long long int a, b;
//     while(cin >> a >> b){
//         long long int ans = 0;
//         if (a >= b) {
//             ans = a - b;
//         }else{
//             ans = b - a;
//         }
//         cout << ans << endl;
//     }
// }

// cryptanalysis

// int main(){
//     int t;
//     int alph_list[26] = {0};
//     cin >> t;
//     char c;
//     char char_list[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//     c = getchar();
//     for(int i = 0; i < t; i++){
//         while((c = getchar())){
//             if(c == '\n') break;
//             else if(c == 'A' || c == 'a'){
//                 alph_list[0]++;
//             }else if(c == 'B' || c == 'b'){
//                 alph_list[1]++;
//             }else if(c == 'C' || c == 'c'){
//                 alph_list[2]++;
//             }else if(c == 'D' || c == 'd'){
//                 alph_list[3]++;
//             }else if(c == 'E' || c == 'e'){
//                 alph_list[4]++;
//             }else if(c == 'F' || c == 'f'){
//                 alph_list[5]++;
//             }else if(c == 'G' || c == 'g'){
//                 alph_list[6]++;
//             }else if(c == 'H' || c == 'h'){
//                 alph_list[7]++;
//             }else if(c == 'I' || c == 'i'){
//                 alph_list[8]++;
//             }else if(c == 'J' || c == 'j'){
//                 alph_list[9]++;
//             }else if(c == 'K' || c == 'k'){
//                 alph_list[10]++;
//             }else if(c == 'L' || c == 'l'){
//                 alph_list[11]++;
//             }else if(c == 'M' || c == 'm'){
//                 alph_list[12]++;
//             }else if(c == 'N' || c == 'n'){
//                 alph_list[13]++;
//             }else if(c == 'O' || c == 'o'){
//                 alph_list[14]++;
//             }else if(c == 'P' || c == 'p'){
//                 alph_list[15]++;
//             }else if(c == 'Q' || c == 'q'){
//                 alph_list[16]++;
//             }else if(c == 'R' || c == 'r'){
//                 alph_list[17]++;
//             }else if(c == 'S' || c == 's'){
//                 alph_list[18]++;
//             }else if(c == 'T' || c == 't'){
//                 alph_list[19]++;
//             }else if(c == 'U' || c == 'u'){
//                 alph_list[20]++;
//             }else if(c == 'V' || c == 'v'){
//                 alph_list[21]++;
//             }else if(c == 'W' || c == 'w'){
//                 alph_list[22]++;
//             }else if(c == 'X' || c == 'x'){
//                 alph_list[23]++;
//             }else if(c == 'Y' || c == 'y'){
//                 alph_list[24]++;
//             }else if(c == 'Z' || c == 'z'){
//                 alph_list[25]++;
//             }
//         }
//     }
//         for(int i = 0; i < 26; i++){
//             for(int j = 0; j < 25 - i; j++){
//                 if(alph_list[j] < alph_list[j+1]){
//                     int temp = alph_list[j];
//                     alph_list[j] = alph_list[j+1];
//                     alph_list[j+1] = temp;  
//                     char temp_c = char_list[j];
//                     char_list[j] = char_list[j+1];
//                     char_list[j+1] = temp_c;
//                 }
//             }
//         }

//         for(int i = 0; i < 26; i++){
//             if(alph_list[i] != 0){
//                 cout << char_list[i] << ' ' << alph_list[i] << endl;
//             }
            
//         }
// }

