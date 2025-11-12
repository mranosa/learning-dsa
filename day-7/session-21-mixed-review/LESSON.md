# Lesson: Mixed Review - All Patterns Combined

---

## 📹 Video 1: Pattern Recognition Strategies (15 min)

**"How to Recognize Patterns in Coding Interview Problems" by NeetCode**
https://www.youtube.com/watch?v=8wywRGRZZmA

**Focus on:**
- Identifying problem types from keywords
- Common patterns across different categories
- Decision tree for choosing approaches
- Time/space trade-off analysis

---

## 📹 Video 2: Mixed Problem-Solving (20 min)

**"Advanced Problem Solving Techniques" by Back to Back SWE**
https://www.youtube.com/watch?v=GBuHSRDGZBY

**Focus on:**
- Breaking down complex problems
- Combining multiple techniques
- Optimization strategies
- Edge case identification

---

## 📹 Video 3: Two Pointers Review (8 min)

**"Two Pointers Technique" by NeetCode**
https://www.youtube.com/watch?v=On03HWe2tZM

**Key patterns:**
- Opposite direction pointers
- Same direction pointers
- Fast/slow pointers

---

## 📹 Video 4: Sliding Window Review (12 min)

**"Sliding Window Template" by NeetCode**
https://www.youtube.com/watch?v=GcW4mgmgSbw

**Key patterns:**
- Fixed size windows
- Variable size windows
- Window with conditions

---

## 📹 Video 5: Binary Search Review (10 min)

**"Binary Search Algorithm" by NeetCode**
https://www.youtube.com/watch?v=s4DPM8ct1pI

**Key patterns:**
- Classic binary search
- Search in rotated array
- Binary search on answer

---

## 📹 Video 6: DFS/BFS Review (15 min)

**"Graph Traversal Algorithms" by NeetCode**
https://www.youtube.com/watch?v=tWVWeAqZ0WU

**Key patterns:**
- Tree/graph DFS
- Level-order BFS
- Memoized DFS (DP)

---

## 📹 Video 7: Dynamic Programming Review (20 min)

**"5 Simple Steps for Solving DP Problems" by NeetCode**
https://www.youtube.com/watch?v=aPQY__2H3tE

**Key patterns:**
- 1D DP (Fibonacci-style)
- 2D DP (grid problems)
- Interval DP
- State machines

---

## 📹 Video 8: Topological Sort (10 min)

**"Topological Sort Algorithm" by NeetCode**
https://www.youtube.com/watch?v=eL-KzMXSXXI

**Key concepts:**
- Kahn's algorithm (BFS)
- DFS with cycle detection
- Applications in dependency ordering

---

## 🎯 Pattern Recognition Guide

### Problem Type → Pattern Mapping

| Problem Description | Pattern | Data Structure |
|---------------------|---------|----------------|
| "Two sum", "pair with target" | Two pointers or Hash map | Array + Map |
| "Substring/subarray with condition" | Sliding window | Array/String |
| "Find in sorted/rotated array" | Binary search | Array |
| "Max/min subarray/path" | DP or Kadane | Array + DP table |
| "Count ways to reach goal" | DP (counting) | DP table |
| "Tree traversal/path" | DFS/BFS | Tree + Stack/Queue |
| "Course scheduling, dependencies" | Topological sort | Graph |
| "Island problems, grid connectivity" | DFS/BFS on grid | 2D array |
| "Anagrams, frequency counting" | Hash map | Map |
| "Parentheses, expression parsing" | Stack | Stack |
| "Shortest path in graph" | BFS | Graph + Queue |
| "Backtracking, all combinations" | DFS | Recursion |

---

## 🧩 Mixed Strategy Patterns

### Strategy 1: Graph Algorithms + Topological Sort

**When:** Dependencies, ordering constraints, cycle detection

**Example: Alien Dictionary**
```typescript
function alienOrder(words: string[]): string {
    // 1. Build graph from character dependencies
    const graph = new Map<string, Set<string>>();
    const inDegree = new Map<string, number>();

    // Initialize all characters
    for (const word of words) {
        for (const char of word) {
            if (!graph.has(char)) {
                graph.set(char, new Set());
                inDegree.set(char, 0);
            }
        }
    }

    // 2. Extract ordering from adjacent words
    for (let i = 0; i < words.length - 1; i++) {
        const w1 = words[i], w2 = words[i + 1];
        const minLen = Math.min(w1.length, w2.length);

        // Invalid case: longer word is prefix
        if (w1.length > w2.length && w1.startsWith(w2)) {
            return "";
        }

        // Find first difference
        for (let j = 0; j < minLen; j++) {
            if (w1[j] !== w2[j]) {
                if (!graph.get(w1[j])!.has(w2[j])) {
                    graph.get(w1[j])!.add(w2[j]);
                    inDegree.set(w2[j], inDegree.get(w2[j])! + 1);
                }
                break;
            }
        }
    }

    // 3. Topological sort (Kahn's algorithm)
    const queue: string[] = [];
    const result: string[] = [];

    for (const [char, degree] of inDegree) {
        if (degree === 0) queue.push(char);
    }

    while (queue.length > 0) {
        const char = queue.shift()!;
        result.push(char);

        for (const neighbor of graph.get(char)!) {
            const newDegree = inDegree.get(neighbor)! - 1;
            inDegree.set(neighbor, newDegree);
            if (newDegree === 0) queue.push(neighbor);
        }
    }

    // Check for cycles
    return result.length === inDegree.size ? result.join('') : "";
}

// Time: O(C) where C is total length of all words
// Space: O(U) where U is unique characters
```

**Pattern:** Graph construction + Topological sort + Cycle detection

---

### Strategy 2: Tree Serialization/Deserialization

**When:** Converting tree structure to/from string representation

**Example: Serialize Binary Tree**
```typescript
class Codec {
    serialize(root: TreeNode | null): string {
        const result: string[] = [];

        function preorder(node: TreeNode | null): void {
            if (!node) {
                result.push('null');
                return;
            }
            result.push(node.val.toString());
            preorder(node.left);
            preorder(node.right);
        }

        preorder(root);
        return result.join(',');
    }

    deserialize(data: string): TreeNode | null {
        const values = data.split(',');
        let index = 0;

        function buildTree(): TreeNode | null {
            if (index >= values.length || values[index] === 'null') {
                index++;
                return null;
            }

            const node = new TreeNode(parseInt(values[index++]));
            node.left = buildTree();
            node.right = buildTree();
            return node;
        }

        return buildTree();
    }
}

// Time: O(n) for both operations
// Space: O(n) for serialized string
```

**Pattern:** Pre-order traversal + Recursion + String parsing

---

### Strategy 3: DFS + Memoization (DP on Grids)

**When:** Finding longest path in grid, counting paths with constraints

**Example: Longest Increasing Path in Matrix**
```typescript
function longestIncreasingPath(matrix: number[][]): number {
    const m = matrix.length, n = matrix[0].length;
    const memo: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
    let maxPath = 0;

    function dfs(i: number, j: number): number {
        if (memo[i][j] !== 0) return memo[i][j];

        const directions = [[0,1], [1,0], [0,-1], [-1,0]];
        let maxLength = 1;

        for (const [di, dj] of directions) {
            const ni = i + di, nj = j + dj;
            if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
                matrix[ni][nj] > matrix[i][j]) {
                maxLength = Math.max(maxLength, 1 + dfs(ni, nj));
            }
        }

        memo[i][j] = maxLength;
        return maxLength;
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            maxPath = Math.max(maxPath, dfs(i, j));
        }
    }

    return maxPath;
}

// Time: O(m*n) - each cell computed once
// Space: O(m*n) for memoization
```

**Pattern:** DFS + Memoization + Grid traversal

---

### Strategy 4: DP + Binary Search (Weighted Intervals)

**When:** Scheduling problems with weights/profits

**Example: Maximum Profit Job Scheduling**
```typescript
function jobScheduling(
    startTime: number[],
    endTime: number[],
    profit: number[]
): number {
    const n = startTime.length;
    const jobs: [number, number, number][] = [];

    for (let i = 0; i < n; i++) {
        jobs.push([startTime[i], endTime[i], profit[i]]);
    }

    // Sort by end time
    jobs.sort((a, b) => a[1] - b[1]);

    const dp: number[] = new Array(n);
    dp[0] = jobs[0][2];

    // Binary search for latest non-overlapping job
    function findLatest(index: number): number {
        let left = 0, right = index - 1;
        let result = -1;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (jobs[mid][1] <= jobs[index][0]) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    for (let i = 1; i < n; i++) {
        let includeProfit = jobs[i][2];
        const latestIndex = findLatest(i);

        if (latestIndex !== -1) {
            includeProfit += dp[latestIndex];
        }

        dp[i] = Math.max(dp[i - 1], includeProfit);
    }

    return dp[n - 1];
}

// Time: O(n log n) for sorting + binary searches
// Space: O(n) for DP array
```

**Pattern:** DP + Binary search + Sorting

---

### Strategy 5: Linked List Pointer Manipulation

**When:** Reversing, reordering, or grouping nodes

**Example: Reverse Nodes in k-Group**
```typescript
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    if (!head || k === 1) return head;

    // Count nodes
    let count = 0;
    let node = head;
    while (node) {
        count++;
        node = node.next;
    }

    const dummy = new ListNode(0);
    dummy.next = head;
    let prevGroup = dummy;

    while (count >= k) {
        let curr = prevGroup.next;
        let next = curr!.next;

        // Reverse k nodes
        for (let i = 1; i < k; i++) {
            curr!.next = next!.next;
            next!.next = prevGroup.next;
            prevGroup.next = next;
            next = curr!.next;
        }

        prevGroup = curr!;
        count -= k;
    }

    return dummy.next;
}

// Time: O(n)
// Space: O(1)
```

**Pattern:** Pointer manipulation + Dummy node + Counting

---

### Strategy 6: Two Pointers + String Matching

**When:** Finding subsequences, windows with conditions

**Example: Minimum Window Subsequence**
```typescript
function minWindow(s1: string, s2: string): string {
    let minLen = s1.length + 1;
    let minStart = 0;
    let i = 0;

    while (i < s1.length) {
        let j = 0;

        // Forward scan: find subsequence
        while (i < s1.length && j < s2.length) {
            if (s1[i] === s2[j]) j++;
            i++;
        }

        if (j < s2.length) break;

        // Backward scan: minimize window
        i--;
        j--;
        while (j >= 0) {
            if (s1[i] === s2[j]) j--;
            i--;
        }

        i++;
        const len = i - 0 + s2.length;
        if (len < minLen) {
            minLen = len;
            minStart = i;
        }

        i++;
    }

    return minLen > s1.length ? "" : s1.substring(minStart, minStart + minLen);
}

// Time: O(m*n) where m = s1.length, n = s2.length
// Space: O(1)
```

**Pattern:** Two pointers + Forward/backward scan

---

### Strategy 7: 2D Dynamic Programming (Pattern Matching)

**When:** String matching with wildcards or patterns

**Example: Wildcard Matching**
```typescript
function isMatch(s: string, p: string): boolean {
    const m = s.length, n = p.length;
    const dp: boolean[][] = Array(m + 1)
        .fill(false)
        .map(() => Array(n + 1).fill(false));

    dp[0][0] = true;

    // Handle patterns starting with *
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (p[j - 1] === '*') {
                dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
            } else if (p[j - 1] === '?' || s[i - 1] === p[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }

    return dp[m][n];
}

// Time: O(m*n)
// Space: O(m*n)
```

**Pattern:** 2D DP + Pattern matching rules

---

### Strategy 8: Interval Dynamic Programming

**When:** Problems on ranges/intervals where order matters

**Example: Burst Balloons**
```typescript
function maxCoins(nums: number[]): number {
    const n = nums.length;
    const balloons = [1, ...nums, 1];
    const dp: number[][] = Array(n + 2)
        .fill(0)
        .map(() => Array(n + 2).fill(0));

    // Try all interval lengths
    for (let len = 1; len <= n; len++) {
        for (let left = 1; left <= n - len + 1; left++) {
            const right = left + len - 1;

            // Try each balloon as last to burst
            for (let k = left; k <= right; k++) {
                const coins = balloons[left - 1] * balloons[k] * balloons[right + 1];
                dp[left][right] = Math.max(
                    dp[left][right],
                    dp[left][k - 1] + coins + dp[k + 1][right]
                );
            }
        }
    }

    return dp[1][n];
}

// Time: O(n³)
// Space: O(n²)
```

**Pattern:** Interval DP + Try all possibilities

---

### Strategy 9: 2D DP (Counting Subsequences)

**When:** Counting ways to form strings/sequences

**Example: Distinct Subsequences**
```typescript
function numDistinct(s: string, t: string): number {
    const m = s.length, n = t.length;
    const dp: number[][] = Array(m + 1)
        .fill(0)
        .map(() => Array(n + 1).fill(0));

    // Empty t can be formed from any s
    for (let i = 0; i <= m; i++) {
        dp[i][0] = 1;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            dp[i][j] = dp[i - 1][j]; // Skip s[i-1]

            if (s[i - 1] === t[j - 1]) {
                dp[i][j] += dp[i - 1][j - 1]; // Use s[i-1]
            }
        }
    }

    return dp[m][n];
}

// Time: O(m*n)
// Space: O(m*n)
```

**Pattern:** 2D DP + Use/skip decisions

---

### Strategy 10: Recursive Descent Parsing

**When:** Evaluating expressions with operator precedence

**Example: Basic Calculator III**
```typescript
class Calculator {
    private index = 0;
    private s = '';

    calculate(s: string): number {
        this.s = s.replace(/\s/g, '');
        this.index = 0;
        return this.parseExpression();
    }

    private parseExpression(): number {
        let result = this.parseTerm();

        while (this.index < this.s.length &&
               (this.s[this.index] === '+' || this.s[this.index] === '-')) {
            const op = this.s[this.index++];
            const term = this.parseTerm();
            result = op === '+' ? result + term : result - term;
        }

        return result;
    }

    private parseTerm(): number {
        let result = this.parseFactor();

        while (this.index < this.s.length &&
               (this.s[this.index] === '*' || this.s[this.index] === '/')) {
            const op = this.s[this.index++];
            const factor = this.parseFactor();
            result = op === '*' ? result * factor : Math.trunc(result / factor);
        }

        return result;
    }

    private parseFactor(): number {
        if (this.s[this.index] === '(') {
            this.index++; // skip '('
            const result = this.parseExpression();
            this.index++; // skip ')'
            return result;
        }
        return this.parseNumber();
    }

    private parseNumber(): number {
        let num = 0;
        while (this.index < this.s.length &&
               this.s[this.index] >= '0' &&
               this.s[this.index] <= '9') {
            num = num * 10 + parseInt(this.s[this.index++]);
        }
        return num;
    }
}

// Time: O(n)
// Space: O(n) for recursion stack
```

**Pattern:** Recursive descent + Operator precedence + State management

---

## 💡 Pattern Recognition Quick Reference

### Time Complexity Hints

| Constraint | Expected Complexity | Pattern |
|------------|---------------------|---------|
| n ≤ 10 | O(n!) | Backtracking all permutations |
| n ≤ 20 | O(2ⁿ) | Backtracking all subsets |
| n ≤ 100 | O(n³) | Interval DP, Floyd-Warshall |
| n ≤ 1000 | O(n²) | DP, nested loops |
| n ≤ 10⁵ | O(n log n) | Sort, heap, binary search |
| n ≤ 10⁶ | O(n) | Hash map, sliding window, DP |
| n > 10⁶ | O(log n) or O(1) | Math, pattern, binary search |

---

## 🎓 Summary: All Patterns Review

### Core Patterns (Must Master)
1. **Two Pointers** - O(n), sorted arrays, pair problems
2. **Sliding Window** - O(n), substring/subarray with condition
3. **Binary Search** - O(log n), sorted arrays, search space
4. **DFS/BFS** - O(V+E), trees, graphs, grids
5. **Dynamic Programming** - Various, optimal substructure
6. **Hash Map** - O(1) lookup, frequency, caching
7. **Stack** - O(n), parentheses, monotonic problems
8. **Heap** - O(log n), k-th elements, priority
9. **Topological Sort** - O(V+E), dependencies, ordering

### Advanced Patterns
10. **Trie** - Prefix searching, word problems
11. **Union Find** - Connected components, MST
12. **Segment Tree** - Range queries, updates
13. **Bit Manipulation** - XOR tricks, subsets
14. **Greedy** - Local optimal → global optimal

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick checklist before solving:**
- [ ] Read problem 2-3 times
- [ ] Identify which patterns apply
- [ ] Consider time/space constraints
- [ ] Plan approach before coding
- [ ] Test with examples
- [ ] Check edge cases

---

[Back to Session README](./README.md)
