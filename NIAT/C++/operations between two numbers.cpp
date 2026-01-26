#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    int b;
    cin >> b;
    char c;
    cin >> c;
    if (c == '+') {
        cout << (a + b);
    }
    if (c == '-') {
        cout << (a - b);
    }
    if (c == '*') {
        cout << (a * b);
    }
    if (c == '/') {
        cout << (a / b);
    }

    return 0;
}