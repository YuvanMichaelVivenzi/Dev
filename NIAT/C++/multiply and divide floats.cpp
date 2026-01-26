#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a;
    cin >> a;
    double b;
    cin >> b;
    cout << fixed << setprecision(2) << double(a * b) << endl;
    if (b != 0) {
        cout << double(a / b) << endl;
    }
    else {
        cout << "Undefined" << endl;
    }

    return 0;
}