#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

struct Node {
    int number;
    int segments;
    int set;
    int left;
    int right;
    bool up;

    Node(int n=0, int segments=0, int set=0, int left=0, int right=0, bool up=false) :
        number(n), segments(segments), set(set), left(left), right(right), up(up) {}
};

vector<Node> t;

void build(int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = Node(0, 0, 0, tl, tr, false);
    } else {
        int mid = (tl + tr) / 2;
        build(v * 2, tl, mid);
        build(v * 2 + 1, mid + 1, tr);
        t[v] = Node(0, 0, 0, tl, tr, false);
    }
}

void push(int v) {
    if (!t[v].up) return;

    t[v].number = t[v].set * (t[v].right - t[v].left + 1);
    t[v].segments = t[v].set * 1;
    t[v].up = false;

    if (t[v].left != t[v].right) {
        t[v * 2].set = t[v].set;
        t[v * 2 + 1].set = t[v].set;
        t[v * 2].up = true;
        t[v * 2 + 1].up = true;
    }
}

bool left_is_black(int v) {
    push(v);
    return (t[v].left == t[v].right) ? t[v].number == 1 : left_is_black(v * 2);
}

bool right_is_black(int v) {
    push(v);
    return (t[v].left == t[v].right) ? t[v].number == 1 : right_is_black(v * 2 + 1);
}

void update(int v, int value, int l, int r) {
    if (t[v].right < l || t[v].left > r) return;

    if (t[v].right <= r && t[v].left >= l) {
        t[v].set = value;
        t[v].up = true;
        push(v);
        return;
    }

    push(v);
    update(v * 2, value, l, r);
    update(v * 2 + 1, value, l, r);

    bool left = right_is_black(v * 2);
    bool right = left_is_black(v * 2 + 1);

    t[v].number = t[v * 2].number + t[v * 2 + 1].number;
    t[v].segments = t[v * 2 + 1].segments + t[v * 2].segments - (left && right);
}

int main() {
    int n;
    cin >> n;

    int max_delta = 0;
    int max_cord = INT_MIN;
    vector<char> color;
    vector<int> cord;
    vector<int> delta;

    for (int i = 0; i < n; ++i) {
        char c;
        int co, d;
        cin >> c >> co >> d;
        d = (d > 0) ? (d - 1) : (d + 1);

        max_cord = max(max_cord, co + d);
        max_delta = min(max_delta, co);

        color.push_back(c);
        cord.push_back(co);
        delta.push_back(d);
    }

    int length = (max_delta < 0) ? (max_cord - max_delta + 1) : (max_cord + 1);
    t.resize((4 * length));
    build(1, 0, length);

    for (int i = 0; i < n; ++i) {
        if (color[i] == 'W') {
            update(1, 0, cord[i] - max_delta, cord[i] + delta[i] - max_delta);
            cout << t[1].segments << " " << t[1].number << endl;
        }

        if (color[i] == 'B') {
            update(1, 1, cord[i] - max_delta, cord[i] + delta[i] - max_delta);
            cout << t[1].segments << " " << t[1].number << endl;
        }
    }

    return 0;
}