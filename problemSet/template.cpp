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
#include <cmath>

using namespace std;

#define INF (int)1e9
#define EPS 1e-9
#define all(x) (x).begin(),(x).end()

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
typedef long long ll;

constexpr double pi = 3.14159265358979323846f;

int main()
{
	int n;
    cin >> n;

    VI xs;
    for(auto& x: xs) cin >> x;

    int ans = solve(xs, n);
    cout << ans << endl;
}
