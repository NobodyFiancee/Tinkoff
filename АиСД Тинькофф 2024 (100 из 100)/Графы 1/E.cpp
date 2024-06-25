#include <iostream>
#include <deque>
#include <vector>
#include <climits>

int min_digit_sum(int K) {
    std::vector<int> visited(K, INT_MAX);
    visited[1] = 1;
    std::deque<int> queue;
    queue.push_back(1);

    while (!queue.empty()) {
        int curr_num = queue.front();
        queue.pop_front();
        int curr_sum = visited[curr_num];

        for (int digit = 0; digit < 10; ++digit) {
            int next_num = (curr_num * 10 + digit) % K;
            int next_sum = curr_sum + digit;

            if (next_sum < visited[next_num]) {
                visited[next_num] = next_sum;
                queue.push_back(next_num);
            }
        }
    }

    return visited[0];
}

int main() {
    int K;
    std::cin >> K;
    std::cout << min_digit_sum(K) << std::endl;
    return 0;
}