#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<long long> hashes;
vector<long long> primePows;

long long get_hash(int l, int r) {
    return hashes[r + 1] - hashes[l] * primePows[r - l + 1];
}

bool check_two_subs(int a, int b, int c, int d) {
    return get_hash(a, b) == get_hash(c, d);
}

int main() {
    string s;
    cin >> s;
    int m;
    cin >> m;
    const long long PRIME = 1000000000LL + 9LL;

    hashes.resize(s.size() + 1);
    primePows.resize(s.size() + 1);

    hashes[0] = 0;
    primePows[0] = 1;

    for (size_t i = 0; i < s.size(); ++i) {
        hashes[i + 1] = hashes[i] * PRIME + s[i];
        primePows[i + 1] = primePows[i] * PRIME;
    }

    for (int i = 0; i < m; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        --a; --b; --c; --d;
        cout << (check_two_subs(a, b, c, d) ? "Yes" : "No") << endl;
    }

    return 0;
}