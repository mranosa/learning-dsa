# Technical Vocabulary - Quick Reference

**Purpose:** Lookup definitions for technical terms used in interviews. Keep this visible while streaming for confident communication.

**Format:** 2-Column (Left: Term | Right: Meaning & Example)

---

## Algorithm & Problem-Solving Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Complement** | Value needed to reach target<br>*"Calculate complement as target minus current number"* |
| **Optimal** | Best possible solution<br>*"This is optimal - can't do better than O of n"* |
| **Greedy** | Always pick locally best choice<br>*"Using greedy approach: take largest available each time"* |
| **Heuristic** | Strategy that usually works well<br>*"This heuristic gives good results in most cases"* |
| **Amortized** | Average cost over many operations<br>*"Array push is O of 1 amortized time"* |
| **Auxiliary** | Helper or extra<br>*"I'm using an auxiliary array to store intermediate results"* |
| **Sentinel** | Special value marking boundary<br>*"Using negative 1 as sentinel to mark visited nodes"* |
| **Pivot** | Reference point for comparison<br>*"In QuickSort, choose pivot and partition around it"* |

---

## Array & String Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Subarray** | Contiguous portion of array<br>*"A subarray is continuous elements like [2,3,4] from [1,2,3,4,5]"* |
| **Subsequence** | Elements in order but not necessarily contiguous<br>*"[1,3,5] is a subsequence of [1,2,3,4,5]"* |
| **Substring** | Contiguous portion of string<br>*"'abc' is a substring of 'xabcy'"* |
| **Contiguous** | Connected, no gaps between elements<br>*"Looking for contiguous subarray with maximum sum"* |
| **Adjacent** | Next to each other<br>*"Check adjacent cells in matrix: up, down, left, right"* |
| **Prefix** | From start up to position<br>*"Prefix sum from index 0 to i"* |
| **Suffix** | From position to end<br>*"Suffix product from index i to end"* |
| **In-place** | Modify without extra space<br>*"Solve in-place using O of 1 space"* |

---

## Data Structure Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Index** | Position in array (0-based)<br>*"Element at index 0 is the first element"* |
| **Pointer** | Variable indicating position<br>*"Using two pointers: left at start, right at end"* |
| **Head** | First element (linked list)<br>*"The head points to the first node"* |
| **Tail** | Last element<br>*"The tail is the last node in the list"* |
| **Dummy node** | Fake starting node to simplify logic<br>*"Using dummy node so I don't special-case the head"* |
| **Key** | Identifier in map/object<br>*"Store number as key, index as value"* |
| **Value** | Data associated with key<br>*"Map stores key-value pairs"* |
| **Entry** | Key-value pair<br>*"Each entry in the map represents a number and its index"* |
| **Bucket** | Storage location in hash table<br>*"Hash function maps keys to buckets"* |
| **Node** | Element in tree or graph<br>*"Each node has a value and pointers to children"* |

---

## Action Words (Verbs)

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Initialize** | Set starting value<br>*"Initialize count to zero"* |
| **Declare** | Create a variable<br>*"Declare a map to store values"* |
| **Increment** | Add 1 or increase<br>*"Increment the counter: i plus plus"* |
| **Decrement** | Subtract 1 or decrease<br>*"Decrement right pointer"* |
| **Accumulate** | Build up total over time<br>*"Accumulate sum as I iterate"* |
| **Iterate** | Go through one by one<br>*"Iterate through the array with a for loop"* |
| **Traverse** | Visit each element<br>*"Traverse the tree in preorder"* |
| **Parse** | Analyze and extract information<br>*"Parse the string to extract numbers"* |
| **Merge** | Combine two structures<br>*"Merge two sorted arrays into one"* |
| **Split** | Divide into parts<br>*"Split string by delimiter"* |
| **Swap** | Exchange two values<br>*"Swap elements at indices i and j"* |
| **Shift** | Move elements left or right<br>*"Shift all elements one position to the right"* |

---

## Graph & Tree Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Edge** | Connection between two nodes<br>*"Graph has vertices and edges"* |
| **Vertex** | Node in a graph<br>*"Count number of vertices in graph"* |
| **Neighbor** | Adjacent connected node<br>*"Check all neighbors of current node"* |
| **Degree** | Number of edges from a node<br>*"Node degree is 3 - connected to 3 neighbors"* |
| **Path** | Sequence of connected nodes<br>*"Find path from start to end node"* |
| **Cycle** | Path that returns to starting node<br>*"Detect if graph contains a cycle"* |
| **Leaf** | Node with no children<br>*"Leaf nodes have no left or right child"* |
| **Root** | Top node in tree<br>*"Start traversal from root"* |
| **Parent** | Node directly above<br>*"Parent of current node"* |
| **Child** | Node directly below<br>*"Left child and right child"* |
| **Sibling** | Nodes with same parent<br>*"These two nodes are siblings"* |
| **Ancestor** | Parent, grandparent, etc.<br>*"All ancestors of this node"* |
| **Descendant** | Child, grandchild, etc.<br>*"All descendants in subtree"* |
| **Depth** | Distance from root<br>*"Node depth is 3 - three levels down from root"* |
| **Height** | Maximum depth in tree<br>*"Tree height is 4"* |
| **Level** | All nodes at same depth<br>*"Process tree level by level"* |
| **Subtree** | Tree rooted at a node<br>*"The left subtree contains all nodes to the left"* |

---

## Complexity Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Big O** | Upper bound on growth rate<br>*"Big O notation describes worst-case performance"* |
| **Linear** | O(n) - grows proportionally<br>*"Linear time means doubling input doubles runtime"* |
| **Quadratic** | O(n²) - nested loops<br>*"Quadratic complexity from two nested loops"* |
| **Logarithmic** | O(log n) - halving search space<br>*"Binary search is logarithmic - very fast"* |
| **Constant** | O(1) - doesn't change with input<br>*"Array access is constant time"* |
| **Exponential** | O(2^n) - doubles each step<br>*"Brute force recursion is exponential - very slow"* |
| **Linearithmic** | O(n log n) - efficient sorting<br>*"Merge sort is linearithmic complexity"* |
| **Worst case** | Maximum possible operations<br>*"Worst case is when array is reverse sorted"* |
| **Average case** | Typical expected performance<br>*"Average case for hash map is O of 1"* |
| **Best case** | Minimum possible operations<br>*"Best case is when target is at index 0"* |
| **Space complexity** | Extra memory used<br>*"Space complexity is O of n for the hash map"* |

---

## Dynamic Programming Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Memoization** | Cache results to avoid recomputing<br>*"Using memoization to store Fibonacci results"* |
| **Tabulation** | Build solution table bottom-up<br>*"Tabulation approach: fill DP array iteratively"* |
| **Overlapping subproblems** | Same subproblems solved multiple times<br>*"DP works because of overlapping subproblems"* |
| **Optimal substructure** | Optimal solution contains optimal subsolutions<br>*"Problem has optimal substructure - perfect for DP"* |
| **State** | Variables defining subproblem<br>*"State is defined by current index and remaining sum"* |
| **Transition** | How to go from one state to another<br>*"State transition: DP[i] equals DP[i minus 1] plus DP[i minus 2]"* |
| **Base case** | Smallest subproblem with known answer<br>*"Base case: DP[0] equals 1"* |
| **Recurrence** | Relationship between subproblems<br>*"The recurrence relation is F(n) equals F(n minus 1) plus F(n minus 2)"* |

---

## Search & Sort Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Binary search** | Halve search space each iteration<br>*"Using binary search on sorted array for O of log n"* |
| **Lower bound** | First element >= target<br>*"Find lower bound using binary search"* |
| **Upper bound** | First element > target<br>*"Upper bound is position where we'd insert"* |
| **Partition** | Divide array around pivot<br>*"Partition array so all smaller elements come before pivot"* |
| **Stable sort** | Preserves relative order of equal elements<br>*"Merge sort is stable, QuickSort is not"* |
| **In-place sort** | Sort without extra array<br>*"QuickSort is in-place with O of 1 space"* |

---

## Miscellaneous Important Terms

| Term | Meaning & Usage Example |
|------|-------------------------|
| **Constraint** | Limitation or requirement<br>*"Constraint: array length up to 10 to the 4"* |
| **Edge case** | Special or extreme scenario<br>*"Edge cases: empty array, single element, all same"* |
| **Boundary** | Limit or edge of valid range<br>*"Check if index is within bounds before accessing"* |
| **Valid** | Meets requirements<br>*"Check if indices are valid before using them"* |
| **Distinct** | All different, no duplicates<br>*"Array contains distinct elements only"* |
| **Unique** | Appears only once<br>*"Find the unique element that appears once"* |
| **Frequency** | How many times something appears<br>*"Count frequency of each character"* |
| **Occurrence** | Instance of appearance<br>*"Find first occurrence of target"* |
| **Candidate** | Potential solution or element<br>*"This element is a candidate for the answer"* |
| **Remainder** | What's left after division<br>*"Remainder when dividing by 2 tells if odd or even"* |
| **Parity** | Odd or even<br>*"Check parity: number modulo 2"* |

---

## How to Use This Guide:

### While Planning:
1. Scan for terms you'll need
2. Check meanings
3. Use in your explanation
4. Sound professional!

### While Coding:
1. Keep visible (print it!)
2. Quick lookup when needed
3. Use correct terminology
4. Build vocabulary naturally

### Example:
**Before:** "I'll use the thing we learned about... the uh... opposite number?"
**After:** "I'll calculate the complement as target minus current number"

---

## Pro Tips:

✅ **Use these terms naturally** - don't force them
✅ **Explain as you use** - "complement, which is the value needed..."
✅ **Build vocabulary gradually** - master 5-10 terms per session
✅ **Reference this guide** while streaming - it's okay!

**Most Important Terms for Session 1:**
- Complement, iterate, traverse, optimal, initialize
- Index, pointer, adjacent, contiguous
- Linear, constant, worst case

---

[Printable 2-Column Version] | [Back to README](./README.md)
