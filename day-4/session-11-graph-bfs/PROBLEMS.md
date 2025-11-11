# Problems: Graph BFS

## Problem 1: Rotting Oranges
**Difficulty:** Medium
**LeetCode:** [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
**NeetCode:** https://www.youtube.com/watch?v=y704fEOx0s0

You are given an `m x n` grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

**Example 1:**
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**
```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**
```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

---

## Problem 2: Course Schedule
**Difficulty:** Medium
**LeetCode:** [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
**NeetCode:** https://www.youtube.com/watch?v=EgI5nU9etnU

There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Example 1:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

---

## Problem 3: Course Schedule II
**Difficulty:** Medium
**LeetCode:** [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
**NeetCode:** https://www.youtube.com/watch?v=Akt3glAwyfY

There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

**Example 1:**
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

**Example 2:**
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

---

## Problem 4: Shortest Path in Binary Matrix
**Difficulty:** Medium
**LeetCode:** [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
**NeetCode:** https://www.youtube.com/watch?v=YnxUdAO7TAo

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected.

The length of a clear path is the number of visited cells of this path.

**Example 1:**
```
Input: grid = [[0,1],[1,0]]
Output: 2
```

**Example 2:**
```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

**Example 3:**
```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

---

## Problem 5: Walls and Gates (Premium)
**Difficulty:** Medium
**LeetCode:** [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) (Premium)
**NeetCode:** https://www.youtube.com/watch?v=e69C6xhiSQE

You are given an m x n grid initialized with these three possible values:
- -1 - A wall or an obstacle.
- 0 - A gate.
- INF - Infinity means an empty room.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

**Example:**
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

---

## Problem 6: Word Ladder
**Difficulty:** Hard
**LeetCode:** [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
**NeetCode:** https://www.youtube.com/watch?v=h9iTnkgv05E

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- sk == endWord

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or 0 if no such sequence exists.

**Example 1:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
```

**Example 2:**
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

---

## Problem 7: 01 Matrix
**Difficulty:** Medium
**LeetCode:** [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)
**NeetCode:** https://www.youtube.com/watch?v=fqVT0QgvOQ

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

**Example 1:**
```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

**Example 2:**
```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

---

## Problem 8: Open the Lock
**Difficulty:** Medium
**LeetCode:** [752. Open the Lock](https://leetcode.com/problems/open-the-lock/)
**NeetCode:** https://www.youtube.com/watch?v=Pzg3bCDY87w

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around. Each move consists of turning one wheel one slot.

The lock initially starts at '0000'. You are given a list of `deadends`, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

**Example 1:**
```
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
```

**Example 2:**
```
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
```

---

## Problem 9: Minimum Knight Moves (Premium)
**Difficulty:** Medium
**LeetCode:** [1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/) (Premium)
**NeetCode:** Not available (Premium problem)

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

**Example 1:**
```
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
```

**Example 2:**
```
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
```

---

## Problem 10: Shortest Bridge
**Difficulty:** Medium
**LeetCode:** [934. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/)
**NeetCode:** https://www.youtube.com/watch?v=gkINMhbbIbU

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

**Example 1:**
```
Input: grid = [[0,1],[1,0]]
Output: 1
```

**Example 2:**
```
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

**Example 3:**
```
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

---

## Problem Solving Order

**Recommended sequence:**
1. Start with **Rotting Oranges** (classic multi-source BFS)
2. Then **01 Matrix** (similar pattern)
3. Move to **Course Schedule** (cycle detection)
4. Then **Course Schedule II** (topological sort)
5. Try **Shortest Path in Binary Matrix** (8-directional BFS)
6. Tackle **Open the Lock** (state space BFS)
7. Challenge yourself with **Word Ladder** (harder transformation)
8. Finish with **Shortest Bridge** (BFS + DFS combo)

**Time Guidelines:**
- Easy: 15-20 minutes
- Medium: 20-30 minutes
- Hard: 30-45 minutes

Remember: Focus on understanding the pattern, not just solving the problem!