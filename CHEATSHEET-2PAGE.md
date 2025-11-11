# Interview Cheatsheet - 2 Pages

**Print landscape, 2-column format**

---

# PAGE 1: INTERVIEW ESSENTIALS

## Column 1

### UMPIRE METHOD
**U - UNDERSTAND** (2 min)
- Restate problem
- Ask: constraints? sorted? empty? duplicates?

**M - MATCH** (1 min)
- Identify pattern from keywords

**P - PLAN** (3-5 min)
- Brute force FIRST
- Then optimized
- Walk through example

**I - IMPLEMENT** (15-25 min)
- Think aloud!
- Use descriptive names

**R - REVIEW** (3-5 min)
- Test edge cases

**E - EVALUATE** (2 min)
- State time/space complexity

### TOP PATTERNS
| Keyword | Pattern |
|---------|---------|
| Subarray | Sliding Window |
| Sorted | Binary Search |
| Find pair | Hash Map |
| Top K | Heap |
| All combinations | Backtracking |
| Shortest path | BFS |

### TYPESCRIPT ESSENTIALS
```ts
// Sort
arr.sort((a,b) => a-b)  // MUST use comparator!

// Map
const map = new Map<number, number>();
map.set(k, v); map.get(k); map.has(k);

// Set
const set = new Set<number>();
set.add(v); set.has(v);

// Two pointers
let [left, right] = [0, arr.length-1];

// Swap
[arr[i], arr[j]] = [arr[j], arr[i]];
```

---

## Column 2

### COMPLEXITY
| Pattern | Time | Space |
|---------|------|-------|
| Two Pointers | O(n) | O(1) |
| Hash Map | O(n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Sliding Window | O(n) | O(k) |
| DFS/BFS Tree | O(n) | O(h) |
| DFS/BFS Graph | O(V+E) | O(V) |
| DP 1D | O(n) | O(n) |
| DP 2D | O(n²) | O(n²) |
| Backtracking | O(2ⁿ) | O(n) |

### EDGE CASES
□ Empty input
□ Single element
□ All same
□ Negatives/zero
□ Max constraints
□ Duplicates

### COMMON BUGS
□ Off-by-one (i < n vs i <= n)
□ Array out of bounds
□ Forgot increment
□ Wrong comparison
□ Mutating while iterating

### TS GOTCHAS
⚠️ arr.sort() sorts as strings!
⚠️ shift()/unshift() is O(n)
⚠️ Math.max(...huge) crashes
⚠️ Always use ===

---

# PAGE 2: VOICE & VOCABULARY

## Column 1

### F12 VOICE COMMANDS
**Setup:** `./setup-voice-hotkeys`

**Session:**
- "Claude, start session X Y, ok submit"
- "Give me the problem, ok submit"
- "I'm stuck, ok submit"
- "Evaluate me, ok submit"
- "Next problem, ok submit"

**Shortcuts:**
- "Go" = Give problem
- "Hint" = Get hint
- "Done" = Evaluate me
- "Next" = Next problem

### THINKING-ALOUD PHRASES
**Starting:**
- "I think I'll use..."
- "This looks like a _____ problem"

**Planning:**
- "The brute force would be..."
- "I can optimize this by..."
- "The trade-off is..."

**Coding:**
- "I'm creating a _____ to..."
- "Now I'm looping through..."
- "I'll check if..."

**Complexity:**
- "The time complexity is O of n because..."
- "Space-wise, I'm using..."

**Edge Cases:**
- "What if the input is empty?"
- "This handles the case where..."

**Testing:**
- "Let me trace through with..."
- "For this input, first..."

---

## Column 2

### TOP 30 TECHNICAL TERMS
**Must Know:**
- **Complement** - Value needed (target - current)
- **Iterate** - Go through one by one
- **Traverse** - Visit each element
- **Optimal** - Best possible solution
- **Index** - Position in array
- **Pointer** - Variable indicating position
- **Adjacent** - Next to each other
- **Contiguous** - Connected, no gaps
- **Initialize** - Set starting value
- **Increment** - Add 1 (i++)
- **Decrement** - Subtract 1 (i--)

**Data Structures:**
- **Node** - Element in tree/graph
- **Edge** - Connection between nodes
- **Leaf** - Node with no children
- **Root** - Top node
- **Key/Value** - Map entries

**Complexity:**
- **Linear** - O(n)
- **Quadratic** - O(n²)
- **Logarithmic** - O(log n)
- **Constant** - O(1)

**DP:**
- **Memoization** - Cache results
- **Base case** - Stopping condition

**Arrays:**
- **Subarray** - Contiguous portion
- **Prefix** - From start
- **Suffix** - From end

### WORKFLOW
```
Setup:
Browser Tab 1: Videos
Browser Tab 2: LeetCode ← CODE HERE
Terminal: ./voice-interview

Session:
F12 → Speak → Auto-type → "ok submit"
Think aloud → I respond in real-time!
```

### QUICK TIPS
✅ Think aloud constantly
✅ Ask clarifying questions
✅ Brute force first
✅ Test edge cases
✅ Use vocabulary guides

**Time:** Easy <15min, Medium <30min

---

**PRINT LANDSCAPE, 2-COLUMN | Keep at desk while coding!**
