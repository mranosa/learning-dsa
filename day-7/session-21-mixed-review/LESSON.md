# Lesson: Mixed Review - Hardest Blind 75 Problems

## Introduction

Welcome to the final session! Today we tackle the most challenging problems that combine multiple concepts and require deep algorithmic thinking. These problems test your ability to synthesize everything you've learned.

---

## Part 1: Advanced Problem-Solving Strategies

### Video: Complex Algorithm Design
- **Link:** https://www.youtube.com/watch?v=8gwka5hc7c4
- **Duration:** 15 minutes
- **Focus:** Breaking down hard problems

### Key Takeaways:
1. **Decomposition** - Break complex problems into subproblems
2. **Pattern Recognition** - Identify hidden structures
3. **Optimization Layers** - Start simple, then optimize
4. **Edge Case Analysis** - Systematic boundary testing

---

## Part 2: Graph Algorithms - Topological Sort

### Video: Topological Sort Deep Dive
- **Link:** https://www.youtube.com/watch?v=eL-KzMXSXXI
- **Duration:** 12 minutes
- **Focus:** Alien Dictionary problem

### Core Concepts:

**Topological Sort:**
```typescript
// Build graph from dependencies
// Detect cycles
// Return valid ordering

function topologicalSort(graph: Map<string, Set<string>>): string[] {
    const inDegree = new Map<string, number>();
    const queue: string[] = [];
    const result: string[] = [];

    // Calculate in-degrees
    for (const [node, neighbors] of graph) {
        if (!inDegree.has(node)) inDegree.set(node, 0);
        for (const neighbor of neighbors) {
            inDegree.set(neighbor, (inDegree.get(neighbor) || 0) + 1);
        }
    }

    // Find nodes with no dependencies
    for (const [node, degree] of inDegree) {
        if (degree === 0) queue.push(node);
    }

    // Process queue
    while (queue.length > 0) {
        const node = queue.shift()!;
        result.push(node);

        for (const neighbor of (graph.get(node) || [])) {
            const newDegree = inDegree.get(neighbor)! - 1;
            inDegree.set(neighbor, newDegree);
            if (newDegree === 0) queue.push(neighbor);
        }
    }

    return result.length === inDegree.size ? result : [];
}
```

---

## Part 3: Tree Serialization

### Video: Serialize/Deserialize Trees
- **Link:** https://www.youtube.com/watch?v=u4JAi2JJhI8
- **Duration:** 14 minutes
- **Focus:** Tree codec design

### Design Patterns:

**Pre-order Traversal Approach:**
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
            if (values[index] === 'null') {
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
```

---

## Part 4: Dynamic Programming on Grids

### Video: DP in 2D Matrices
- **Link:** https://www.youtube.com/watch?v=wCc_nd-GiEc
- **Duration:** 16 minutes
- **Focus:** Longest increasing path

### Advanced DP Patterns:

**Memoized DFS:**
```typescript
function longestIncreasingPath(matrix: number[][]): number {
    const m = matrix.length, n = matrix[0].length;
    const memo = Array(m).fill(0).map(() => Array(n).fill(0));
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
```

---

## Part 5: Complex Linked List Manipulation

### Video: K-Group Reversal
- **Link:** https://www.youtube.com/watch?v=1UOPsfP85V4
- **Duration:** 13 minutes
- **Focus:** Reverse nodes in k-group

### Implementation Strategy:

```typescript
function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    // Count nodes
    let count = 0;
    let node = head;
    while (node) {
        count++;
        node = node.next;
    }

    // Process k groups
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
```

---

## Part 6: String Pattern Matching

### Video: Wildcard and Regular Expression
- **Link:** https://www.youtube.com/watch?v=l3hda49XcDE
- **Duration:** 18 minutes
- **Focus:** Pattern matching DP

### DP Table Approach:

```typescript
function wildcardMatch(s: string, p: string): boolean {
    const m = s.length, n = p.length;
    const dp = Array(m + 1).fill(false).map(() => Array(n + 1).fill(false));

    dp[0][0] = true;

    // Handle patterns starting with *
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*') {
            dp[0][j] = dp[0][j - 1];
        }
    }

    // Fill DP table
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
```

---

## Part 7: Interval Dynamic Programming

### Video: Burst Balloons Strategy
- **Link:** https://www.youtube.com/watch?v=VFskby7lUbw
- **Duration:** 20 minutes
- **Focus:** Interval DP technique

### Interval DP Pattern:

```typescript
function burstBalloons(nums: number[]): number {
    const n = nums.length;
    const balloons = [1, ...nums, 1];
    const dp = Array(n + 2).fill(0).map(() => Array(n + 2).fill(0));

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
```

---

## Part 8: Expression Parsing

### Video: Calculator Implementation
- **Link:** https://www.youtube.com/watch?v=vq-nUF0G4fI
- **Duration:** 22 minutes
- **Focus:** Recursive descent parsing

### Parser Design:

```typescript
class Calculator {
    private index = 0;
    private s = '';

    calculate(s: string): number {
        this.s = s;
        this.index = 0;
        return this.expression();
    }

    private expression(): number {
        let result = this.term();

        while (this.index < this.s.length) {
            const op = this.s[this.index];
            if (op === '+' || op === '-') {
                this.index++;
                const term = this.term();
                result = op === '+' ? result + term : result - term;
            } else {
                break;
            }
        }

        return result;
    }

    private term(): number {
        let result = this.factor();

        while (this.index < this.s.length) {
            const op = this.s[this.index];
            if (op === '*' || op === '/') {
                this.index++;
                const factor = this.factor();
                result = op === '*' ? result * factor : Math.floor(result / factor);
            } else {
                break;
            }
        }

        return result;
    }

    private factor(): number {
        this.skipWhitespace();

        if (this.s[this.index] === '(') {
            this.index++; // skip '('
            const result = this.expression();
            this.index++; // skip ')'
            return result;
        }

        return this.number();
    }

    private number(): number {
        this.skipWhitespace();
        let num = 0;
        let negative = false;

        if (this.s[this.index] === '-') {
            negative = true;
            this.index++;
        }

        while (this.index < this.s.length &&
               this.s[this.index] >= '0' &&
               this.s[this.index] <= '9') {
            num = num * 10 + parseInt(this.s[this.index++]);
        }

        return negative ? -num : num;
    }

    private skipWhitespace(): void {
        while (this.index < this.s.length && this.s[this.index] === ' ') {
            this.index++;
        }
    }
}
```

---

## Summary

These hard problems require:
1. **Multiple concepts** - Combining different techniques
2. **Careful implementation** - Many edge cases
3. **Optimization** - Both time and space matter
4. **Clean code** - Complexity demands clarity
5. **Testing** - Verify with multiple cases

---

## Practice Approach

1. **Understand deeply** - Read problem multiple times
2. **Plan thoroughly** - Design before coding
3. **Implement incrementally** - Test as you go
4. **Optimize later** - Working solution first
5. **Learn from solutions** - Study different approaches

Ready to solve these challenging problems? Head to PROBLEMS.md!