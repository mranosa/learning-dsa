# Union-Find Problems

## Problem Set Overview

10 carefully selected Union-Find problems, progressing from basic connectivity to advanced applications.

**Estimated total time:** 3-4 hours

---

## 1. Number of Provinces (Medium)

**LeetCode:** [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

### Problem Statement

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

### Example

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: Cities 0 and 1 are connected, so they are in one province.
City 2 is in another province.
```

### Constraints
- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

### Topics
- Union-Find
- Graph Connectivity
- Connected Components

---

## 2. Graph Valid Tree (Medium)

**LeetCode:** [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) (Premium)

### Problem Statement

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

A valid tree must:
1. Be connected (all nodes reachable from any node)
2. Have no cycles
3. Have exactly n-1 edges

### Example

```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Explanation: Forms a valid tree with root at node 0
```

### Constraints
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- No duplicate edges

### Topics
- Union-Find
- Cycle Detection
- Tree Properties

---

## 3. Number of Connected Components in an Undirected Graph (Medium)

**LeetCode:** [323. Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Premium)

### Problem Statement

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return the number of connected components in the graph.

### Example

```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation:
Component 1: nodes 0, 1, 2
Component 2: nodes 3, 4
```

### Constraints
- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai <= bi < n`
- `ai != bi`
- No duplicate edges

### Topics
- Union-Find
- Component Counting
- Graph Connectivity

---

## 4. Redundant Connection (Medium)

**LeetCode:** [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

### Problem Statement

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two different vertices chosen from `1` to `n`, and was not an edge that already existed.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

### Example

```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: The edge [2,3] creates a cycle when added
```

### Constraints
- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai < bi <= n`
- `ai != bi`
- No duplicate edges

### Topics
- Union-Find
- Cycle Detection
- Edge Removal

---

## 5. Accounts Merge (Medium)

**LeetCode:** [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

### Problem Statement

Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.

### Example

```
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                   ["John","johnsmith@mail.com","john00@mail.com"],
                   ["Mary","mary@mail.com"],
                   ["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
         ["Mary","mary@mail.com"],
         ["John","johnnybravo@mail.com"]]
```

### Constraints
- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`
- `accounts[i][0]` consists of English letters
- `accounts[i][j]` is a valid email

### Topics
- Union-Find
- Graph Components
- Email Grouping

---

## 6. Most Stones Removed with Same Row or Column (Medium)

**LeetCode:** [947. Most Stones Removed](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

### Problem Statement

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array `stones` of length `n` where `stones[i] = [xi, yi]` represents the location of the `ith` stone, return the largest possible number of stones that can be removed.

### Example

```
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is:
1. Remove stone [2,2] (shares row with [2,1] and column with [0,2],[1,2])
2. Remove stone [2,1] (shares row with remaining [2,*])
3. Remove stone [1,2] (shares row with [1,0])
4. Remove stone [1,0] (shares column with [0,0])
5. Remove stone [0,1] (shares row with [0,0])
The stone [0,0] cannot be removed.
```

### Constraints
- `1 <= stones.length <= 1000`
- `0 <= xi, yi <= 10^4`
- No two stones are at the same coordinate point

### Topics
- Union-Find
- Component Optimization
- Graph Connectivity

---

## 7. Number of Operations to Make Network Connected (Medium)

**LeetCode:** [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

### Problem Statement

There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables `connections` forming a network where `connections[i] = [ai, bi]` represents a connection between computers `ai` and `bi`. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return `-1`.

### Example

```
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between 1 and 2 and place between 1 and 3.
```

### Constraints
- `1 <= n <= 10^5`
- `1 <= connections.length <= min(n * (n - 1) / 2, 10^5)`
- `connections[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- No duplicate connections

### Topics
- Union-Find
- Component Counting
- Cable Redistribution

---

## 8. Satisfiability of Equality Equations (Medium)

**LeetCode:** [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

### Problem Statement

You are given an array of strings `equations` that represent relationships between variables where each string `equations[i]` has length 4 and takes one of two different forms: `"xi==yi"` or `"xi!=yi"`. Here, `xi` and `yi` are lowercase letters (not necessarily different) representing variable names.

Return `true` if it is possible to assign integers to variable names so as to satisfy all the given equations, or `false` otherwise.

### Example

```
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If a equals b, then b cannot not equal a.
```

### Constraints
- `1 <= equations.length <= 500`
- `equations[i].length == 4`
- `equations[i][0]` is a lowercase letter
- `equations[i][1]` is either `'='` or `'!'`
- `equations[i][2]` is `'='`
- `equations[i][3]` is a lowercase letter

### Topics
- Union-Find
- Equation Grouping
- Contradiction Detection

---

## 9. Smallest String With Swaps (Medium)

**LeetCode:** [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)

### Problem Statement

You are given a string `s`, and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates 2 indices (0-indexed) of the string.

You can swap the characters at any pair of indices in the given `pairs` any number of times.

Return the lexicographically smallest string that `s` can be transformed to after using the swaps.

### Example

```
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explanation:
- Swap s[0] and s[3], s = "bcad"
- Swap s[1] and s[2], s = "bacd"
```

### Constraints
- `1 <= s.length <= 10^5`
- `0 <= pairs.length <= 10^5`
- `0 <= pairs[i][0], pairs[i][1] < s.length`
- `s` only contains lowercase English letters

### Topics
- Union-Find
- Component Optimization
- String Manipulation

---

## 10. Evaluate Division (Medium)

**LeetCode:** [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)

### Problem Statement

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents the `jth` query where you must find the answer for `Cj / Dj = ?`.

Return the answers to all queries. If a single query cannot be determined, return `-1.0`.

### Example

```
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
       queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0]
```

### Constraints
- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= Ai.length, Bi.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`

### Topics
- Weighted Union-Find
- Graph Traversal
- Division Chains

---

## Problem-Solving Strategy

### Approach Order
1. **Start with problems 1-3** - Basic Union-Find implementation
2. **Move to problems 4-5** - Cycle detection and grouping
3. **Try problems 6-7** - Component optimization
4. **Tackle problems 8-9** - Special applications
5. **Finish with problem 10** - Weighted Union-Find

### Time Management
- Problems 1-3: 15-20 minutes each
- Problems 4-7: 20-25 minutes each
- Problems 8-9: 25-30 minutes each
- Problem 10: 30-35 minutes

### Key Patterns to Remember
1. **Component counting** - Track number of unions
2. **Cycle detection** - Check if nodes already connected
3. **Group merging** - Unite elements sharing properties
4. **Optimization** - Minimize/maximize components
5. **Weighted edges** - Modified find with path weights