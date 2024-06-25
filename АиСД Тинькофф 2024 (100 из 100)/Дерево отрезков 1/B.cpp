#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

class SegmentTree {
private:
    vector<pair<int, int>> tree;
    vector<int> arr;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = make_pair(arr[start], 1);
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            arr[idx] = val;
            tree[node] = make_pair(val, 1);
        } else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid) {
                update(2 * node + 1, start, mid, idx, val);
            } else {
                update(2 * node + 2, mid + 1, end, idx, val);
            }
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    pair<int, int> query(int node, int start, int end, int left, int right) {
        if (start > right || end < left) {
            return make_pair(INT_MAX, 0);
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        pair<int, int> left_min = query(2 * node + 1, start, mid, left, right);
        pair<int, int> right_min = query(2 * node + 2, mid + 1, end, left, right);
        return merge(left_min, right_min);
    }

    pair<int, int> merge(pair<int, int> left, pair<int, int> right) {
        int left_min = left.first;
        int left_count = left.second;
        int right_min = right.first;
        int right_count = right.second;
        int min_val = min(left_min, right_min);
        int count = 0;
        if (left_min == right_min) {
            count = left_count + right_count;
        } else if (left_min == INT_MAX || right_min == INT_MAX) {
            count = left_count + right_count;
        } else {
            count = (left_min == min_val ? left_count : 0) + (right_min == min_val ? right_count : 0);
        }
        return make_pair(min_val, count);
    }

public:
    SegmentTree(vector<int>& arr) : arr(arr) {
        tree.resize(4 * arr.size());
        build(0, 0, arr.size() - 1);
    }

    void update(int idx, int val) {
        update(0, 0, arr.size() - 1, idx, val);
    }

    pair<int, int> query(int left, int right) {
        return query(0, 0, arr.size() - 1, left, right);
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    SegmentTree seg_tree(arr);

    for (int i = 0; i < m; i++) {
        int op, l, r;
        cin >> op >> l >> r;
        if (op == 2) {
            pair<int, int> result = seg_tree.query(l, r - 1);
            cout << result.first << " " << result.second << endl;
        } else if (op == 1) {
            seg_tree.update(l, r);
        }
    }

    return 0;
}