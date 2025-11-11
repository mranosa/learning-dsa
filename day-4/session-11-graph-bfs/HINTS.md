# Hints: Graph BFS

## Problem 1: Rotting Oranges

### Hint 1 (Gentle nudge)
This is a classic "spreading" problem. Think about how rot spreads from multiple sources simultaneously each minute.

### Hint 2 (Directed guidance)
Use multi-source BFS. Start with all initially rotten oranges in the queue. Process level by level to track minutes.

### Hint 3 (Detailed approach)
1. Find all rotten oranges and add to queue
2. Count fresh oranges
3. BFS level by level (each level = 1 minute)
4. For each rotten orange, rot adjacent fresh ones
5. Return minutes if all fresh are rotten, else -1

---

## Problem 2: Course Schedule

### Hint 1 (Gentle nudge)
This is about detecting cycles in a directed graph. If there's a cycle in prerequisites, you can't complete all courses.

### Hint 2 (Directed guidance)
Use topological sort with Kahn's algorithm. Track in-degrees and process nodes with 0 in-degree.

### Hint 3 (Detailed approach)
1. Build adjacency list from prerequisites
2. Calculate in-degree for each course
3. Queue all courses with 0 in-degree
4. Process queue: remove course, reduce in-degrees of dependents
5. If processed all courses, no cycle exists

---

## Problem 3: Course Schedule II

### Hint 1 (Gentle nudge)
Similar to Course Schedule I, but now you need to return the actual ordering.

### Hint 2 (Directed guidance)
Use Kahn's algorithm but track the order of courses as you process them. The processing order is your answer.

### Hint 3 (Detailed approach)
1. Build graph and calculate in-degrees
2. Queue courses with 0 in-degree
3. Process queue and add each course to result array
4. For each dependent, reduce in-degree and add to queue if it becomes 0
5. Return result if length equals numCourses, else return empty array

---

## Problem 4: Shortest Path in Binary Matrix

### Hint 1 (Gentle nudge)
BFS naturally finds shortest paths. This problem allows 8-directional movement.

### Hint 2 (Directed guidance)
Start BFS from (0,0) and try to reach (n-1, n-1). Track distance as you explore.

### Hint 3 (Detailed approach)
1. Check if start or end is blocked
2. Use BFS with 8 directions (including diagonals)
3. Track visited cells and current distance
4. When you reach target, return distance
5. If queue empties without reaching target, return -1

---

## Problem 5: Walls and Gates

### Hint 1 (Gentle nudge)
Instead of BFS from each empty room to find nearest gate, reverse the problem.

### Hint 2 (Directed guidance)
Start BFS from all gates simultaneously. The first time you reach an empty room is the shortest distance.

### Hint 3 (Detailed approach)
1. Find all gates (value 0) and add to queue
2. BFS from all gates simultaneously
3. For each neighbor that's an empty room (INF), update its distance
4. Continue until all reachable rooms are updated
5. Rooms remain INF if unreachable

---

## Problem 6: Word Ladder

### Hint 1 (Gentle nudge)
Think of this as a graph where words are nodes and edges exist between words differing by one letter.

### Hint 2 (Directed guidance)
Use BFS to find shortest transformation path. Consider using patterns like "h*t" to find neighbors efficiently.

### Hint 3 (Detailed approach)
1. Create pattern map: "hit" → ["*it", "h*t", "hi*"]
2. Group words by patterns for O(1) neighbor lookup
3. BFS from beginWord tracking level (transformation count)
4. For each word, check all patterns and their word lists
5. Return level when endWord is found

---

## Problem 7: 01 Matrix

### Hint 1 (Gentle nudge)
Similar to Walls and Gates - start from all 0s and spread outward.

### Hint 2 (Directed guidance)
Multi-source BFS from all cells containing 0. Each level of BFS increases distance by 1.

### Hint 3 (Detailed approach)
1. Find all cells with 0 and add to queue
2. Mark these cells as distance 0
3. BFS to unvisited neighbors
4. Each neighbor gets distance = current + 1
5. Continue until all cells are processed

---

## Problem 8: Open the Lock

### Hint 1 (Gentle nudge)
Each lock state is a node in a graph. Moving one wheel creates an edge to a new state.

### Hint 2 (Directed guidance)
BFS from "0000" trying to reach target. Each state has 8 neighbors (4 wheels × 2 directions).

### Hint 3 (Detailed approach)
1. Start BFS from "0000"
2. For each state, generate 8 possible next states
3. Skip deadends and visited states
4. Track number of turns (BFS levels)
5. Return turns when target is reached

---

## Problem 9: Minimum Knight Moves

### Hint 1 (Gentle nudge)
Knight moves form a graph. BFS finds the minimum number of moves.

### Hint 2 (Directed guidance)
Use symmetry to optimize - abs(x) and abs(y) reduce the search space. Be careful with boundary conditions.

### Hint 3 (Detailed approach)
1. Use absolute values of x and y (symmetry)
2. BFS with 8 possible knight moves
3. Track visited positions to avoid cycles
4. Prune positions that go too far negative
5. Return steps when target is reached

---

## Problem 10: Shortest Bridge

### Hint 1 (Gentle nudge)
Find one island first, then find the shortest path to the other island.

### Hint 2 (Directed guidance)
Use DFS to identify and mark the first island, then BFS from all cells of that island to find the second.

### Hint 3 (Detailed approach)
1. DFS to find and mark first island (change 1s to 2s)
2. Add all first island cells to BFS queue
3. BFS outward tracking distance
4. When you hit a cell with value 1 (second island), return distance
5. The distance is the number of 0s you need to flip

---

## General BFS Tips

### Pattern Recognition
- **Multi-source BFS**: Multiple starting points (Rotting Oranges, Walls and Gates)
- **Shortest path**: Unweighted graphs (Word Ladder, Knight Moves)
- **Level tracking**: Need distance/steps (01 Matrix, Open Lock)
- **State space**: Each state is a node (Open Lock, Word Ladder)

### Common Optimizations
1. **Bidirectional BFS**: Search from both ends (Word Ladder)
2. **Early termination**: Stop when target found
3. **Pruning**: Skip invalid/suboptimal states
4. **Pattern matching**: Group similar states

### Edge Cases to Consider
- Empty input
- Single element
- Start equals target
- Unreachable target
- Cycles in graph
- Disconnected components