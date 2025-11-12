# Hints: Tries

## Problem 1: Implement Trie (Prefix Tree)

### Hint 1 (Gentle)
Think about how each node in the Trie should store its children. What data structure allows efficient lookup by character?

### Hint 2 (Direct)
Use a Map to store children where the key is the character and the value is the child TrieNode. Don't forget the isEndOfWord flag to mark complete words.

### Hint 3 (Detailed)
```typescript
class TrieNode {
    children: Map<string, TrieNode>;
    isEndOfWord: boolean;
}
// Insert: traverse and create nodes as needed
// Search: traverse and check isEndOfWord at the end
// StartsWith: just traverse, don't check isEndOfWord
```

---

## Problem 2: Design Add and Search Words Data Structure

### Hint 1 (Gentle)
The '.' character is a wildcard. When you encounter it during search, what should you do differently than with a regular character?

### Hint 2 (Direct)
Use DFS/recursion for search. When you hit a '.', try all possible children at that position. For regular characters, proceed normally.

### Hint 3 (Detailed)
```typescript
searchHelper(word, index, node): boolean {
    if (index === word.length) return node.isEndOfWord;

    if (word[index] === '.') {
        // Try all children
        for (const child of node.children.values()) {
            if (searchHelper(word, index + 1, child)) return true;
        }
        return false;
    } else {
        // Normal character search
        if (!node.children.has(word[index])) return false;
        return searchHelper(word, index + 1, node.children.get(word[index]));
    }
}
```

---

## Problem 3: Word Search II

### Hint 1 (Gentle)
Combine Trie with backtracking. Build a Trie from all words first, then use DFS on the board while simultaneously traversing the Trie.

### Hint 2 (Direct)
Store complete words at Trie nodes (node.word) instead of just isEndOfWord. During DFS, when you reach a node with a word, add it to results. Mark cells as visited using '#'.

### Hint 3 (Detailed)
```typescript
// Build Trie with node.word = fullWord at endpoints
// DFS function:
dfs(i, j, node) {
    if (out of bounds || board[i][j] === '#') return;
    if (!node.children.has(board[i][j])) return;

    node = node.children.get(board[i][j]);
    if (node.word) {
        result.push(node.word);
        node.word = null; // Avoid duplicates
    }

    const temp = board[i][j];
    board[i][j] = '#'; // Mark visited
    // Recurse in 4 directions
    board[i][j] = temp; // Restore
}
```

---

## Problem 4: Longest Word in Dictionary

### Hint 1 (Gentle)
A word can be built "one character at a time" means every prefix of the word must also exist in the dictionary.

### Hint 2 (Direct)
Build a Trie and mark all words. Then DFS from root, only continuing to children that are marked as complete words. Track the longest valid path.

### Hint 3 (Detailed)
```typescript
dfs(node, path): void {
    // Update longest if needed (consider lexicographical order)
    if (path.length > longest.length ||
        (path.length === longest.length && path < longest)) {
        longest = path;
    }

    for (const [char, child] of node.children) {
        if (child.isEndOfWord) {  // Can only continue if this forms a word
            dfs(child, path + char);
        }
    }
}
```

---

## Problem 5: Replace Words

### Hint 1 (Gentle)
Build a Trie of roots. For each word in the sentence, find the shortest root that matches its prefix.

### Hint 2 (Direct)
When searching for a root, traverse the Trie character by character. As soon as you find a node marked as end of word, return that prefix as the root.

### Hint 3 (Detailed)
```typescript
findRoot(word): string {
    let node = root;
    let prefix = "";

    for (const char of word) {
        if (!node.children.has(char)) return word; // No root found
        prefix += char;
        node = node.children.get(char);
        if (node.isRoot) return prefix; // Found shortest root
    }
    return word; // No root found
}
```

---

## Problem 6: Implement Magic Dictionary

### Hint 1 (Gentle)
You need to find if changing exactly one character creates a valid word. Track whether you've made your one change during the search.

### Hint 2 (Direct)
Use a recursive search with a boolean flag indicating whether you've used your one allowed change. Try both exact match and changing the current character.

### Hint 3 (Detailed)
```typescript
searchHelper(word, index, node, changed): boolean {
    if (index === word.length) return node.isEndOfWord && changed;

    const char = word[index];

    // Try exact match
    if (node.children.has(char)) {
        if (searchHelper(word, index + 1, node.children.get(char), changed)) {
            return true;
        }
    }

    // Try changing if haven't changed yet
    if (!changed) {
        for (const [childChar, child] of node.children) {
            if (childChar !== char) {
                if (searchHelper(word, index + 1, child, true)) {
                    return true;
                }
            }
        }
    }

    return false;
}
```

---

## Problem 7: Prefix and Suffix Search

### Hint 1 (Gentle)
Think about combining suffix and prefix into a single searchable pattern. What separator could you use that won't appear in normal words?

### Hint 2 (Direct)
For each word, insert all combinations of "suffix#prefix" into the Trie. For "apple": insert "apple#apple", "pple#apple", "ple#apple", etc.

### Hint 3 (Detailed)
```typescript
// During construction:
for (let i = 0; i <= word.length; i++) {
    const combined = word.substring(i) + '#' + word;
    // Insert combined into Trie, storing weight at each node
    let node = root;
    for (const char of combined) {
        if (!node.children.has(char)) {
            node.children.set(char, new TrieNode());
        }
        node = node.children.get(char);
        node.weight = currentIndex; // Update to latest weight
    }
}

// For query:
// Search for suffix + '#' + prefix in Trie
```

---

## Problem 8: Word Squares

### Hint 1 (Gentle)
In a word square, row[i] = column[i]. When building row k, the prefix is determined by the characters at position k in all previous rows.

### Hint 2 (Direct)
Build a Trie that stores all words at each prefix node. Use backtracking to build the square row by row, where each new row must start with a specific prefix.

### Hint 3 (Detailed)
```typescript
// Store words at each prefix node during Trie construction
class TrieNode {
    children: Map<string, TrieNode>;
    words: string[] = []; // All words with this prefix
}

// During backtracking:
backtrack(square) {
    if (square.length === n) {
        result.push([...square]);
        return;
    }

    // Get prefix for next row
    let prefix = "";
    for (let i = 0; i < square.length; i++) {
        prefix += square[i][square.length];
    }

    // Find all words with this prefix and try each
    const candidates = getWordsWithPrefix(prefix);
    for (const word of candidates) {
        square.push(word);
        backtrack(square);
        square.pop();
    }
}
```

---

## Problem 9: Concatenated Words

### Hint 1 (Gentle)
A concatenated word can be broken into at least two other words from the array. Think about checking all possible split points.

### Hint 2 (Direct)
Use dynamic programming with a Trie. dp[i] = true if word[0...i-1] can be formed by concatenation. Check all possible last words ending at position i.

### Hint 3 (Detailed)
```typescript
isConcatenated(word): boolean {
    const dp = new Array(word.length + 1).fill(false);
    dp[0] = true;

    for (let i = 1; i <= word.length; i++) {
        // Try all possible last words ending at i
        let node = root;
        for (let j = i - 1; j >= 0; j--) {
            if (!node.children.has(word[j])) break;
            node = node.children.get(word[j]);

            if (node.isEndOfWord && dp[j]) {
                // Skip if it's the word itself (need at least 2 words)
                if (!(j === 0 && i === word.length)) {
                    dp[i] = true;
                    break;
                }
            }
        }
    }

    return dp[word.length];
}
```

---

## Problem 10: Stream of Characters

### Hint 1 (Gentle)
You need to check if any suffix of the stream matches a word. What if you stored words in reverse in the Trie?

### Hint 2 (Direct)
Build a reverse Trie (insert words backward). Keep a buffer of recent characters. For each query, traverse the Trie backward through the buffer.

### Hint 3 (Detailed)
```typescript
constructor(words) {
    // Build Trie with reversed words
    for (const word of words) {
        let node = root;
        // Insert word backward: "abc" -> "cba"
        for (let i = word.length - 1; i >= 0; i--) {
            const char = word[i];
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        node.isEndOfWord = true;
    }
    this.maxLength = Math.max(...words.map(w => w.length));
}

query(letter) {
    this.stream.push(letter);

    // Keep stream size limited
    if (this.stream.length > this.maxLength) {
        this.stream.shift();
    }

    // Traverse from end of stream backward
    let node = root;
    for (let i = this.stream.length - 1; i >= 0; i--) {
        if (!node.children.has(this.stream[i])) return false;
        node = node.children.get(this.stream[i]);
        if (node.isEndOfWord) return true;
    }

    return false;
}
```
