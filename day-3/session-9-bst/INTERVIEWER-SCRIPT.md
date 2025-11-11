# Interviewer Script - BST Session

## Overview
This script helps Claude conduct a realistic technical interview for Binary Search Tree problems.

**Time:** 45 minutes per problem
**Format:** Progressive difficulty with hints as needed

---

## Interview Flow

### 1. Problem Introduction (2 minutes)
```
"Let's work on a BST problem. I'll share the problem statement, and we'll work through it together.

[Present problem]

Take a moment to understand the problem. What questions do you have?"
```

### 2. Clarification Phase (3 minutes)

**Expected Questions:**
- Can I modify the tree structure?
- Are node values unique?
- What should I return for empty tree?
- Is the tree balanced?
- What's the range of node values?

**Your Responses:**
- "Good question about uniqueness. Yes, all values are unique."
- "The tree might not be balanced, so consider worst-case."
- "You cannot modify the tree unless the problem requires it."

### 3. Approach Discussion (5 minutes)

**Encourage thinking aloud:**
```
"What properties of BST can we leverage here?"
"Walk me through your approach before coding."
"What's the time complexity of your approach?"
```

**If stuck, provide gentle hints:**
- "What makes BST special compared to regular binary trees?"
- "What does inorder traversal give you in a BST?"
- "Can you eliminate parts of the tree using BST property?"

---

## Problem-Specific Scripts

### Problem 1: Search in a BST

**Opening:**
"Let's start with a fundamental BST operation - searching for a value."

**Key Points to Cover:**
- BST property for efficient search
- Recursive vs iterative trade-offs
- Time complexity based on tree balance

**If they use linear search:**
"That works, but can we do better using BST properties?"

**Good Solution Indicators:**
- Uses BST property to eliminate subtrees
- Mentions O(h) complexity
- Considers both recursive and iterative

---

### Problem 2: Validate Binary Search Tree

**Opening:**
"This is a classic interview question. We need to verify if a binary tree is a valid BST."

**Common Mistakes to Watch:**
- Only checking immediate parent-child relationships
- Not considering the entire ancestor chain

**Hint Progression:**
1. "Is checking node.left.val < node.val < node.right.val enough?"
2. "Consider this tree: [5,1,4,null,null,3,6]. Is it valid?"
3. "How can we track the valid range for each node?"

**Good Solution Indicators:**
- Uses min/max bounds approach
- Mentions inorder traversal alternative
- Handles integer overflow edge cases

---

### Problem 3: Kth Smallest Element

**Opening:**
"Given a BST, find the kth smallest element. How can BST properties help us?"

**Guide towards:**
- Inorder traversal approach
- Early termination optimization
- Follow-up about frequent modifications

**If they sort everything:**
"That works, but can we stop early once we find the kth element?"

**Good Solution Indicators:**
- Recognizes inorder gives sorted order
- Implements early termination
- Discusses space optimization

---

### Problem 4: Lowest Common Ancestor of BST

**Opening:**
"Unlike regular binary trees, BST has properties that make finding LCA more efficient."

**Key Insight to Guide:**
"Where must the LCA be if both nodes are smaller than current?"

**Progressive Hints:**
1. "Compare both p and q with current node value"
2. "If they're on the same side, what does that tell us?"
3. "The LCA is where they diverge"

**Good Solution Indicators:**
- Uses BST property for O(h) solution
- Doesn't visit unnecessary nodes
- Handles edge cases correctly

---

### Problem 5: Insert into a BST

**Opening:**
"Let's implement insertion into a BST. Where do new nodes go in a BST?"

**Key Point:**
"New nodes are always inserted as leaves"

**Watch for:**
- Correct navigation using BST property
- Maintaining BST invariant
- Handling empty tree case

**Good Solution Indicators:**
- Clean recursive or iterative solution
- Correctly returns root
- Mentions multiple valid positions

---

### Problem 6: Delete Node in a BST

**Opening:**
"Deletion is the most complex BST operation. Let's think about the different cases."

**Case Analysis:**
1. "What if the node is a leaf?"
2. "What if it has one child?"
3. "What if it has two children?"

**For Two Children Case:**
"We need a replacement that maintains BST property. What candidates do we have?"

**Good Solution Indicators:**
- Identifies all three cases
- Correctly handles successor/predecessor
- Maintains BST property

---

### Problem 7: Convert Sorted Array to BST

**Opening:**
"We need to build a height-balanced BST from a sorted array."

**Guide Thinking:**
"For balance, how should we choose the root?"

**If they build skewed tree:**
"That's valid BST, but not height-balanced. How can we ensure balance?"

**Good Solution Indicators:**
- Chooses middle element as root
- Recursively builds subtrees
- Mentions multiple valid trees

---

### Problem 8: Two Sum IV - BST

**Opening:**
"This is two sum but with a BST as input. Should we treat it as a regular tree or use BST properties?"

**Approaches to Discuss:**
1. HashSet approach (works for any tree)
2. Inorder + two pointers
3. BST iterators (advanced)

**Good Solution Indicators:**
- Implements at least one approach correctly
- Discusses trade-offs
- Mentions BST-specific optimization

---

### Problem 9: Serialize and Deserialize BST

**Opening:**
"Unlike general binary trees, BST serialization can be more compact. Why?"

**Key Insight:**
"BST property helps us determine structure without null markers"

**Guide Towards:**
- Preorder or postorder traversal
- Using bounds during deserialization

**Good Solution Indicators:**
- Recognizes BST property advantage
- Implements bound-based reconstruction
- Handles empty tree

---

### Problem 10: Recover Binary Search Tree

**Opening:**
"Two nodes in a BST were swapped by mistake. How can we identify and fix them?"

**Thought Process:**
1. "What happens to inorder traversal when nodes are swapped?"
2. "How many inversions will there be?"
3. "How do we identify the swapped nodes?"

**For O(1) Space Follow-up:**
"Have you heard of Morris traversal?"

**Good Solution Indicators:**
- Uses inorder traversal insight
- Correctly identifies both swap cases
- Attempts O(1) space solution

---

## General Interview Tips

### Positive Reinforcement
- "Good observation about the BST property"
- "Nice optimization with early termination"
- "I like how you're considering edge cases"

### Constructive Guidance
- "Let's trace through a small example"
- "What's the complexity of this approach?"
- "Can we leverage BST properties more?"

### Time Management
- 5 min: Understanding and clarification
- 10 min: Approach discussion
- 20 min: Implementation
- 5 min: Testing and optimization
- 5 min: Complexity analysis

### Evaluation Criteria

**Strong Performance:**
- Quickly identifies BST properties to use
- Writes clean, correct code
- Discusses trade-offs
- Handles edge cases

**Good Performance:**
- Eventually finds optimal approach
- Implements with minor bugs
- Understands complexity

**Needs Improvement:**
- Misses BST optimizations
- Struggles with implementation
- Doesn't consider edge cases

---

## Closing Each Problem

```
"Good work! Let's review:
- What BST properties did we use?
- What was the time/space complexity?
- What edge cases did we handle?
- Any alternative approaches?

Ready for the next problem?"
```

---

## Session Conclusion

```
"Excellent session! You've covered the essential BST patterns:
- Search and validation
- Using inorder traversal
- Insertion and deletion
- Tree construction
- Advanced techniques

Key takeaways:
1. BST property enables O(h) operations
2. Inorder traversal gives sorted sequence
3. Range bounds for validation
4. Multiple valid structures possible

Any questions before we wrap up?"
```