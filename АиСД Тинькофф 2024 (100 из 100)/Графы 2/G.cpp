#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const long long LLONG_MAX_VAL = 1e18;

vector<long long> dijkstra(vector<vector<pair<int, long long>>>& graph, int start) {
    int n = graph.size();
    vector<long long> distances(n, LLONG_MAX_VAL);
    distances[start] = 0;

    set<pair<long long, int>> queue;
    queue.insert({0, start});

    while (!queue.empty()) {
        auto [distance, u] = *queue.begin();
        queue.erase(queue.begin());

        for (auto [v, length] : graph[u]) {
            if (distances[v] > distances[u] + length) {
                queue.erase({distances[v], v});
                distances[v] = distances[u] + length;
                queue.insert({distances[v], v});
            }
        }
    }

    return distances;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, long long>>> graph(n);

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        u--;
        v--;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    int a, b, c;
    cin >> a >> b >> c;
    a--;
    b--;
    c--;

    vector<long long> distances_from_a = dijkstra(graph, a);
    vector<long long> distances_from_b = dijkstra(graph, b);
    vector<long long> distances_from_c = dijkstra(graph, c);

    long long res = LLONG_MAX_VAL;
    for (int i = 0; i < n; ++i) {
        long long distance_from_a_to_x = distances_from_a[i];
        long long distance_from_b_to_x = distances_from_b[i];
        long long distance_from_c_to_x = distances_from_c[i];

        if (distance_from_a_to_x != LLONG_MAX_VAL || distance_from_b_to_x != LLONG_MAX_VAL || distance_from_c_to_x != LLONG_MAX_VAL) {
            long long min_distance = min({distance_from_a_to_x, distance_from_b_to_x, distance_from_c_to_x});
            if (min_distance == distance_from_a_to_x) {
                res = min(res, 2 * min_distance + distance_from_b_to_x + distance_from_c_to_x);
            }
            if (min_distance == distance_from_b_to_x) {
                res = min(res, 2 * min_distance + distance_from_a_to_x + distance_from_c_to_x);
            }
            if (min_distance == distance_from_c_to_x) {
                res = min(res, 2 * min_distance + distance_from_b_to_x + distance_from_a_to_x);
            }
        }
    }

    if (res != LLONG_MAX_VAL) {
        cout << res << endl;
    } else {
        cout << "-1" << endl;
    }

    return 0;
}