/*
 * Codeforces Round #202 (Div. 2)
 *
 * Problem 349A. Cinema Line
 *
 * author: yamaton
 * date: 2015-12-01
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <tuple>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <cmath>

using namespace std;


string solve(vector<int> xs, int n) {
    int change25 = 0;
    int change50 = 0;
    for (auto x: xs) {
        if (x == 25) {
            change25++;
        } else if (x == 50) {
            change50++;
            change25--;
        } else if (change50 > 0) {
            change50--;
            change25--;
        } else {
            change25 -= 3;
        }
        if (change25 < 0) return "NO";
    }
    return "YES";
}


int main() {
    int n;
    cin >> n;
    vector<int> xs(n);
    for(auto& x: xs)
        cin >> x;

    auto res = solve(xs, n);
    cout << res << endl;
}