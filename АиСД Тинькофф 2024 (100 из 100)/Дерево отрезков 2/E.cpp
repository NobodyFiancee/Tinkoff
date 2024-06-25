#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

void updateSegmentTree(vector<long long> &segmentTree, long long key, long long newValue, long long n) {
    vector<vector<long long>> stack {{1, -1, 0, n}};

    while (!stack.empty()) {
        stack.back()[1]++;
        long long nodeIndex = stack.back()[0];
        long long state = stack.back()[1];
        long long left = stack.back()[2];
        long long right = stack.back()[3];

        if (left > key || right <= key) {
            stack.pop_back();
            continue;
        }
        if (left == right - 1) {
            segmentTree[nodeIndex] = newValue;
            stack.pop_back();
            continue;
        }
        long long mid = (left + right) / 2;
        if (state == 0) {
            stack.push_back({nodeIndex * 2, -1, left, mid});
        } else if (state == 1) {
            stack.push_back({nodeIndex * 2 + 1, -1, mid, right});
        } else {
            stack.pop_back();
            segmentTree[nodeIndex] = segmentTree[nodeIndex * 2] + segmentTree[nodeIndex * 2 + 1];
        }
    }
}

long long querySegmentTree(vector<long long> &segmentTree, long long left, long long right, long long n) {
    vector<vector<long long>> stack {{1, -1, 0, n}};
    long long sum = 0;

    while (!stack.empty()) {
        stack.back()[1]++;
        long long nodeIndex = stack.back()[0];
        long long state = stack.back()[1];
        long long currentLeft = stack.back()[2];
        long long currentRight = stack.back()[3];

        if (left <= currentLeft && currentRight <= right) {
            sum += segmentTree[nodeIndex];
            stack.pop_back();
            continue;
        }
        if (currentLeft >= right || currentRight <= left) {
            stack.pop_back();
            continue;
        }
        long long mid = (currentLeft + currentRight) / 2;
        if (state == 0) {
            stack.push_back({nodeIndex * 2, -1, currentLeft, mid});
        } else if (state == 1) {
            stack.push_back({nodeIndex * 2 + 1, -1, mid, currentRight});
        } else {
            stack.pop_back();
        }
    }
    return sum;
}

unordered_map<long long, long long> compressCoordinates(vector<long long> &coordinates) {
    sort(coordinates.begin(), coordinates.end());
    unordered_map<long long, long long> compressedMap;

    long long count = 0;
    for (long long coord : coordinates) {
        if (compressedMap.find(coord) == compressedMap.end()) {
            compressedMap[coord] = count;
            count++;
        }
    }
    return compressedMap;
}

long long countVisiblePoints(long long n, vector<vector<long long>> &segments) {
    vector<vector<long long>> queries;
    vector<long long> yCoordinates;
    for (long long i = 0; i < n; ++i) {
        long long x1 = segments[i][0], y1 = segments[i][1], x2 = segments[i][2], y2 = segments[i][3];
        if (y1 == y2) {
            yCoordinates.push_back(y1);
            queries.push_back({min(x1, x2), 0, y1});
            queries.push_back({max(x1, x2), 2, y1});
        } else {
            yCoordinates.push_back(y1);
            yCoordinates.push_back(y2);
            queries.push_back({x1, 1, min(y1, y2), max(y1, y2)});
        }
    }
    sort(queries.begin(), queries.end());
    unordered_map<long long, long long> compressedY = compressCoordinates(yCoordinates);
    long long compressedSize = compressedY.size();

    long long visibleCount = 0;
    vector<long long> segmentTree(4 * compressedSize, 0);
    vector<long long> dp_s(compressedSize, 0);
    vector<long long> dp_l(compressedSize, 0);

    long long queryIndex = 0;
    long long queryCount = queries.size();
    while (queryIndex < queryCount) {
        vector<long long> query = queries[queryIndex];
        long long x = query[0];
        if (query[1] == 1) {
            while (queryIndex < queryCount - 1 && queries[queryIndex + 1][0] == x && queries[queryIndex + 1][2] <= query[3] + 1 && queries[queryIndex + 1][1] == 1) {
                query[3] = max(query[3], queries[queryIndex + 1][3]);
                queryIndex++;
            }
            long long sum = querySegmentTree(segmentTree, compressedY[query[2]], compressedY[query[3]] + 1, compressedSize);
            long long length = query[3] - query[2] + 1;
            visibleCount += length - sum;
        } else {
            long long yIndex = compressedY[query[2]];
            dp_s[yIndex] += (query[1] == 2) ? -1 : 1;
            if (dp_s[yIndex] == 0) {
                updateSegmentTree(segmentTree, compressedY[query[2]], 0, compressedSize);
                visibleCount += x - dp_l[yIndex] + 1;
            } else if (query[1] == 0 && dp_s[yIndex] == 1) {
                dp_l[yIndex] = x;
                updateSegmentTree(segmentTree, compressedY[query[2]], 1, compressedSize);
            }
        }
        queryIndex++;
    }
    return visibleCount;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    cin >> n;
    vector<vector<long long>> segments(n, vector<long long>(4));
    for (long long i = 0; i < n; ++i) {
        for (long long j = 0; j < 4; ++j) {
            cin >> segments[i][j];
        }
    }
    long long visibleCount = countVisiblePoints(n, segments);
    cout << visibleCount << endl;

    return 0;
}