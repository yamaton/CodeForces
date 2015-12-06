/*
 * Codeforces
 *
 * Problem 124 A. The number of positions
 *
 * author: yamaton
 * date: 2015-12-01
 *
 */

#include <iostream>

using namespace std;

int solve(int n, int a, int b) {
    return n - max(1 + a, n - b) + 1;
}


int main() {
    int n, a, b;
    cin >> n >> a >> b;
    auto ans = solve(n, a, b);
    cout << ans << endl;

}