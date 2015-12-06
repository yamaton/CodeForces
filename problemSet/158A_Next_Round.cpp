/*
 * Codeforces
 *
 * Problem 158 A. Next Round
 *
 * author: yamaton
 * date: 2015-11-25
 * 
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

typedef long long ll;

int solve(vector<int> xs, int n, int k) {
    int cnt = 0;
    for (int i = 0; i < n && xs[i] >= xs[k-1] && xs[i] > 0; i++)
        cnt++;
    return cnt;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<int> arr(n);
    for(auto& a : arr) 
        cin >> a;

    auto ans = solve(arr, n, k);
    cout << ans << endl;
	return 0;
}
