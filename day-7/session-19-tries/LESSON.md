# Lesson: Tries (Prefix Trees)

---

## 📹 Video 1: Trie Implementation & Fundamentals (20 min)

**"Implement Trie (Prefix Tree) - Leetcode 208" by NeetCode**
https://www.youtube.com/watch?v=oobqoCJlHA0

**Alternative:**
"Trie Data Structure" by William Fiset (14 min): https://www.youtube.com/watch?v=AXjmTQ8LEoI

**Focus on:**
- What a Trie is and why we use it
- Basic Trie node structure (children + isEnd flag)
- Insert, search, and startsWith operations
- Time and space complexity analysis

---

## 📹 Video 2: Trie Advanced Patterns (20 min)

**"Design Add and Search Words - Leetcode 211" by NeetCode**
https://www.youtube.com/watch?v=BTf05gs_8iU

**Also watch:**
"Word Search II - Leetcode 212" by NeetCode (15 min): https://www.youtube.com/watch?v=asbcE9mZz_U

**Focus on:**
- Wildcard matching with dots
- Combining Trie with DFS/backtracking
- Pruning techniques for optimization
- When to use Tries vs HashMaps

---

## 🎯 Tries: Structure & Creation

### What is a Trie?

A **Trie** (pronounced "try") is a tree-like data structure used for efficient string storage and retrieval. Also known as a **prefix tree** or **digital tree**.

**Key Properties:**
- Each node represents a single character
- Root node is typically empty
- Path from root to node spells out a string
- Nodes can be marked as end of word

---

### Trie Node Structure

```typescript
// Basic Trie Node with Map
class TrieNode {
    children: Map<string, TrieNode>;
    isEndOfWord: boolean;

    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}

// Trie Node with Array (for fixed alphabet)
class TrieNodeArray {
    children: (TrieNodeArray | null)[];
    isEndOfWord: boolean;

    constructor() {
        this.children = new Array(26).fill(null); // a-z only
        this.isEndOfWord = false;
    }
}
```

**Node Components:**
- **children:** Map/Array of child nodes (one per character)
- **isEndOfWord:** Boolean flag marking complete words
- **Optional:** count (for frequency), value (for data storage)

---

### Complete Trie Implementation

```typescript
class Trie {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    // Insert a word - O(m) time, O(m) space
    insert(word: string): void {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isEndOfWord = true;
    }

    // Search exact match - O(m) time, O(1) space
    search(word: string): boolean {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char)!;
        }
        return node.isEndOfWord;
    }

    // Check prefix exists - O(p) time, O(1) space
    startsWith(prefix: string): boolean {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char)!;
        }
        return true;
    }
}
```

---

## 📊 Big O Notation for Tries

### Complexity Table

| Operation | Time Complexity | Space Complexity | Notes |
|-----------|----------------|------------------|-------|
| **Insert** | O(m) | O(m) | m = word length |
| **Search** | O(m) | O(1) | Exact match |
| **StartsWith** | O(p) | O(1) | p = prefix length |
| **Delete** | O(m) | O(1) | With cleanup |
| **Space (total)** | - | O(ALPHABET_SIZE × N × M) | N words, M avg length |

**Why these complexities?**

```typescript
// O(m) - Insert/Search
// Must traverse every character in word
for (const char of word) {  // m iterations
    // O(1) map operations
}

// O(ALPHABET_SIZE × N × M) - Space
// Each node can have up to ALPHABET_SIZE children
// N words with M average length = N × M nodes
// Each node stores children map
```

---

### Trie vs HashMap

| Feature | Trie | HashMap |
|---------|------|---------|
| **Prefix search** | O(p) | O(n × m) |
| **Autocomplete** | O(p + k) | O(n × m) |
| **Memory** | Higher | Lower |
| **Insert/Search** | O(m) | O(1) average |
| **Best for** | Strings, prefixes | Any data type |

**Say this:** "Tries trade space for prefix search speed. Use Tries when prefix operations are frequent, HashMaps for simple lookups."

---

## 🧩 Common Trie Patterns

### Pattern 1: Wildcard Matching

**📹 Learn:** [Design Add and Search Words](https://www.youtube.com/watch?v=BTf05gs_8iU) by NeetCode (~10 min)

Used when: Support '.' wildcard matching any character.

```typescript
searchWithWildcard(word: string): boolean {
    const dfs = (index: number, node: TrieNode): boolean => {
        // Base case: reached end of word
        if (index === word.length) {
            return node.isEndOfWord;
        }

        const char = word[index];

        if (char === '.') {
            // Try all possible children
            for (const child of node.children.values()) {
                if (dfs(index + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            // Regular character
            if (!node.children.has(char)) {
                return false;
            }
            return dfs(index + 1, node.children.get(char)!);
        }
    };

    return dfs(0, this.root);
}
```

**Time:** O(m × 26^k) where k = number of wildcards | **Space:** O(m) recursion depth

---

### Pattern 2: Collecting Words with Prefix

Used when: Get all words starting with a prefix (autocomplete).

```typescript
wordsWithPrefix(prefix: string): string[] {
    const result: string[] = [];
    let node = this.root;

    // Navigate to prefix end
    for (const char of prefix) {
        if (!node.children.has(char)) {
            return result;
        }
        node = node.children.get(char)!;
    }

    // DFS to collect all words
    const dfs = (currentNode: TrieNode, path: string) => {
        if (currentNode.isEndOfWord) {
            result.push(prefix + path);
        }
        for (const [char, child] of currentNode.children) {
            dfs(child, path + char);
        }
    };

    dfs(node, "");
    return result;
}
```

**Time:** O(p + n × m) where p = prefix length, n = matching words | **Space:** O(n × m)

---

### Pattern 3: Trie + Backtracking

**📹 Learn:** [Word Search II](https://www.youtube.com/watch?v=asbcE9mZz_U) by NeetCode (~15 min)

Used when: Search grid for multiple words simultaneously.

```typescript
function findWords(board: string[][], words: string[]): string[] {
    // Build Trie from words
    const root = new TrieNode();
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.word = word; // Store complete word
    }

    const result: string[] = [];
    const m = board.length;
    const n = board[0].length;

    const dfs = (i: number, j: number, node: TrieNode): void => {
        // Bounds check
        if (i < 0 || i >= m || j < 0 || j >= n) return;

        const char = board[i][j];
        if (char === '#' || !node.children.has(char)) return;

        node = node.children.get(char)!;

        // Found a word
        if (node.word !== null) {
            result.push(node.word);
            node.word = null; // Avoid duplicates
        }

        // Mark visited
        board[i][j] = '#';

        // Explore 4 directions
        dfs(i + 1, j, node);
        dfs(i - 1, j, node);
        dfs(i, j + 1, node);
        dfs(i, j - 1, node);

        // Restore cell
        board[i][j] = char;
    };

    // Start DFS from each cell
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            dfs(i, j, root);
        }
    }

    return result;
}
```

**Key insight:** Trie allows checking multiple words simultaneously during one grid traversal.

**Time:** O(m × n × 4^L) where L = max word length | **Space:** O(TOTAL_CHARS)

---

### Pattern 4: Reverse Trie for Suffix Matching

Used when: Check if suffix matches any word.

```typescript
class StreamChecker {
    private root: TrieNode;
    private stream: string[];
    private maxLength: number;

    constructor(words: string[]) {
        this.root = new TrieNode();
        this.stream = [];
        this.maxLength = 0;

        // Build reverse Trie
        for (const word of words) {
            this.maxLength = Math.max(this.maxLength, word.length);
            let node = this.root;

            // Insert word in reverse
            for (let i = word.length - 1; i >= 0; i--) {
                const char = word[i];
                if (!node.children.has(char)) {
                    node.children.set(char, new TrieNode());
                }
                node = node.children.get(char)!;
            }
            node.isEndOfWord = true;
        }
    }

    query(letter: string): boolean {
        this.stream.push(letter);

        // Keep stream size limited
        if (this.stream.length > this.maxLength) {
            this.stream.shift();
        }

        // Check if any suffix matches
        let node = this.root;
        for (let i = this.stream.length - 1; i >= 0; i--) {
            const char = this.stream[i];
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char)!;
            if (node.isEndOfWord) {
                return true;
            }
        }

        return false;
    }
}
```

**Key insight:** Reverse Trie allows suffix checking by traversing stream backward.

**Time:** O(m) per query | **Space:** O(TOTAL_CHARS)

---

## 💡 Interview Tips

### Array vs Map for Children

**Use Array when:**
- Fixed alphabet size (e.g., lowercase a-z only)
- Dense character distribution
- Memory predictable (26 × node count)

**Use Map when:**
- Large or variable alphabet (Unicode, mixed case)
- Sparse character distribution
- Memory scales with actual characters

```typescript
// Array-based (lowercase only)
private charToIndex(char: string): number {
    return char.charCodeAt(0) - 'a'.charCodeAt(0);
}

// Usage
if (!node.children[index]) {
    node.children[index] = new TrieNode();
}

// Map-based (any characters)
if (!node.children.has(char)) {
    node.children.set(char, new TrieNode());
}
```

---

### TypeScript Trie Patterns

```typescript
// Generic Trie with value storage
interface TrieNode<T> {
    children: Map<string, TrieNode<T>>;
    isEndOfWord: boolean;
    value?: T;
}

// Trie with frequency tracking
class FrequencyTrie {
    private root: TrieNode;

    insert(word: string): void {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
            node.count = (node.count || 0) + 1; // Track frequency
        }
        node.isEndOfWord = true;
    }
}

// Delete with cleanup
delete(word: string): boolean {
    const deleteHelper = (node: TrieNode, word: string, index: number): boolean => {
        if (index === word.length) {
            if (!node.isEndOfWord) return false;
            node.isEndOfWord = false;
            return node.children.size === 0; // Can delete if no children
        }

        const char = word[index];
        if (!node.children.has(char)) return false;

        const child = node.children.get(char)!;
        const shouldDelete = deleteHelper(child, word, index + 1);

        if (shouldDelete) {
            node.children.delete(char);
            return node.children.size === 0 && !node.isEndOfWord;
        }

        return false;
    };

    return deleteHelper(this.root, word, 0);
}
```

---

### Common Edge Cases

```typescript
// Handle empty strings
if (word.length === 0) {
    this.root.isEndOfWord = true;
    return;
}

// Check for null/undefined
if (!word || word.length === 0) return false;

// Case sensitivity
word = word.toLowerCase(); // Normalize if needed

// Duplicate insertions
// isEndOfWord handles this - safe to insert multiple times
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Trie node:** children (Map/Array) + isEndOfWord flag
- **Insert/Search:** O(m) where m = word length
- **Prefix search:** O(p) where p = prefix length
- **Space:** O(ALPHABET_SIZE × N × M)
- **Wildcard:** Use DFS, try all children for '.'
- **Backtracking:** Combine Trie with grid DFS
- **Reverse Trie:** Insert words backward for suffix matching

---

[Back to Session README](./README.md)
