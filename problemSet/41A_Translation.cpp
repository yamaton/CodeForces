/*
 * Codeforces
 *
 * Problem 41 A. Translation
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


string tf_to_yn(bool tf) {
    return (tf) ? "YES" : "NO";
}


bool solve2(string s, string t) {
    return s.size() == t.size() && equal(s.begin(), s.end(), t.rbegin());
}


bool solve(string s, string t) {
    reverse(s.begin(), s.end());
    return s == t;
}


int main() {
    string s, t;
    cin >> s >> t;
    cout << tf_to_yn(solve2(s, t)) << endl;
    return 0;
}