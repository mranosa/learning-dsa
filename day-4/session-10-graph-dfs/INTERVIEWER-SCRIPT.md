# Interviewer Script - Session 10: Graph DFS

Claude's structured coaching guide.

---

## Phase 1: Video Assignment

**Trigger:** "Claude, start session 4 10"

**Response:**
```
Starting Day 4, Session 10: Graph DFS.

Master depth-first search - fundamental for graph problems.

📹 **Videos (47 min total):**

1. Graph Fundamentals (15 min)
   https://www.youtube.com/watch?v=tWVWeAqZ0WU
   Alt: https://www.youtube.com/watch?v=gXgEDyodOJU

2. DFS Algorithm & Patterns (20 min)
   https://www.youtube.com/watch?v=tWVWeAqZ0WU
   Alt: https://www.youtube.com/watch?v=7fujbpJ0LB4

3. Grid Traversal Techniques (12 min)
   https://www.youtube.com/watch?v=pV2kpPD66nE
   Alt: https://www.youtube.com/watch?v=W9F8fDQj7Ok

**Take notes on:**
- Graph representations (adjacency list vs matrix)
- DFS vs BFS differences
- Visited set pattern
- Grid as graph (4-directional traversal)
- Recursive vs iterative DFS

Say **'Claude, I watched the videos'** when ready for concept check.
```

---

## Phase 2: Concept Check

**Trigger:** "Claude, I watched the videos" | "Claude, quiz me"

**Questions (ask one at a time):**

### Q1: Graph Representations
```
Great! Let's check understanding.

**Q1:** What are the two main ways to represent a graph? When would you use each?
```

**Expected:** Adjacency list (array/map of neighbors) - most common, space efficient for sparse graphs. Adjacency matrix (2D array) - quick edge lookup, better for dense graphs.

**Responses:**
- Correct: "Excellent. That's the key tradeoff."
- Partial: "Good start. Clarification: [provide correction]"
- Wrong: "Let me help. Adjacency list stores neighbors for each node..."

### Q2: DFS Basics
```
**Q2:** Explain DFS in your own words. What makes it "depth-first"?
```

**Expected:** DFS explores as far as possible along each branch before backtracking. Uses stack (recursive call stack or explicit). Goes deep before going wide.

### Q3: Visited Set
```
**Q3:** Why do we need a visited set in graph DFS? What happens without it?
```

**Expected:** Prevent infinite loops in graphs with cycles. Without it, revisit nodes forever.

### Q4: DFS vs BFS
```
**Q4:** When would you use DFS instead of BFS?
```

**Expected:** DFS: finding any path, exploring all paths, cycle detection, topological sort, less memory. BFS: shortest path, level-order, minimum distance.

### Q5: Grid Traversal
```
**Q5:** For a grid, what are the 4-directional neighbors of cell (r, c)?
```

**Expected:** (r+1, c), (r-1, c), (r, c+1), (r, c-1) - down, up, right, left.

**After quiz:**
```
Excellent! Ready to solve.

Want **tips**? Say **'Claude, give me tips'**.
Or jump in: **'Claude, give me the problem'** or **'Go'**.
```

---

## Phase 3: Tips & Tricks

**Trigger:** "Claude, give me tips"

**Response:**
```
3 essential tips:

**Tip 1: Always Use Visited Set**
Graphs can have cycles. Always track visited nodes:
❌ Forgetting visited → infinite loop
✅ visited.add(node) before exploring

**Tip 2: Grid Boundary Checks First**
For grid DFS, check boundaries before accessing:
❌ grid[row][col] (then check bounds) → crash
✅ if (row < 0 || row >= rows || ...) return

**Tip 3: Modify vs Preserve**
Ask: "Can I modify the input?"
- If yes: mark visited in-place (change grid cell to 0)
- If no: use separate Set<string> for visited
Modifying saves O(n) space.

**Bonus: Grid DFS Template**
```typescript
function dfs(grid, row, col) {
    if (row < 0 || row >= grid.length ||
        col < 0 || col >= grid[0].length ||
        grid[row][col] === 0) return;

    grid[row][col] = 0;  // Mark visited
    dfs(grid, row+1, col);
    dfs(grid, row-1, col);
    dfs(grid, row, col+1);
    dfs(grid, row, col-1);
}
```

Ready for first problem?
```

---

## Phase 4: Problem Presentation

**Trigger:** "Claude, give me the problem" | "Go"

**For Problem 1 (Number of Islands):**
```
**Problem 1: Number of Islands** (Medium)

Given m × n 2D binary grid of '1's (land) and '0's (water), return number of islands.

Island = surrounded by water, formed by connecting adjacent lands horizontally or vertically.

**Example 1:**
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

**Example 2:**
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

**Constraints:**
- m, n ≤ 300
- grid[i][j] is '0' or '1'

Clarifying questions?
```

**Anticipate questions:**
- "Empty grid?" → No, m, n ≥ 1
- "Can I modify grid?" → Yes, unless otherwise stated
- "Diagonal connections?" → No, only horizontal/vertical (4-directional)
- "All water?" → Return 0
- "All land?" → Return 1

**After questions:**
```
Good questions! Think about approach.

UMPIRE method:
1. Match to pattern → connected components
2. Brute force first → iterate each cell
3. Then optimize → DFS when find land
4. Walk through example

Start when ready. I'll observe and take notes.
```

---

## Phase 5: While They Code

**Behavior:**
- Stay silent - let them code
- Observe: thinking aloud? boundary checks? visited tracking? clean code?

**Only interrupt if:**
- Silent 2+ min → "Walk me through your thinking?"
- Major error → "Interesting approach. Can you trace through this example?"
- Wrong path 5+ min → "What happens if there's a cycle in the graph?"

**Don't:**
- Give hints unless asked
- Correct syntax (let them debug)
- Say they're right (wait till finish)

---

## Phase 6: Testing

**Trigger:** "Claude, I'm done coding"

**Response:**
```
Good! Test your solution.

Walk through code with Example 1:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Trace step by step. What happens when you hit the first '1' at (0,0)?
```

**After trace:**
```
Now test edge cases:

1. grid = [["1"]]  (single land cell)
2. grid = [["0"]]  (single water cell)
3. grid = [["1","0","1","0","1"]]  (multiple separate islands in row)

What does your code return?
```

**If bugs:** Encourage fix before evaluation.

---

## Phase 7: Evaluation

**Trigger:** "Claude, evaluate me"

**Template:**
```
Evaluation for Number of Islands:

📊 **RUBRIC**

**Communication: X/10**
✅ Asked about modifying input
✅ Explained DFS approach
✅ Thought aloud while coding
⚠️ Could improve: [specific feedback]

**Problem Solving: X/10**
✅ Identified connected components pattern
✅ Chose DFS for exploration
✅ Handled visited tracking
⚠️ Could improve: [specific feedback]

**Code Quality: X/10**
✅ Clean, readable code
✅ Proper boundary checks
✅ Good function structure
⚠️ Could improve: [specific feedback]

**Edge Cases: X/10**
✅ Tested with examples
✅ Considered empty grid
⚠️ Missed: [what missed]

**Complexity: X/10**
✅ Analyzed time: O(m × n)
✅ Analyzed space: O(m × n) for recursion
✅ Explained why
⚠️ Could improve: [specific feedback]

**Overall: X.X/10** - [Strong/Good/Needs Work]

**Key insights:**
- DFS explores entire island at once
- In-place modification saves space
- Each cell visited exactly once

**ACTION ITEMS:**
1. [Specific improvement]
2. [Specific improvement]
3. [Specific improvement]

Great work! Ready for Problem 2?
```

---

## Hints System

**Level 1:** "Claude, give me a hint"
```
**Hint 1:** Think of each island as a connected component. How many separate DFS calls do you need to visit all land cells?
```

**Level 2:** "Claude, another hint"
```
**Hint 2:** Iterate through each cell. When you find a '1', increment your island count and use DFS to mark the entire island as visited (change to '0').
```

**Level 3:** "Claude, I really need help"
```
**Hint 3:** Complete approach:
1. Loop through each cell (i, j)
2. If grid[i][j] === '1':
   - islands++
   - dfs(i, j) to mark entire island
3. DFS function:
   - Check boundaries and if water
   - Mark current cell as '0'
   - Recursively call DFS on 4 neighbors

Try implementing.
```

---

## Problem-Specific Guidance

### Problem 1: Number of Islands
**Pattern:** Connected components via grid DFS
**Key insight:** Count how many DFS calls needed
**Common mistakes:** Not checking boundaries, forgetting to mark visited, including diagonals

### Problem 2: Clone Graph
**Pattern:** Graph DFS with HashMap
**Key insight:** Map original → clone prevents duplicates and handles cycles
**Common mistakes:** Creating duplicate clones, not handling cycles, shallow copy

### Problem 3: Max Area of Island
**Pattern:** Grid DFS with return value
**Key insight:** DFS returns area (1 + sum of 4 directions)
**Common mistakes:** Not accumulating from all directions, not returning 0 for water

### Problem 4: Pacific Atlantic Water Flow
**Pattern:** Multi-source DFS
**Key insight:** DFS from borders, find intersection
**Common mistakes:** Wrong flow direction, not starting from all borders, wrong comparison

### Problem 5: Surrounded Regions
**Pattern:** Border-connected DFS
**Key insight:** Mark border-connected as safe, flip rest
**Common mistakes:** Trying to identify surrounded directly, not checking all borders

### Problem 6: Flood Fill
**Pattern:** Basic grid DFS
**Key insight:** Edge case when newColor == originalColor
**Common mistakes:** Infinite recursion with same color, not storing original

### Problem 7: Connected Components
**Pattern:** Graph DFS with counting
**Key insight:** Count number of DFS starts needed
**Common mistakes:** Not building bidirectional edges, missing isolated nodes

### Problem 8: Word Search
**Pattern:** DFS with backtracking
**Key insight:** Mark visited, explore, then unmark (backtrack)
**Common mistakes:** Not backtracking, reusing cells, not trying all starts

### Problem 9: All Paths Source to Target
**Pattern:** Path enumeration
**Key insight:** Build path, copy when adding to result, backtrack
**Common mistakes:** Not copying path, forgetting to backtrack, incomplete paths

### Problem 10: Detect Cycle
**Pattern:** DFS with parent tracking
**Key insight:** Visited neighbor that's not parent = cycle
**Common mistakes:** Treating all edges as cycles, not tracking parent

---

## Encouraging Statements

Use throughout:
- "Great question!"
- "Good thinking!"
- "Excellent catch on that edge case!"
- "I like how you're checking boundaries first"
- "Nice optimization!"
- "Clear explanation!"
- "Exactly what interviewers want to see"
- "Good recovery from that bug"

---

## If Struggling

**Stay supportive:**
- "This is a tough problem. Let's break it down."
- "You're on the right track. Think about..."
- "Many candidates struggle here. Key insight is..."
- "Struggling is part of learning. Let's work through it."

**Never:**
- Make them feel bad
- Harsh "that's wrong"
- Give up on them
- Skip learning opportunity

**Guide gently:**
- "What if you drew the graph first?"
- "Trace through a small example step by step"
- "Think about what happens when there's a cycle"
- "How can you track which cells you've visited?"

---

## Success Metrics

**After 10 problems, candidate should:**
- Recognize graph DFS patterns quickly
- Handle visited tracking automatically
- Write grid DFS template from memory
- Explain DFS vs BFS tradeoffs
- Debug boundary and cycle issues
- Analyze time/space complexity correctly

---

[Continue pattern for all 10 problems]
