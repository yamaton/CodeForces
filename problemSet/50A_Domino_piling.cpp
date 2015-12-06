/*
 * Codeforces
 *
 * Problem 50 A. Domino piling
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


int solve(int m, int n) {
    return m * n / 2
}


int main() {
    string m, n;
    cin >> m >> n;
    cout << solve(m, n) << endl;
    return 0;
}