/*
 * Codeforces Round #332 (Div. 2)
 *
 * Problem 599 A. Patrick and Shopping
 *
 * author: yamaton
 * date: 2015-11-20
 *
 */

#include <iostream>
#include <vector>

using namespace std;

int solve(int d1, int d2, int d3) {
    vector<int> v{d1 + d2 + d3,
                  2 * (d1 + d2),
                  2 * (d2 + d3),
                  2 * (d1 + d3)};
    return *min_element(v.begin(), v.end());
}


int main() {
    int d1, d2, d3;
    cin >> d1;
    cin >> d2;
    cin >> d3;
    int ans = solve(d1, d2, d3);
    cout << ans << endl;
}