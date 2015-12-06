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


pair<int, int> solve(vector<int> xs, int n) {
    map<int, int> frequencyCount;
    for (auto x: xs)
        frequencyCount[x]++;

    auto p = *max_element(frequencyCount.begin(), frequencyCount.end(),
                          [] (const pair<int, int> & p1, const pair<int, int> & p2)
                          {return p1.second < p2.second;}
    );
    return make_pair(p.second, frequencyCount.size());
}


int main() {
    int n;
    cin >> n;
    vector<int> xs(n);
    for(auto& x: xs)
        cin >> x;

    auto res = solve(xs, n);
    cout << res.first << " " << res.second << endl;
}