# Interviewer Script: Graph BFS

## Opening (2 minutes)

**Claude says:**
"Welcome to Session 11 on Graph BFS and Topological Sort! Today we'll master breadth-first traversal patterns that are essential for level-order problems and shortest path algorithms.

Before we dive in, let me check your understanding of graph basics:
1. Can you explain when BFS is preferred over DFS?
2. What data structure does BFS use and why?
3. How does BFS guarantee shortest paths in unweighted graphs?

Take your time to think through these."

**Expected answers:**
- BFS for shortest paths, level-order; DFS for all paths, backtracking
- Queue (FIFO) ensures level-by-level processing
- BFS explores all nodes at distance k before k+1

---

## Concept Check (3 minutes)

**Claude asks these questions:**

### Question 1: "What's the key difference between tree BFS and graph BFS?"

**Looking for:**
- Graphs can have cycles (need visited tracking)
- Multiple paths to same node
- May have disconnected components

**If struggling, Claude hints:**
"Think about what could go wrong if we don't track visited nodes in a graph..."

### Question 2: "Explain multi-source BFS. When would you use it?"

**Looking for:**
- Start from multiple nodes simultaneously
- Useful for spreading/distance problems
- More efficient than multiple single-source BFS

### Question 3: "What is topological sort and when is it possible?"

**Looking for:**
- Linear ordering respecting dependencies
- Only possible in DAGs (Directed Acyclic Graphs)
- Cycle makes it impossible

---

## Problem Selection (1 minute)

**Claude says:**
"I've selected 10 problems that cover essential BFS patterns:
- Multi-source BFS (Rotting Oranges, Walls and Gates)
- Topological sorting (Course Schedule I & II)
- Shortest path variants (Binary Matrix, Word Ladder)
- State space exploration (Open Lock, Knight Moves)

Which problem would you like to start with? I recommend Rotting Oranges for a classic multi-source BFS pattern."

---

## Problem Walkthrough: Rotting Oranges (15 minutes)

### Understanding Phase (3 minutes)

**Claude begins:**
"Let's work through the Rotting Oranges problem. Please read it and tell me:
1. What are we trying to find?
2. What are the constraints?
3. Can you identify the graph structure here?"

**Claude listens for:**
- Minimum time for all oranges to rot
- 4-directional spread
- Grid as implicit graph

### Approach Discussion (4 minutes)

**Claude asks:**
"How would you approach this problem? Think about:
- Where does the rotting start?
- How does it spread?
- How do we track time?"

**If student suggests DFS:**
"DFS could work, but how would you track the minutes? Remember, all rotten oranges spread simultaneously each minute."

**Guide towards:**
"Multi-source BFS - start with all rotten oranges in queue, process level by level where each level represents one minute."

### Implementation Phase (6 minutes)

**Claude prompts:**
"Let's implement this step by step:
1. First, scan the grid - what are we looking for?
2. How do we set up our BFS?
3. How do we track minutes?"

**Watch for common mistakes:**
- Not counting fresh oranges initially
- Processing entire queue vs level-by-level
- Not checking if fresh oranges remain

**If stuck, Claude hints:**
```typescript
// Structure hint
const queue: [row, col][] = [];
let freshCount = 0;
// Scan grid first...
// Then BFS with level processing
```

### Complexity Analysis (2 minutes)

**Claude asks:**
"What's the time and space complexity?"

**Looking for:**
- Time: O(m × n) - visit each cell once
- Space: O(m × n) - worst case all in queue

---

## Problem Walkthrough: Course Schedule (15 minutes)

### Understanding Phase (3 minutes)

**Claude begins:**
"Now let's tackle Course Schedule - a classic cycle detection problem.
- What does a cycle in prerequisites mean?
- How can we detect it?"

**Listen for understanding of:**
- Circular dependencies
- Impossibility of completion
- Directed graph representation

### Approach Discussion (4 minutes)

**Claude guides:**
"There are two main approaches:
1. Topological sort (Kahn's algorithm)
2. DFS with cycle detection

Which would you prefer and why?"

**For Kahn's algorithm:**
"Excellent! Walk me through:
- What is in-degree?
- How does Kahn's algorithm detect cycles?
- What's our success condition?"

### Implementation Phase (6 minutes)

**Key implementation points:**
```typescript
// Build graph and in-degree
// Queue nodes with 0 in-degree
// Process and track count
// Check if all processed
```

**Common issues Claude watches for:**
- Building adjacency list incorrectly
- Not tracking processed count
- Confusion about prerequisite direction

### Follow-up Question (2 minutes)

**Claude asks:**
"How would you modify this to return the actual course order?"

**Looking for:** Understanding that the processing order in Kahn's algorithm IS the topological order.

---

## Advanced Problem: Word Ladder (18 minutes)

### Problem Analysis (5 minutes)

**Claude says:**
"Word Ladder is more complex. Let's break it down:
- What's the graph here?
- What are the edges?
- Why is this challenging?"

**Guide towards:**
- Words as nodes
- Edges between words differing by one letter
- Challenge: efficiently finding neighbors

### Optimization Discussion (5 minutes)

**Claude asks:**
"Checking every word against every other word is O(N²M). Can we do better?"

**Introduce pattern concept:**
```typescript
"hit" → ["*it", "h*t", "hi*"]
```

**Discuss bidirectional BFS:**
"For even better performance, we could search from both ends. Why does this help?"

### Implementation Focus (8 minutes)

**Critical points:**
- Pattern map construction
- BFS with level tracking
- Efficient neighbor finding

---

## Pattern Recognition (5 minutes)

**Claude summarizes:**
"Let's identify the patterns we've seen:

1. **Multi-source BFS**: When did we use this?
   - Rotting Oranges, Walls and Gates
   - Key: Multiple starting points spreading simultaneously

2. **Topological Sort**: What problems use this?
   - Course Schedule, task dependencies
   - Key: Linear ordering respecting constraints

3. **Shortest Path**: Which problems?
   - Binary Matrix, Word Ladder
   - Key: BFS guarantees minimum in unweighted graphs

4. **State Space**: What makes these unique?
   - Open Lock, each state is a node
   - Key: Abstract graph, not explicit

Which pattern did you find most challenging?"

---

## Debugging Session (8 minutes)

**Claude presents buggy code:**

```typescript
// Buggy BFS implementation
function bfs(graph: Map<number, number[]>, start: number) {
    const queue = [start];
    const visited = new Set();

    while (queue.length > 0) {
        const node = queue.shift();
        visited.add(node);  // Bug: Too late!

        for (const neighbor of graph.get(node)) {
            if (!visited.has(neighbor)) {
                queue.push(neighbor);
            }
        }
    }
}
```

**Claude asks:**
"This BFS has a critical bug. Can you spot it?"

**Answer:** Marking visited after dequeue instead of before enqueue causes duplicates in queue.

---

## Complexity Deep Dive (5 minutes)

**Claude discusses:**
"Let's analyze different BFS patterns:

1. Basic BFS: O(V + E) time, O(V) space
2. Matrix BFS: O(m × n) time and space
3. Bidirectional BFS: O(b^(d/2)) vs O(b^d)

When would space complexity be a concern?"

**Discuss:**
- Dense graphs
- Large state spaces
- Memory constraints

---

## Tips and Tricks (3 minutes)

**Claude shares:**
"Key BFS insights for interviews:

1. **Always mark visited before enqueueing** - prevents duplicates
2. **Process level-by-level for distance** - use queue size
3. **Multi-source for spreading problems** - more efficient
4. **Consider bidirectional for single target** - reduces search space
5. **Check early termination opportunities** - stop when found

What's your biggest takeaway from today?"

---

## Closing (2 minutes)

**Claude concludes:**
"Excellent work today! You've mastered:
- Multi-source BFS patterns
- Topological sorting with Kahn's algorithm
- Shortest path in unweighted graphs
- State space exploration

For extra practice, try:
1. Implementing bidirectional BFS for Word Ladder
2. Solving 'Alien Dictionary' (topological sort variant)
3. 'Minimum Height Trees' (BFS from leaves)

Tomorrow we'll explore DFS patterns including backtracking and connected components.

Your performance score: [Claude provides score based on understanding, implementation, and problem-solving]

Any questions before we wrap up?"

---

## Scoring Rubric

**Claude evaluates on:**

1. **Concept Understanding (25%)**
   - BFS vs DFS tradeoffs
   - Queue-based traversal
   - Shortest path properties

2. **Problem Analysis (25%)**
   - Graph identification
   - Pattern recognition
   - Edge case consideration

3. **Implementation (25%)**
   - Correct BFS structure
   - Proper visited tracking
   - Level/distance handling

4. **Optimization (15%)**
   - Multi-source recognition
   - Bidirectional BFS understanding
   - Time/space analysis

5. **Communication (10%)**
   - Clear explanation
   - Structured thinking
   - Question asking

**Score interpretation:**
- 90-100: Ready for advanced graph problems
- 75-89: Solid understanding, practice optimization
- 60-74: Good foundation, review patterns
- Below 60: Review basics, practice more problems