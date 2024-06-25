#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

const int INF = 1e9;

struct Edge {
    int to;
    int time;
    int cups;
    Edge(int _to, int _time, int _cups) : to(_to), time(_time), cups(_cups) {}
};

int n, m;
vector<vector<Edge>> graph;

int dijkstra(int cups_limit) {
    vector<bool> visited(n + 1, false);
    priority_queue<pair<int, int>> pq;
    pq.push({0, 1}); // Start from node 1

    while (!pq.empty()) {
        auto [time, from] = pq.top();
        pq.pop();
        time = -time;

        if (time > 1440)
            return 0; // Time limit exceeded

        if (from == n)
            return time; // Reached destination

        visited[from] = true;

        for (const auto& edge : graph[from]) {
            if (!visited[edge.to] && edge.cups >= cups_limit) {
                int new_time = time + edge.time;
                if (new_time <= 1440)
                    pq.push({-new_time, edge.to});
            }
        }
    }

    return 0; // Destination not reachable
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n >> m;
    graph.resize(n + 1);

    if (n == 1) {
        cout << 10000000 << endl;
        return 0;
    }

    set<int> unique_cups;

    for (int i = 0; i < m; ++i) {
        int from, to, time, weight;
        cin >> from >> to >> time >> weight;
        int cups = (weight - 3000000) / 100;
        if (cups <= 0)
            continue;

        graph[from].emplace_back(to, time, cups);
        graph[to].emplace_back(from, time, cups);
        unique_cups.insert(cups);
    }

    vector<int> unique_cups_vec(unique_cups.begin(), unique_cups.end());

    int l = 0, r = unique_cups_vec.size() - 1, max_cups = 0;
    while (l <= r) {
        int mid = (l + r) / 2;
        int min_time = dijkstra(unique_cups_vec[mid]);

        if (min_time == 0)
            r = mid - 1;
        else {
            l = mid + 1;
            max_cups = max(max_cups, unique_cups_vec[mid]);
        }
    }

    cout << max_cups << endl;

    return 0;
}