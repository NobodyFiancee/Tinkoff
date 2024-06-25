#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int num_monsters;
    cin >> num_monsters;

    vector<int> attack_values(num_monsters + 2), defense_values(num_monsters + 2, INT_MAX);
    for (int i = 1; i <= num_monsters; ++i) cin >> attack_values[i];
    for (int i = 1; i <= num_monsters; ++i) cin >> defense_values[i];

    set<int> left_alive, current_alive;
    for (int i = 0; i < num_monsters + 2; ++i) {
        left_alive.insert(i);
        current_alive.insert(i);
    }

    for (int round = 0; round < num_monsters; ++round) {
        set<int> dead_monsters, next_alive;
        for (int monster_index : current_alive) {
            auto it = left_alive.find(monster_index);
            if (it == left_alive.end()) continue;
            int prev_index = *prev(it);
            int next_index = *next(it);
            if (attack_values[prev_index] + attack_values[next_index] > defense_values[monster_index]) {
                dead_monsters.insert(monster_index);
                next_alive.insert(prev_index);
                next_alive.insert(next_index);
            }
        }
        cout << dead_monsters.size() << ' ';
        for (auto monster_index : dead_monsters) left_alive.erase(monster_index);
        current_alive = next_alive;
    }
    cout << '\n';
}