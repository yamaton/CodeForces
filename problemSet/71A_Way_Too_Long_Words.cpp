/*
 * Codeforces
 *
 * Problem 71 A. Way Too Long Words
 *
 * author: yamaton
 * date: 2015-11-26
 * 
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

string solve(string s) {
    int len = s.size();
    if (len <= 10) {
        return s;
    } else {
        return s.front() + to_string(len - 2) + s.back();
    }
}

int main() {
    int n;
    cin >> n;

    vector<string> arr(n);
    string s;
    for(int i = 0; i < n; i++) {
        cin >> s;
        cout << solve(s) << endl;
    }
	return 0;
}
