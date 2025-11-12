# Problems - Session 11: Graph BFS

10 problems in order. Use UMPIRE method.

**Targets:** Medium <30 min | Hard <45 min

---

## Problem 1: Rotting Oranges

**Difficulty:** Medium | **Pattern:** Multi-source BFS
**LeetCode:** https://leetcode.com/problems/rotting-oranges/

### Problem

Given m x n grid where each cell has one of three values:
- 0 = empty cell
- 1 = fresh orange
- 2 = rotten orange

Every minute, any fresh orange 4-directionally adjacent to rotten orange becomes rotten.

Return minimum minutes until no cell has fresh orange. If impossible, return -1.

### Examples

```
grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: Bottom left corner orange never rots
```

### Constraints

- m == grid.length
- n == grid[i].length
- 1 ≤ m, n ≤ 10
- grid[i][j] is 0, 1, or 2

### Hints
- Multi-source BFS from all rotten oranges
- Process level by level (each level = 1 minute)
- Track fresh orange count
- O(m × n) time, O(m × n) space

---

## Problem 2: Course Schedule

**Difficulty:** Medium | **Pattern:** Cycle Detection
**LeetCode:** https://leetcode.com/problems/course-schedule/

### Problem

numCourses courses labeled 0 to numCourses - 1. Array prerequisites where prerequisites[i] = [ai, bi] means must take course bi before ai.

Return true if can finish all courses. Otherwise, false.

### Examples

```
numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: Take course 0, then course 1

numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: Cannot take 0 before 1 and 1 before 0
```

### Constraints

- 1 ≤ numCourses ≤ 2000
- 0 ≤ prerequisites.length ≤ 5000
- prerequisites[i].length == 2
- 0 ≤ ai, bi < numCourses
- All pairs [ai, bi] are unique

### Hints
- Detect cycle in directed graph
- Use topological sort (Kahn's algorithm)
- Track in-degrees
- If can process all nodes, no cycle exists
- O(V + E) time, O(V + E) space

---

## Problem 3: Course Schedule II

**Difficulty:** Medium | **Pattern:** Topological Sort
**LeetCode:** https://leetcode.com/problems/course-schedule-ii/

### Problem

Return ordering of courses to finish all courses. If many valid answers, return any. If impossible, return empty array.

### Examples

```
numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]

numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]

numCourses = 1, prerequisites = []
Output: [0]
```

### Constraints

- 1 ≤ numCourses ≤ 2000
- 0 ≤ prerequisites.length ≤ numCourses × (numCourses - 1)
- prerequisites[i].length == 2
- 0 ≤ ai, bi < numCourses
- ai ≠ bi
- All pairs unique

### Hints
- Topological sort with Kahn's algorithm
- Track order as you process nodes
- Processing order is the answer
- Return empty if cycle detected
- O(V + E) time, O(V + E) space

---

## Problem 4: Shortest Path in Binary Matrix

**Difficulty:** Medium | **Pattern:** 8-directional BFS
**LeetCode:** https://leetcode.com/problems/shortest-path-in-binary-matrix/

### Problem

Given n x n binary matrix grid, return length of shortest clear path. If no clear path, return -1.

Clear path from (0, 0) to (n-1, n-1) requires:
- All visited cells are 0
- All adjacent cells 8-directionally connected

Length = number of visited cells.

### Examples

```
grid = [[0,1],[1,0]]
Output: 2

grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

### Constraints

- n == grid.length
- n == grid[i].length
- 1 ≤ n ≤ 100
- grid[i][j] is 0 or 1

### Hints
- 8-directional BFS (includes diagonals)
- Check if start/end blocked first
- Track distance with each cell
- Return distance when reach target
- O(n²) time, O(n²) space

---

## Problem 5: Walls and Gates

**Difficulty:** Medium | **Pattern:** Multi-source BFS
**LeetCode:** https://leetcode.com/problems/walls-and-gates/ **(Premium)**

### Problem

Given m x n grid with three values:
- -1 = Wall or obstacle
- 0 = Gate
- INF = Empty room

Fill each empty room with distance to nearest gate. If impossible, leave INF.

### Examples

```
Input: rooms = [
  [INF, -1,  0,  INF],
  [INF, INF, INF, -1],
  [INF, -1,  INF, -1],
  [0,   -1,  INF, INF]
]

Output: [
  [3, -1, 0,  1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3,  4]
]
```

### Constraints

- m == rooms.length
- n == rooms[i].length
- 1 ≤ m, n ≤ 250
- rooms[i][j] is -1, 0, or 2³¹ - 1

### Hints
- Multi-source BFS from all gates
- Start from gates, spread outward
- First time reaching room = shortest distance
- Update rooms in-place
- O(m × n) time, O(m × n) space

---

## Problem 6: Word Ladder

**Difficulty:** Hard | **Pattern:** Transformation Graph
**LeetCode:** https://leetcode.com/problems/word-ladder/

### Problem

Transformation sequence from beginWord to endWord using wordList:
- Every adjacent pair differs by single letter
- Every si is in wordList
- sk == endWord

Return number of words in shortest transformation. Return 0 if no sequence exists.

### Examples

```
beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: endWord not in wordList
```

### Constraints

- 1 ≤ beginWord.length ≤ 10
- endWord.length == beginWord.length
- 1 ≤ wordList.length ≤ 5000
- wordList[i].length == beginWord.length
- Only lowercase English letters
- beginWord ≠ endWord
- All wordList strings unique

### Hints
- Build graph where words are nodes
- Use pattern matching ("h*t", "hi*") for neighbors
- BFS from beginWord to endWord
- Track transformation count (levels)
- O(M² × N) time where M = word length, N = word count

---

## Problem 7: 01 Matrix

**Difficulty:** Medium | **Pattern:** Distance BFS
**LeetCode:** https://leetcode.com/problems/01-matrix/

### Problem

Given m x n binary matrix mat, return distance of nearest 0 for each cell.

Distance between two adjacent cells is 1.

### Examples

```
mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

### Constraints

- m == mat.length
- n == mat[i].length
- 1 ≤ m, n ≤ 10⁴
- 1 ≤ m × n ≤ 10⁴
- mat[i][j] is 0 or 1
- At least one 0 exists

### Hints
- Multi-source BFS from all 0s
- Similar to Walls and Gates
- Each level increases distance by 1
- Mark visited to avoid reprocessing
- O(m × n) time, O(m × n) space

---

## Problem 8: Open the Lock

**Difficulty:** Medium | **Pattern:** State Space BFS
**LeetCode:** https://leetcode.com/problems/open-the-lock/

### Problem

Lock with 4 circular wheels. Each wheel has 10 slots: '0' to '9'. Wheels rotate freely and wrap.

Lock starts at '0000'. Given list of deadends. Given target, return minimum turns to unlock, or -1 if impossible.

### Examples

```
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
Output: 6
Explanation: "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"

deadends = ["8888"], target = "0009"
Output: 1
Explanation: "0000" -> "0009"

deadends = ["0000"], target = "8888"
Output: -1
```

### Constraints

- 1 ≤ deadends.length ≤ 500
- deadends[i].length == 4
- target.length == 4
- target not in deadends
- All strings consist of digits only

### Hints
- Each state is a node in graph
- 8 neighbors per state (4 wheels × 2 directions)
- BFS from "0000" to target
- Skip deadends and visited states
- O(10⁴) time and space (all possible states)

---

## Problem 9: Minimum Knight Moves

**Difficulty:** Medium | **Pattern:** Chess BFS
**LeetCode:** https://leetcode.com/problems/minimum-knight-moves/ **(Premium)**

### Problem

Infinite chessboard from -∞ to +∞. Knight at [0, 0].

Knight has 8 possible moves. Return minimum steps to move knight to [x, y]. Answer guaranteed to exist.

### Examples

```
x = 2, y = 1
Output: 1
Explanation: [0, 0] -> [2, 1]

x = 5, y = 5
Output: 4
Explanation: [0, 0] -> [2, 1] -> [4, 2] -> [3, 4] -> [5, 5]
```

### Constraints

- -300 ≤ x, y ≤ 300
- 0 ≤ |x| + |y| ≤ 300

### Hints
- BFS with 8 knight moves
- Use symmetry: abs(x), abs(y)
- Prune positions going too far negative
- Track visited to avoid cycles
- O(|x| × |y|) time and space

---

## Problem 10: Shortest Bridge

**Difficulty:** Medium | **Pattern:** BFS + DFS
**LeetCode:** https://leetcode.com/problems/shortest-bridge/

### Problem

Given n x n binary matrix where 1 = land, 0 = water.

Island = 4-directionally connected group of 1s. Exactly two islands exist.

May change 0s to 1s to connect islands. Return smallest number of 0s to flip.

### Examples

```
grid = [[0,1],[1,0]]
Output: 1

grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

### Constraints

- n == grid.length
- n == grid[i].length
- 2 ≤ n ≤ 100
- grid[i][j] is 0 or 1
- Exactly two islands

### Hints
- DFS to find first island
- BFS from first island to find second
- Mark first island cells (change to 2)
- BFS tracks distance (flips needed)
- O(n²) time, O(n²) space

---

## Summary

**Total:** 10 problems (7 Medium, 1 Hard, 2 Premium)

**Patterns:**
- Multi-source BFS
- Topological Sort
- Matrix BFS
- State Space BFS
- Bidirectional BFS

**Time Guidelines:**
- Medium: 20-30 minutes
- Hard: 30-45 minutes

Focus on patterns, not just solutions!

---

**Ready?** Say: `"Claude, give me the problem"` or `"Go"`

[Solutions](./SOLUTIONS.md) | [Hints](./HINTS.md)
