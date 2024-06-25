package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type SegmentTreeNode struct {
	start   int
	end     int
	minVal  int
	lazy    int
	left    *SegmentTreeNode
	right   *SegmentTreeNode
}

func buildTree(start, end int) *SegmentTreeNode {
	if start == end {
		node := &SegmentTreeNode{start: start, end: end}
		return node
	}

	mid := (start + end) / 2
	leftChild := buildTree(start, mid)
	rightChild := buildTree(mid+1, end)

	node := &SegmentTreeNode{start: start, end: end}
	node.left = leftChild
	node.right = rightChild

	return node
}

func updateRange(node *SegmentTreeNode, start, end, delta int) {
	if node.start > end || node.end < start {
		return
	}

	if start <= node.start && node.end <= end {
		node.minVal += delta
		node.lazy += delta
		return
	}

	propagateLazy(node)

	updateRange(node.left, start, end, delta)
	updateRange(node.right, start, end, delta)

	node.minVal = min(node.left.minVal, node.right.minVal)
}

func queryRange(node *SegmentTreeNode, start, end int) int {
	if node.start > end || node.end < start {
		return int(^uint(0) >> 1)
	}

	if start <= node.start && node.end <= end {
		return node.minVal
	}

	propagateLazy(node)

	leftMin := queryRange(node.left, start, end)
	rightMin := queryRange(node.right, start, end)

	return min(leftMin, rightMin)
}

func propagateLazy(node *SegmentTreeNode) {
	if node.lazy != 0 {
		node.left.minVal += node.lazy
		node.right.minVal += node.lazy
		node.left.lazy += node.lazy
		node.right.lazy += node.lazy
		node.lazy = 0
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	scanner.Scan()
	m, _ := strconv.Atoi(scanner.Text())

	root := buildTree(0, n-1)

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for i := 0; i < m; i++ {
		scanner.Scan()
		op := scanner.Text()
		if op == "1" {
			scanner.Scan()
			l, _ := strconv.Atoi(scanner.Text())
			scanner.Scan()
			r, _ := strconv.Atoi(scanner.Text())
			scanner.Scan()
			v, _ := strconv.Atoi(scanner.Text())
			updateRange(root, l, r-1, v)
		} else if op == "2" {
			scanner.Scan()
			l, _ := strconv.Atoi(scanner.Text())
			scanner.Scan()
			r, _ := strconv.Atoi(scanner.Text())
			result := queryRange(root, l, r-1)
			fmt.Fprintf(writer, "%d\n", result)
		}
	}
}