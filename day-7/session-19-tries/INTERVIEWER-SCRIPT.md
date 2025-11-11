# Interviewer Script: Tries

## Phase 1: Video Assignment (5 min)

**You:** "Claude, start session 7 19"

**Me:** "Starting Day 7, Session 19: Tries (Prefix Trees).

Today we'll master Trie data structures - the go-to solution for efficient string operations, autocomplete, and word games.

**Watch this video first:** [Implement Trie - Leetcode 208](https://www.youtube.com/watch?v=oobqoCJlHA0) (20 min)

Say 'I watched the video' when you're ready for the concept check."

---

## Phase 2: Concept Check (10 min)

**You:** "I watched the video"

**Me:** "Great! Let's verify your understanding of Tries. I'll ask you a few questions.

**Question 1:** Explain in your own words what a Trie is and why we use it instead of a HashSet for storing words."

**Expected Answer:** A Trie is a tree structure where each node represents a character, and paths from root to nodes spell out strings. We use it for efficient prefix operations (O(prefix_length) vs O(num_words × word_length) for HashSet), memory sharing of common prefixes, and natural alphabetical ordering.

**Question 2:** What's the time complexity of insert, search, and startsWith operations in a Trie?"

**Expected Answer:** All three are O(m) where m is the length of the word/prefix. This is independent of how many words are stored.

**Question 3:** When would you use a Map vs an Array to store children in a TrieNode?"

**Expected Answer:** Use Array when the alphabet is fixed and small (e.g., 26 lowercase letters) for better cache locality. Use Map when the alphabet is large or variable (e.g., Unicode) to save space.

**Question 4:** How do you handle wildcard characters like '.' in Trie search?"

**Expected Answer:** Use DFS/recursion. When encountering '.', recursively try all children at that position. For regular characters, follow the normal path.

**Me:** "Excellent! You understand the fundamentals. Let's cover some interview tips before starting problems."

---

## Phase 3: Tips & Tricks (5 min)

**Me:** "Here are key insights for Trie problems in interviews:

1. **Always clarify the alphabet** - Ask if it's just lowercase, all ASCII, or Unicode
2. **Consider space tradeoffs** - Tries can use significant memory
3. **Draw it out** - Visualizing the Trie helps avoid bugs
4. **Don't forget isEndOfWord** - Common bug is forgetting to mark word endings
5. **Think about optimization** - Pruning, early termination, compressed tries

Common patterns to recognize:
- **Prefix operations** → Use Trie
- **Wildcard/pattern matching** → Trie + DFS
- **Word games/puzzles** → Often Trie + Backtracking
- **Autocomplete** → Trie with frequency/ranking

Ready to solve problems? Let's start with Problem 1."

---

## Phase 4: Problem Solving (2-3 hours)

### Problem 1: Implement Trie (15 min)

**Me:** "Let's implement a basic Trie. Take 2 minutes to understand the problem."

*After 2 minutes*

**Me:** "What's your approach?"

**Good Response:** "I'll create a TrieNode class with a Map for children and a boolean for end of word. Insert traverses and creates nodes, search traverses and checks isEndOfWord, startsWith just traverses."

**Me:** "Perfect! Code it up. Remember to handle edge cases."

*After implementation*

**Me:** "Good! What's the space complexity of your Trie?"

**Expected:** "O(ALPHABET_SIZE × N × M) where N is number of words and M is average length."

### Problem 2: Add and Search Words (20 min)

**Me:** "Now let's handle wildcard matching. How does the '.' character change your approach?"

**Good Response:** "I need to use DFS. When I hit '.', I'll try all possible children recursively."

**Me:** "Exactly! What's the time complexity of search with wildcards?"

**Expected:** "O(m × 26^k) worst case, where k is the number of dots."

### Problem 3: Word Search II (30 min)

**Me:** "This combines Tries with backtracking. How would you approach it?"

**Good Response:** "Build a Trie from all words, then DFS through the board while simultaneously traversing the Trie. When I find a complete word, add it to results."

**Me:** "How do you avoid duplicates?"

**Expected:** "Either use a Set for results or mark found words as null in the Trie."

**Me:** "What optimization can you add?"

**Expected:** "Prune branches - if a Trie node has no children after finding a word, we can remove it to avoid unnecessary exploration."

### Problem 4: Longest Word in Dictionary (20 min)

**Me:** "What does 'built one character at a time' mean?"

**Good Response:** "Every prefix of the word must also be a valid word in the dictionary."

**Me:** "How do you handle ties?"

**Expected:** "Return the lexicographically smallest word among those with the same length."

### Problem 5: Replace Words (20 min)

**Me:** "How is this different from regular Trie search?"

**Good Response:** "I need to find the shortest prefix that exists as a root, not exact match."

**Me:** "What's your optimization strategy?"

**Expected:** "Stop as soon as I find the first root while traversing - that's guaranteed to be the shortest."

### Problem 6: Magic Dictionary (25 min)

**Me:** "The constraint is exactly one character must be different. How do you track this?"

**Good Response:** "Use a boolean flag in recursion to track if I've made my one allowed change."

**Me:** "Can you optimize the space?"

**Expected:** "Instead of Trie, I could use a HashSet with all possible one-character variations, but that's O(n×m×26) space."

### Problem 7: Prefix and Suffix Search (30 min)

**Me:** "This needs both prefix and suffix matching. What's your approach?"

**Good Response:** "I'll create combinations like 'suffix#prefix' for all possible suffixes of each word."

**Me:** "Why does this work?"

**Expected:** "Because searching for 'suf#pre' will find all words that have suffix 'suf' and prefix 'pre'."

**Me:** "What's the space tradeoff?"

**Expected:** "O(N × L^2) where L is max word length, since we store L suffixes for each word."

### Problem 8: Word Squares (30 min)

**Me:** "Explain what makes a valid word square."

**Good Response:** "The kth row and kth column read the same. So square[i][j] == square[j][i]."

**Me:** "How do you determine what words can go in the next row?"

**Expected:** "The prefix is determined by taking the kth character from each previous row, where k is the current row index."

### Problem 9: Concatenated Words (25 min)

**Me:** "How do you check if a word is concatenated?"

**Good Response:** "Use DP where dp[i] means word[0:i] can be formed. For each position, check all possible last words."

**Me:** "How do you avoid counting the word itself?"

**Expected:** "Skip the case where we use the entire word as a single piece (when i=0 and j=word.length)."

### Problem 10: Stream of Characters (25 min)

**Me:** "We need to check suffixes efficiently. What's your approach?"

**Good Response:** "Build a reverse Trie - insert words backward. Then check the stream backward."

**Me:** "How do you handle the stream getting very long?"

**Expected:** "Keep a buffer limited to the length of the longest word in the dictionary."

---

## Phase 5: Wrap-up (5 min)

**Me:** "Excellent work! Let's review what you've learned:

**Strengths I observed:**
- [Specific positive feedback based on performance]

**Areas to focus on:**
- [Specific areas for improvement]

**Key Takeaways:**
1. Tries excel at prefix operations and string manipulation
2. Combine with DFS for wildcard/pattern matching
3. Space complexity is the main tradeoff
4. Drawing helps visualize the structure

**Action items before next session:**
- Review any problems you struggled with
- Practice implementing a Trie from memory
- Try solving Trie problems without hints

Ready for Session 20 on Bit Manipulation? Take a 15-minute break first!"

---

## Scoring Rubric

**For each problem:**
- **Approach (40%):** Did they identify Trie as the solution?
- **Implementation (30%):** Clean, bug-free code?
- **Complexity (20%):** Correct time/space analysis?
- **Communication (10%):** Clear explanation?

**Overall performance:**
- 90-100%: Ready for advanced topics
- 70-89%: Solid understanding, practice implementation
- 50-69%: Review fundamentals, redo problems
- Below 50%: Revisit tree basics first

---

## Common Mistakes to Watch For

1. **Forgetting isEndOfWord flag** - Won't distinguish prefixes from complete words
2. **Not handling empty strings** - Edge case in many problems
3. **Inefficient wildcard search** - Not pruning impossible branches
4. **Memory leaks** - Not cleaning up deleted nodes
5. **Wrong complexity analysis** - Confusing with tree operations
6. **Array index errors** - When using array-based children

---

## Notes for Claude

- Start gentle, increase difficulty gradually
- If stuck on implementation, guide toward the pattern
- Emphasize visualization for complex problems
- For Hard problems, accept partial solutions
- Celebrate insights and creative approaches
- Time management is crucial with 10 problems