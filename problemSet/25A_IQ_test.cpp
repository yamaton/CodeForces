/*
 * Codeforces
 *
 * Problem 25 A. IQ test
 *
 * author: yamaton
 * date: 2015-11-26
 * 
 */
#include <algorithm>
#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

bool even(int n) {
    return n % 2 == 0;
}


int solve2(vector<int> xs, int n) {
    auto even_count = count_if(xs.begin(), xs.end(), even);
    auto res = (even_count == 1) ? 
                find_if(xs.begin(), xs.end(), even) - xs.begin()
                : find_if_not(xs.begin(), xs.end(), even) - xs.begin();
    return res + 1;
}


int solve(vector<int> xs, int n) {
    int evens = 0;
    int pos_even, pos_odd;
    for(int i = 0; i < n; ++i) {
        if(xs[i] % 2 == 0) {
            evens++, pos_even = i + 1;
        } else {
            pos_odd = i + 1;
        }
    }
    return (evens == 1) ? pos_even : pos_odd;
}


int main() {
    int n;
    cin >> n;

    vector<int> xs(n);
    for(auto& x: xs) 
        cin >> x;

    cout << solve2(xs, n) << endl;
    return 0;
}