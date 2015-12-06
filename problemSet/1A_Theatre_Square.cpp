/*
 * Codeforces
 *
 * Problem 1 A. Theatre Square
 *
 * author: yamaton
 * date: 2015-11-25
 *
 */

#include <iostream>
using namespace std;

typedef long long ll;


ll solve(ll n, ll m, ll a) {
    return ((n + a - 1) / a) * ((m + a - 1) / a);
}

int main()
{
    ll n, m, a;
    cin >> n >> m >> a;

    auto ans = solve(n, m, a);
    cout << ans << endl;
	return 0;
}
