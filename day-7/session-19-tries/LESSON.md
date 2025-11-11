# Lesson: Tries (Prefix Trees)

## Video Assignment

**Watch this video:** [Implement Trie - Leetcode 208](https://www.youtube.com/watch?v=oobqoCJlHA0)
**Duration:** 20 minutes
**Channel:** NeetCode

After watching, you should understand:
- What a Trie is and why we use it
- Basic Trie node structure
- Insert, search, and startsWith operations
- Time and space complexity analysis

---

## Core Concepts

### 1. What is a Trie?

A **Trie** (pronounced "try") is a tree-like data structure used for efficient string storage and retrieval. Also known as a **prefix tree** or **digital tree**.

```typescript
// Basic Trie Node structure
class TrieNode {
    children: Map<string, TrieNode>;
    isEndOfWord: boolean;

    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}
```

**Key Properties:**
- Each node represents a single character
- Root node is typically empty
- Path from root to node spells out a string
- Nodes can be marked as end of word

### 2. Why Use Tries?

**Advantages over HashMaps:**
- **Prefix searching:** O(p) where p is prefix length
- **Alphabetical ordering:** Natural sorting of strings
- **Memory sharing:** Common prefixes share nodes
- **Wildcard matching:** Efficient pattern matching

**Use Cases:**
- Autocomplete systems
- Spell checkers
- IP routing tables
- Word games (Scrabble, Boggle)
- Phone directories

### 3. Basic Operations

#### Insert
```typescript
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
```
**Time:** O(m) where m is word length
**Space:** O(m) worst case

#### Search
```typescript
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
```
**Time:** O(m)
**Space:** O(1)

#### StartsWith
```typescript
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
```
**Time:** O(p) where p is prefix length
**Space:** O(1)

### 4. Advanced Patterns

#### Wildcard Matching
Support '.' to match any character:
```typescript
searchWithWildcard(word: string): boolean {
    const dfs = (index: number, node: TrieNode): boolean => {
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
            if (!node.children.has(char)) {
                return false;
            }
            return dfs(index + 1, node.children.get(char)!);
        }
    };

    return dfs(0, this.root);
}
```

#### Collecting All Words
Get all words with a given prefix:
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

### 5. Space Optimization

#### Array vs Map for Children
```typescript
// Array-based (for fixed alphabet size)
class TrieNodeArray {
    children: (TrieNodeArray | null)[];
    isEndOfWord: boolean;

    constructor() {
        this.children = new Array(26).fill(null); // a-z only
        this.isEndOfWord = false;
    }
}

// Map-based (for variable alphabet)
class TrieNodeMap {
    children: Map<string, TrieNodeMap>;
    isEndOfWord: boolean;

    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}
```

**When to use which:**
- **Array:** Fixed, small alphabet (e.g., lowercase letters only)
- **Map:** Large or variable alphabet (e.g., Unicode characters)

### 6. Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(m) | O(m) |
| Search | O(m) | O(1) |
| StartsWith | O(p) | O(1) |
| Delete | O(m) | O(1) |
| Space (total) | - | O(ALPHABET_SIZE × N × M) |

Where:
- m = length of word
- p = length of prefix
- N = number of words
- M = average length of words

---

## TypeScript Implementation Tips

### 1. Use Proper Types
```typescript
interface ITrieNode {
    children: Map<string, ITrieNode>;
    isEndOfWord: boolean;
    count?: number; // For frequency tracking
    value?: any; // For storing additional data
}
```

### 2. Generic Trie Class
```typescript
class Trie<T = void> {
    private root: TrieNode<T>;

    constructor() {
        this.root = new TrieNode<T>();
    }

    // Methods...
}
```

### 3. Efficient Character Indexing
```typescript
// For lowercase letters only
private charToIndex(char: string): number {
    return char.charCodeAt(0) - 'a'.charCodeAt(0);
}
```

---

## Common Interview Patterns

### 1. Word Search in Grid
Combine Trie with backtracking for efficient word search.

### 2. Autocomplete System
Use Trie with frequency counts for ranking suggestions.

### 3. Replace Words
Use shortest prefix matching to replace words with roots.

### 4. Stream Processing
Maintain state while processing character stream.

### 5. Suffix Trees
Build reverse Trie for suffix-based operations.

---

## Practice Problems

Start with these in order:
1. **Implement Trie** - Basic operations
2. **Add and Search Words** - Wildcard matching
3. **Word Search II** - Trie + Backtracking
4. **Longest Word in Dictionary** - Building words incrementally
5. **Replace Words** - Prefix replacement

---

## Key Takeaways

1. **Tries excel at prefix operations** - Use when dealing with prefixes/autocomplete
2. **Space vs Time tradeoff** - Tries use more space but offer faster prefix operations
3. **Combine with other techniques** - Tries + DFS/BFS/Backtracking is powerful
4. **Consider alphabet size** - Affects implementation choice (Array vs Map)
5. **Practice implementation** - Trie problems often require custom implementation

---

## Next Steps

After understanding these concepts:
1. Implement a basic Trie from scratch
2. Solve the first 3 problems
3. Move to advanced problems with wildcards
4. Practice space optimization techniques

Remember: Tries are about **efficient string operations**, not just storage!