/*
 * Codeforces
 *
 * Problem 4 A. Watermelon
 *
 * author: yamaton
 * date: 2015-11-25
 * 
 */

#include <iostream>
#include <string>
using namespace std;

string tf_to_yn(bool tf) {
    return tf ? "YES" : "NO";
}

bool solve(int w) {
    return w > 2 && w % 2 == 0;
}

int main()
{
    int w;
    cin >> w;

    auto ans = tf_to_yn(solve(w));
    cout << ans << endl;
	return 0;
}
