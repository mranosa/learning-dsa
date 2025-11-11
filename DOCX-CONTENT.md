# Interview Master Cheatsheet - DOCX Content

**Instructions:** Format this content into a 3-page, 2-column, landscape DOCX file for printing.

---

# PAGE 1: BEFORE YOU CODE

## Column 1: UMPIRE Framework & Pattern Keywords

### UMPIRE METHOD ✅
**U - UNDERSTAND (2 min)**
□ Restate problem
□ Ask clarifying questions
□ Identify inputs/outputs
□ Understand constraints

**M - MATCH (1 min)**
□ Identify pattern from keywords
□ Recall similar problems

**P - PLAN (3-5 min)**
□ Discuss brute force FIRST
□ Explain optimized approach
□ Walk through example
□ Get approval before coding

**I - IMPLEMENT (15-25 min)**
□ Think aloud while coding
□ Use descriptive names
□ Handle edge cases

**R - REVIEW (3-5 min)**
□ Trace through with example
□ Test edge cases
□ Check for bugs

**E - EVALUATE (2 min)**
□ State time complexity
□ State space complexity
□ Discuss trade-offs

### PATTERN KEYWORDS
| Keyword | Pattern |
|---------|---------|
| "Subarray" | Sliding Window, Prefix Sum |
| "Sorted array" | Binary Search, Two Pointers |
| "Find pair" | Two Pointers, Hash Map |
| "Top K" | Heap |
| "All combinations" | Backtracking |
| "Shortest path" | BFS |
| "Maximum/minimum" | DP, Greedy |

---

## Column 2: Complexity & Edge Cases

### TIME COMPLEXITY
| Pattern | Time | Space |
|---------|------|-------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(k) |
| Hash Map | O(n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Tree DFS | O(n) | O(h) |
| Tree BFS | O(n) | O(w) |
| Graph DFS/BFS | O(V+E) | O(V) |
| DP 1D | O(n) | O(n)→O(1) |
| DP 2D | O(n²) | O(n²)→O(n) |
| Backtracking | O(2ⁿ) | O(n) |
| Heap ops | O(log n) | O(n) |

### EDGE CASES CHECKLIST
**Universal:**
□ Empty input ([], "", null)
□ Single element
□ Two elements
□ All same elements
□ Negative numbers/zero
□ Maximum constraints

**Arrays:**
□ First/last element
□ Duplicates

**Strings:**
□ Empty string
□ Single character
□ Spaces

**Trees:**
□ Null root
□ Single node
□ Left-only or right-only

**Graphs:**
□ Disconnected
□ Cycles
□ Single node

---

# PAGE 2: WHILE YOU CODE

## Column 1: TypeScript Essentials

### ARRAY
```ts
// Creation
const arr: number[] = [1, 2, 3];
new Array(5).fill(0);  // [0,0,0,0,0]
Array.from({length: 5}, (_, i) => i);

// Sort (MUST provide comparator!)
arr.sort((a, b) => a - b);  // ascending
arr.sort((a, b) => b - a);  // descending
// ⚠️ arr.sort() sorts as strings!

// Stack
arr.push(x);  // O(1)
arr.pop();    // O(1)

// Queue (slow!)
arr.push(x);   // enqueue O(1)
arr.shift();   // dequeue O(n) ⚠️
```

### MAP (Hash Map)
```ts
const map = new Map<number, number>();
map.set(key, val);
map.get(key);      // or undefined
map.has(key);      // boolean
map.delete(key);
map.size;

// Frequency counter
for (const num of arr) {
  map.set(num, (map.get(num) || 0) + 1);
}
```

### SET (Hash Set)
```ts
const set = new Set<number>();
set.add(val);
set.has(val);
set.delete(val);
set.size;

// Remove duplicates
const unique = [...new Set(arr)];
```

### STRING
```ts
str.length
str[0] or str.charAt(0)
str.charCodeAt(0)  // ASCII code
String.fromCharCode(65)  // 'A'

str.substring(0, 3)
str.slice(-2)  // last 2 chars

str.split('')  // to array
arr.join('')   // to string
[...str]       // handles Unicode

str.includes('x')
str.startsWith('ab')
str.endsWith('yz')
```

### MATH
```ts
Math.max(a, b)
Math.min(a, b)
Math.max(...arr)  // ⚠️ stack overflow on huge arrays

Math.floor(3.7)  // 3
Math.ceil(3.2)   // 4
Math.round(3.5)  // 4
Math.abs(-5)     // 5
```

### COMMON PATTERNS
```ts
// Two pointers
let [left, right] = [0, arr.length - 1];

// Swap
[arr[i], arr[j]] = [arr[j], arr[i]];

// 2D array
const matrix = Array.from(
  {length: rows},
  () => new Array(cols).fill(0)
);
```

---

## Column 2: Communication & Debugging

### WHAT TO SAY

**Starting:**
- "Let me make sure I understand..."
- "Can I ask clarifying questions?"
- "What about edge case X?"

**Planning:**
- "The brute force approach would be..."
- "I can optimize this by..."
- "The trade-off is..."

**Coding:**
- "I'm creating a hash map to..."
- "Now I'll loop through..."
- "This handles the edge case where..."

**Stuck:**
- "Let me think through this..."
- "I'm considering two approaches..."
- "Could you give me a hint about..."

### RED FLAGS ❌
- Jumping straight to code
- Silent coding
- Ignoring edge cases
- Not asking questions
- Defensive about mistakes

### GREEN FLAGS ✅
- Ask clarifying questions
- Discuss multiple approaches
- Think aloud constantly
- Test with examples
- Explain complexity

### COMMON BUGS
□ Off-by-one (i < n vs i <= n)
□ Array out of bounds
□ Forgot to increment loop
□ Wrong comparison (< vs <=)
□ Mutating while iterating
□ Uninitialized variables
□ Wrong recursion base case

### TS GOTCHAS ⚠️
- `arr.sort()` without comparator sorts as strings!
- `shift()/unshift()` is O(n), not O(1)
- `Math.max(...hugeArr)` can crash
- Map keys vs Object keys (type preservation)
- Always use `===` not `==`

---

# PAGE 3: VOICE COMMANDS REFERENCE

## Column 1: Commands

### SESSION MANAGEMENT
**"Claude, start session [day] [session]"**
Begin a session, get video assignment

**"Claude, resume"**
Continue where you left off

**"Claude, next session"**
Complete session, move to next

**"Claude, end session"**
Save and exit gracefully

### INTERVIEW FLOW
**"Claude, I watched the video"**
Start concept check quiz

**"Claude, quiz me"**
Ask me concept questions

**"Claude, give me the problem"** or **"Go"**
Present problem formally

**"Claude, give me tips"**
Share tips before problem

**"Claude, start timer"**
Start countdown for problem

**"Claude, I'm done coding"** or **"Done"**
Move to testing phase

### HELP & HINTS
**"Claude, I'm stuck"** or **"Help"**
Get probing questions

**"Claude, give me a hint"** or **"Hint"**
Level 1 hint (gentle)

**"Claude, another hint"**
Level 2 hint (direct)

**"Claude, I really need help"**
Level 3 hint (step-by-step)

**"Claude, show me the solution"**
Reveal answer (mark for review)

---

## Column 2: More Commands

### EVALUATION
**"Claude, evaluate me"**
Get structured feedback with scores

**"Claude, what did I miss"**
Show missed edge cases

**"Claude, is my complexity right"**
Verify time/space analysis

**"Claude, can I optimize this"**
Suggest optimizations

### PROGRESS
**"Claude, my progress"** or **"Stats"**
Show comprehensive dashboard

**"Claude, mark complete"**
Mark done, auto-commit progress

**"Claude, what's next"**
Preview next problem

**"Claude, save my work"**
Manual commit (mid-work)

### QUICK REFERENCE
**"Claude, show pattern [name]"**
Display code template

**"Claude, TypeScript [method]"**
Show TS method reference

**"Claude, what pattern is this"**
Help identify pattern from problem

### TIME MANAGEMENT
**"Claude, time check"**
Show remaining time + pacing

**"Claude, pause timer"**
Pause countdown, take break

### SHORTCUTS
**"Go"** = Give me the problem
**"Hint"** = Give me a hint
**"Done"** = I'm done coding
**"Help"** = I'm stuck
**"Next"** = Next problem
**"Stats"** = My progress

---

## QUICK TIPS AT BOTTOM
- **Always follow UMPIRE** - Don't skip steps!
- **Think aloud constantly** - Silent coding = red flag
- **Brute force first** - Then optimize
- **Test edge cases** - Empty, single, max
- **Ask questions** - Shows you're thoughtful
- **Practice with timer** - Simulate real pressure
- **Use voice commands naturally** - Makes it interactive

**Time targets:** Easy <15min, Medium <30min, Hard <45min

---

---

# PAGE 4: THINKING-ALOUD PHRASES

## Column 1: Starting & Planning

### STARTING
- "I think I'll use..."
- "This looks like a _____ problem"
- "The pattern I see is..."
- "My first thought is..."
- "Let me start by..."

### PLANNING
- "The brute force would be..."
- "I can optimize this by..."
- "The trade-off is..."
- "This gives me O of n instead of..."

### WHILE CODING
- "I'm creating a _____ to..."
- "Now I'm looping through..."
- "Let me initialize..."
- "I'll check if..."
- "This handles the case where..."

### DATA STRUCTURES
- "I'm using a hash map because..."
- "I'm storing _____ in _____"
- "The map stores key-value pairs where..."
- "Adding this to the..."

---

## Column 2: Complexity & Testing

### COMPLEXITY
- "The time complexity is O of n because..."
- "Space-wise, I'm using O of n for..."
- "Each operation takes O of 1"
- "This runs in O of..."
- "Compared to brute force..."

### EDGE CASES
- "What if the input is empty?"
- "I should handle the case where..."
- "Edge case: when _____, then _____"
- "Let me check for..."

### TESTING
- "Let me trace through with..."
- "For this input, first..."
- "Step by step..."
- "This should return..."

### WHEN UNCERTAIN
- "I'm thinking through..."
- "Let me consider..."
- "Two approaches come to mind..."
- "The question I have is..."

---

# PAGE 5: TECHNICAL VOCABULARY

## Column 1: Core Terms

### ALGORITHM TERMS
**Complement** - Value needed to reach target
*"Calculate complement as target - current"*

**Iterate** - Go through one by one
*"Iterating through the array"*

**Traverse** - Visit each element
*"Traversing the tree"*

**Contiguous** - Connected, no gaps
*"Subarray is contiguous"*

**Adjacent** - Next to each other
*"Check adjacent cells"*

**Optimal** - Best possible solution
*"This is optimal - can't do better"*

### DATA STRUCTURE
**Index** - Position in array (0-based)
**Pointer** - Variable indicating position
**Key** - Identifier in map
**Value** - Data stored with key
**Node** - Element in tree/graph
**Edge** - Connection between nodes

### ACTIONS
**Initialize** - Set starting value
**Increment** - Add 1 (i++)
**Decrement** - Subtract 1 (i--)
**Accumulate** - Build up total
**Swap** - Exchange two values
**Merge** - Combine two things

---

## Column 2: Advanced Terms

### COMPLEXITY
**Linear** - O(n), grows proportionally
**Quadratic** - O(n²), nested loops
**Logarithmic** - O(log n), halving
**Constant** - O(1), fixed time
**Amortized** - Average over operations

### TREE/GRAPH
**Leaf** - Node with no children
**Root** - Top node in tree
**Depth** - Distance from root
**Height** - Maximum depth
**Path** - Sequence of nodes
**Cycle** - Path returning to start
**Neighbor** - Adjacent connected node

### DP TERMS
**Memoization** - Cache results
**Tabulation** - Build table bottom-up
**Base case** - Smallest subproblem
**State** - Variables defining subproblem

### SEARCH/SORT
**Binary search** - Halve search space
**Partition** - Divide around pivot
**Lower bound** - First >= target
**In-place** - No extra space

### OTHER
**Constraint** - Limitation
**Edge case** - Special scenario
**Frequency** - Count of occurrences
**Distinct** - All different
**Prefix** - From start to position
**Suffix** - From position to end

---

[End of DOCX Content - Format this into 5-page landscape document]

**PRINT ALL 5 PAGES - Keep at desk while streaming!**
