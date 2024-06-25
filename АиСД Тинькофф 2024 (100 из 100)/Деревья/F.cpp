#include <iostream>
#include <unordered_map>
#include <random>
#include <vector>

using namespace std;

class Node {
public:
    int value;
    double priority;
    Node* left;
    Node* right;

    Node(int val) : value(val), priority((double)rand() / RAND_MAX), left(nullptr), right(nullptr) {}
};

class Tree {
public:
    Node* root;
    unordered_map<int, bool> node_dict;

    Tree() : root(nullptr) {}

    void add(int value) {
        if (node_dict.find(value) != node_dict.end())
            return;

        pair<Node*, Node*> parts = split_tree(root, value);
        root = merge_trees(merge_trees(parts.first, new Node(value)), parts.second);
        node_dict[value] = true;
    }

    int next(int value) {
        int pre_value = -1;
        Node* node = root;
        while (node != nullptr) {
            if (value <= node->value) {
                pre_value = node->value;
                node = node->left;
            } else {
                node = node->right;
            }
        }
        return pre_value;
    }

private:
    pair<Node*, Node*> split_tree(Node* node, int value) {
        if (node == nullptr)
            return {nullptr, nullptr};

        if (value <= node->value) {
            pair<Node*, Node*> parts = split_tree(node->left, value);
            node->left = parts.second;
            return {parts.first, node};
        } else {
            pair<Node*, Node*> parts = split_tree(node->right, value);
            node->right = parts.first;
            return {node, parts.second};
        }
    }

    Node* merge_trees(Node* left_node, Node* right_node) {
        if (left_node == nullptr)
            return right_node;
        if (right_node == nullptr)
            return left_node;
        if (right_node->priority <= left_node->priority) {
            right_node->left = merge_trees(left_node, right_node->left);
            return right_node;
        } else {
            left_node->right = merge_trees(left_node->right, right_node);
            return left_node;
        }
    }
};

int main() {
    int n;
    cin >> n;

    char op;
    int value;
    char pre_command_op = '\0';
    int pre_command_value = 0;

    Tree tree;
    for (int i = 0; i < n; ++i) {
        cin >> op >> value;
        if (op == '?') {
            int ans = tree.next(value);
            pre_command_op = op;
            pre_command_value = ans;
            cout << ans << endl;
        } else if (op == '+') {
            if (pre_command_op == '?') {
                tree.add((value + pre_command_value) % 1000000000);
            } else {
                tree.add(value);
            }
            pre_command_op = op;
            pre_command_value = 0;
        }
    }

    return 0;
}