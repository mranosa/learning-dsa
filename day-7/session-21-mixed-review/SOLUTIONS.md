# Solutions: Mixed Review - Hardest Blind 75

## Problem 1: Alien Dictionary

### Approach 1: Topological Sort with BFS (Kahn's Algorithm)

```typescript
function alienOrder(words: string[]): string {
    // Build graph
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

    // Compare adjacent words
    for (let i = 0; i < words.length - 1; i++) {
        const word1 = words[i];
        const word2 = words[i + 1];
        const minLen = Math.min(word1.length, word2.length);

        // Check if word2 is prefix of word1 (invalid case)
        if (word1.length > word2.length && word1.startsWith(word2)) {
            return "";
        }

        // Find first different character
        for (let j = 0; j < minLen; j++) {
            if (word1[j] !== word2[j]) {
                if (!graph.get(word1[j])!.has(word2[j])) {
                    graph.get(word1[j])!.add(word2[j]);
                    inDegree.set(word2[j], inDegree.get(word2[j])! + 1);
                }
                break;
            }
        }
    }

    // Topological sort using BFS
    const queue: string[] = [];
    const result: string[] = [];

    // Find nodes with no dependencies
    for (const [char, degree] of inDegree) {
        if (degree === 0) {
            queue.push(char);
        }
    }

    while (queue.length > 0) {
        const char = queue.shift()!;
        result.push(char);

        for (const neighbor of graph.get(char)!) {
            const newDegree = inDegree.get(neighbor)! - 1;
            inDegree.set(neighbor, newDegree);
            if (newDegree === 0) {
                queue.push(neighbor);
            }
        }
    }

    // Check if all characters are processed (no cycle)
    return result.length === inDegree.size ? result.join('') : "";
}

// Time: O(C) where C is total length of all words
// Space: O(U) where U is number of unique characters
```

### Approach 2: DFS with Cycle Detection

```typescript
function alienOrderDFS(words: string[]): string {
    const graph = new Map<string, Set<string>>();

    // Build graph (same as above)
    for (const word of words) {
        for (const char of word) {
            if (!graph.has(char)) {
                graph.set(char, new Set());
            }
        }
    }

    for (let i = 0; i < words.length - 1; i++) {
        const word1 = words[i];
        const word2 = words[i + 1];
        const minLen = Math.min(word1.length, word2.length);

        if (word1.length > word2.length && word1.startsWith(word2)) {
            return "";
        }

        for (let j = 0; j < minLen; j++) {
            if (word1[j] !== word2[j]) {
                graph.get(word1[j])!.add(word2[j]);
                break;
            }
        }
    }

    // DFS with cycle detection
    const visited = new Map<string, number>(); // 0: unvisited, 1: visiting, 2: visited
    const result: string[] = [];

    function dfs(char: string): boolean {
        if (visited.get(char) === 1) return false; // Cycle detected
        if (visited.get(char) === 2) return true;  // Already processed

        visited.set(char, 1); // Mark as visiting

        for (const neighbor of graph.get(char)!) {
            if (!dfs(neighbor)) return false;
        }

        visited.set(char, 2); // Mark as visited
        result.push(char);
        return true;
    }

    // Process all characters
    for (const char of graph.keys()) {
        if (!visited.has(char)) {
            visited.set(char, 0);
        }
    }

    for (const char of graph.keys()) {
        if (visited.get(char) === 0) {
            if (!dfs(char)) return "";
        }
    }

    return result.reverse().join('');
}

// Time: O(C) where C is total length of all words
// Space: O(U) where U is number of unique characters
```

---

## Problem 2: Serialize and Deserialize Binary Tree

### Approach 1: Pre-order Traversal

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

// Time: O(n) for both serialize and deserialize
// Space: O(n) for the serialized string
```

### Approach 2: Level-order Traversal

```typescript
class CodecBFS {
    serialize(root: TreeNode | null): string {
        if (!root) return "";

        const result: string[] = [];
        const queue: (TreeNode | null)[] = [root];

        while (queue.length > 0) {
            const node = queue.shift()!;

            if (node) {
                result.push(node.val.toString());
                queue.push(node.left);
                queue.push(node.right);
            } else {
                result.push('null');
            }
        }

        // Remove trailing nulls
        while (result[result.length - 1] === 'null') {
            result.pop();
        }

        return result.join(',');
    }

    deserialize(data: string): TreeNode | null {
        if (!data) return null;

        const values = data.split(',');
        const root = new TreeNode(parseInt(values[0]));
        const queue: TreeNode[] = [root];
        let i = 1;

        while (queue.length > 0 && i < values.length) {
            const node = queue.shift()!;

            if (i < values.length && values[i] !== 'null') {
                node.left = new TreeNode(parseInt(values[i]));
                queue.push(node.left);
            }
            i++;

            if (i < values.length && values[i] !== 'null') {
                node.right = new TreeNode(parseInt(values[i]));
                queue.push(node.right);
            }
            i++;
        }

        return root;
    }
}

// Time: O(n) for both operations
// Space: O(n) for queue and result
```

---

## Problem 3: Longest Increasing Path in a Matrix

### Approach 1: DFS with Memoization

```typescript
function longestIncreasingPath(matrix: number[][]): number {
    if (!matrix || matrix.length === 0) return 0;

    const m = matrix.length, n = matrix[0].length;
    const memo: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
    let maxPath = 0;

    function dfs(i: number, j: number): number {
        if (memo[i][j] !== 0) return memo[i][j];

        const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];
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

// Time: O(m * n) - each cell visited once
// Space: O(m * n) for memoization
```

### Approach 2: Topological Sort

```typescript
function longestIncreasingPathTopo(matrix: number[][]): number {
    const m = matrix.length, n = matrix[0].length;
    const indegree: number[][] = Array(m).fill(0).map(() => Array(n).fill(0));
    const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    // Calculate indegrees
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (const [di, dj] of directions) {
                const ni = i + di, nj = j + dj;
                if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
                    matrix[ni][nj] > matrix[i][j]) {
                    indegree[ni][nj]++;
                }
            }
        }
    }

    // BFS from cells with indegree 0
    const queue: [number, number][] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (indegree[i][j] === 0) {
                queue.push([i, j]);
            }
        }
    }

    let length = 0;
    while (queue.length > 0) {
        const size = queue.length;
        for (let k = 0; k < size; k++) {
            const [i, j] = queue.shift()!;

            for (const [di, dj] of directions) {
                const ni = i + di, nj = j + dj;
                if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
                    matrix[ni][nj] > matrix[i][j]) {
                    if (--indegree[ni][nj] === 0) {
                        queue.push([ni, nj]);
                    }
                }
            }
        }
        length++;
    }

    return length;
}

// Time: O(m * n)
// Space: O(m * n)
```

---

## Problem 4: Maximum Profit in Job Scheduling

### Approach 1: DP with Binary Search

```typescript
function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
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
    function findLatestNonOverlapping(index: number): number {
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
        const includeProfit = jobs[i][2];
        const latestIndex = findLatestNonOverlapping(i);

        if (latestIndex !== -1) {
            includeProfit += dp[latestIndex];
        }

        dp[i] = Math.max(dp[i - 1], includeProfit);
    }

    return dp[n - 1];
}

// Time: O(n log n) for sorting and binary search
// Space: O(n) for DP array
```

### Approach 2: DP with TreeMap (if available)

```typescript
function jobSchedulingMap(startTime: number[], endTime: number[], profit: number[]): number {
    const n = startTime.length;
    const jobs: [number, number, number][] = [];

    for (let i = 0; i < n; i++) {
        jobs.push([endTime[i], startTime[i], profit[i]]);
    }

    jobs.sort((a, b) => a[0] - b[0]); // Sort by end time

    const dp = new Map<number, number>();
    dp.set(0, 0);

    for (const [end, start, profit] of jobs) {
        // Find max profit before start time
        let prevMax = 0;
        for (const [time, prof] of dp) {
            if (time <= start) {
                prevMax = Math.max(prevMax, prof);
            }
        }

        const currentMax = Array.from(dp.values()).reduce((a, b) => Math.max(a, b), 0);
        dp.set(end, Math.max(currentMax, prevMax + profit));
    }

    return Math.max(...dp.values());
}

// Time: O(n²) due to linear search in map
// Space: O(n)
```

---

## Problem 5: Reverse Nodes in k-Group

### Approach 1: Iterative Reversal

```typescript
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    if (!head || k === 1) return head;

    // Count total nodes
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

### Approach 2: Recursive Reversal

```typescript
function reverseKGroupRecursive(head: ListNode | null, k: number): ListNode | null {
    // Check if we have k nodes
    let curr = head;
    let count = 0;

    while (curr && count < k) {
        curr = curr.next;
        count++;
    }

    if (count === k) {
        // Reverse k nodes
        curr = reverseKGroupRecursive(curr, k);

        // Reverse current k-group
        while (count > 0) {
            const tmp = head!.next;
            head!.next = curr;
            curr = head;
            head = tmp;
            count--;
        }

        head = curr;
    }

    return head;
}

// Time: O(n)
// Space: O(n/k) for recursion stack
```

---

## Problem 6: Minimum Window Subsequence

### Approach 1: Two Pointers

```typescript
function minWindow(s1: string, s2: string): string {
    let minLen = s1.length + 1;
    let minStart = 0;

    let i = 0; // pointer for s1

    while (i < s1.length) {
        let j = 0; // pointer for s2
        let start = i;

        // Find subsequence starting from i
        while (i < s1.length && j < s2.length) {
            if (s1[i] === s2[j]) {
                j++;
            }
            i++;
        }

        // If we didn't find complete subsequence
        if (j < s2.length) break;

        // Move back to find minimum window
        i--; // Back to last matching character
        j--;

        while (j >= 0) {
            if (s1[i] === s2[j]) {
                j--;
            }
            i--;
        }

        i++; // Move to start of window

        if (start - i + s2.length < minLen) {
            minLen = start - i + s2.length;
            minStart = i;
        }

        i++; // Move to next starting position
    }

    return minLen > s1.length ? "" : s1.substring(minStart, minStart + minLen);
}

// Time: O(n * m) where n = s1.length, m = s2.length
// Space: O(1)
```

### Approach 2: Dynamic Programming

```typescript
function minWindowDP(s1: string, s2: string): string {
    const m = s1.length, n = s2.length;
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(-1));

    // dp[i][j] = start index of minimum window in s1[0..i-1] that contains s2[0..j-1]

    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    let minLen = m + 1;
    let minStart = 0;

    for (let i = n; i <= m; i++) {
        if (dp[i][n] !== -1 && i - dp[i][n] < minLen) {
            minLen = i - dp[i][n];
            minStart = dp[i][n];
        }
    }

    return minLen > m ? "" : s1.substring(minStart, minStart + minLen);
}

// Time: O(m * n)
// Space: O(m * n)
```

---

## Problem 7: Wildcard Matching

### Approach 1: Dynamic Programming

```typescript
function isMatch(s: string, p: string): boolean {
    const m = s.length, n = p.length;
    const dp: boolean[][] = Array(m + 1).fill(false).map(() => Array(n + 1).fill(false));

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

// Time: O(m * n)
// Space: O(m * n)
```

### Approach 2: Two Pointers (Greedy)

```typescript
function isMatchGreedy(s: string, p: string): boolean {
    let sIdx = 0, pIdx = 0;
    let starIdx = -1, sTmpIdx = -1;

    while (sIdx < s.length) {
        // If characters match or pattern has '?'
        if (pIdx < p.length && (p[pIdx] === '?' || p[pIdx] === s[sIdx])) {
            sIdx++;
            pIdx++;
        }
        // If pattern has '*'
        else if (pIdx < p.length && p[pIdx] === '*') {
            starIdx = pIdx;
            sTmpIdx = sIdx;
            pIdx++;
        }
        // If current characters don't match, use last '*'
        else if (starIdx !== -1) {
            pIdx = starIdx + 1;
            sTmpIdx++;
            sIdx = sTmpIdx;
        }
        // No match
        else {
            return false;
        }
    }

    // Check remaining pattern characters are all '*'
    while (pIdx < p.length && p[pIdx] === '*') {
        pIdx++;
    }

    return pIdx === p.length;
}

// Time: O(m * n) worst case, O(m + n) average
// Space: O(1)
```

---

## Problem 8: Burst Balloons

### Approach: Interval Dynamic Programming

```typescript
function maxCoins(nums: number[]): number {
    const n = nums.length;
    const balloons = [1, ...nums, 1];
    const dp: number[][] = Array(n + 2).fill(0).map(() => Array(n + 2).fill(0));

    // Length of interval
    for (let len = 1; len <= n; len++) {
        for (let left = 1; left <= n - len + 1; left++) {
            const right = left + len - 1;

            // Try bursting each balloon last in this interval
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

---

## Problem 9: Distinct Subsequences

### Approach 1: 2D Dynamic Programming

```typescript
function numDistinct(s: string, t: string): number {
    const m = s.length, n = t.length;
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Empty t can be formed from any s
    for (let i = 0; i <= m; i++) {
        dp[i][0] = 1;
    }

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            dp[i][j] = dp[i - 1][j]; // Don't use s[i-1]

            if (s[i - 1] === t[j - 1]) {
                dp[i][j] += dp[i - 1][j - 1]; // Use s[i-1]
            }
        }
    }

    return dp[m][n];
}

// Time: O(m * n)
// Space: O(m * n)
```

### Approach 2: Space Optimized DP

```typescript
function numDistinctOptimized(s: string, t: string): number {
    const n = t.length;
    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 0; i < s.length; i++) {
        for (let j = n - 1; j >= 0; j--) {
            if (s[i] === t[j]) {
                dp[j + 1] += dp[j];
            }
        }
    }

    return dp[n];
}

// Time: O(m * n)
// Space: O(n)
```

---

## Problem 10: Basic Calculator III

### Approach: Recursive Descent Parser

```typescript
class Calculator {
    private index = 0;
    private s = '';

    calculate(s: string): number {
        this.s = s.replace(/\s/g, ''); // Remove spaces
        this.index = 0;
        return this.parseExpression();
    }

    private parseExpression(): number {
        const nums: number[] = [];
        const ops: string[] = [];
        nums.push(this.parseTerm());

        while (this.index < this.s.length && this.s[this.index] !== ')') {
            const op = this.s[this.index++];
            if (op === '+' || op === '-') {
                ops.push(op);
                nums.push(this.parseTerm());
            } else {
                break;
            }
        }

        // Calculate result left to right
        let result = nums[0];
        for (let i = 0; i < ops.length; i++) {
            if (ops[i] === '+') {
                result += nums[i + 1];
            } else {
                result -= nums[i + 1];
            }
        }

        return result;
    }

    private parseTerm(): number {
        const nums: number[] = [];
        const ops: string[] = [];
        nums.push(this.parseFactor());

        while (this.index < this.s.length &&
               (this.s[this.index] === '*' || this.s[this.index] === '/')) {
            const op = this.s[this.index++];
            ops.push(op);
            nums.push(this.parseFactor());
        }

        // Calculate result left to right
        let result = nums[0];
        for (let i = 0; i < ops.length; i++) {
            if (ops[i] === '*') {
                result *= nums[i + 1];
            } else {
                result = Math.trunc(result / nums[i + 1]);
            }
        }

        return result;
    }

    private parseFactor(): number {
        if (this.s[this.index] === '(') {
            this.index++; // skip '('
            const result = this.parseExpression();
            this.index++; // skip ')'
            return result;
        } else {
            return this.parseNumber();
        }
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

// Time: O(n) where n is the length of the expression
// Space: O(n) for recursion stack
```

---

## Summary

These hard problems demonstrate:
1. **Complex algorithm design** - Multiple concepts in one problem
2. **Advanced data structures** - Custom implementations
3. **Optimization techniques** - Time/space trade-offs
4. **Edge case handling** - Critical for correctness
5. **Clean implementation** - Managing complexity

Master these problems and you're ready for any interview!