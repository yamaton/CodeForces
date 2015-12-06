// 200 B. Drinks
// @author yamaton
// @date 2015-11-20
//
#include <iostream>
#include <map>
#include <set>
#include <assert.h>
#include <cmath>
#include <vector>
#include <numeric>

using namespace std;

typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);


double solve(vector<int> xs, int n) {
    return (double) accumulate(xs.begin(), xs.end(), 0) / n;
}


int main() {
    int n;
    cin >> n;
    vector<int> xs(n);
    for(auto&& x: xs) cin >> x;

    double ans = solve(xs, n);
    printf("%.12f\n", ans);

    return 0;
}

