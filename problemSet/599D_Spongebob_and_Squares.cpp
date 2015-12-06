/*
 * Codeforces Round #332 (Div. 2)
 *
 * Problem 599 D. Spongebob and Squares
 *
 * author: yamaton
 * date: 2015-11-20
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

using namespace std;

#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
typedef long long ll;


vector<pair<ll, ll>> solve(ll x) {
    vector<pair<ll, ll>> result;
    for(ll n = 1; ; n++) {
        ll num = 6 * x -  n * (n + 1) * (2 * n + 1);
        ll den = 3 * n * (n + 1);
        ll p = num / den;
        if(num < 0) break;
        if(p * den == num) {
            result.push_back(make_pair(n, n + p));
            if(p > 0) result.push_back(make_pair(n + p, n));
        }
    }
    sort(result.begin(), result.end());
    return result;
}


int main() {
    ll x;
    cin >> x;
    auto ps = solve(x);
    cout << ps.size() << endl;
    for(auto p: ps) {cout << p.first << " " << p.second << endl;}

    return 0;
}