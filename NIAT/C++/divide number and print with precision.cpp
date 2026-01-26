#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    long long a;
    cin >> a;
    double b;
    cin >> b;
    double c;
    c = (a / b);
    cout << fixed << setprecision(2) << double(c) << endl;

    return 0;
}