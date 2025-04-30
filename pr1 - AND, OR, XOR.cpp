#include <iostream>
#include <iomanip>  // For hex output
#include <cstring>

using namespace std;

int main() {
    string str = "Hello World";
    int len = str.length();
    char str1[11], str2[11], str3[11];

    // AND operation with 127
    cout << "AND Operation (& 127): ";
    for (int i = 0; i < len; i++) {
        str1[i] = str[i] & 127;  
        cout << str1[i];
    }
    cout << endl;

    // XOR operation with 127
    cout << "XOR Operation (^ 127): ";
    for (int i = 0; i < len; i++) {
        str2[i] = str[i] ^ 127;  
        cout << str2[i];
    }
    cout << endl;

    // OR operation with  127 
    cout << "OR Operation (| 127): ";
    for (int i = 0; i < len; i++) {
        str3[i] = str[i] | 127;  
        cout << str3[i];
    }
    cout << endl;

    return 0;
}
