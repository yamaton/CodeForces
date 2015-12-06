/*
 * Codeforces Round #247 (Div. 2)
 *
 * Problem 431 A. Black Square
 *
 * author: yamaton
 * date: 2015-12-01
 *
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(vector<int> a, string s) {
    int total = 0;
    for (auto c: s) {
        int i = c - '1';
        total += a[i];
    }
    return total;
}


int main() {
    vector<int> a(4);
    for(auto& x: a)
        cin >> x;

    string s;
    cin >> s;

    auto ans = solve(a, s);
    cout << ans << endl;

}