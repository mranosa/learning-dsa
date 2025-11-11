# Solutions: Tries

## Problem 1: Implement Trie (Prefix Tree)

### Approach 1: Map-based Children
```typescript
class TrieNode {
    children: Map<string, TrieNode>;
    isEndOfWord: boolean;

    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}

class Trie {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

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
**Time:** O(m) for all operations where m is word/prefix length
**Space:** O(ALPHABET_SIZE × N × M) where N is number of words, M is average length

### Approach 2: Array-based Children (Memory Optimized)
```typescript
class TrieNode {
    children: (TrieNode | null)[];
    isEndOfWord: boolean;

    constructor() {
        this.children = new Array(26).fill(null);
        this.isEndOfWord = false;
    }
}

class Trie {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    private charToIndex(char: string): number {
        return char.charCodeAt(0) - 'a'.charCodeAt(0);
    }

    insert(word: string): void {
        let node = this.root;
        for (const char of word) {
            const index = this.charToIndex(char);
            if (!node.children[index]) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index]!;
        }
        node.isEndOfWord = true;
    }

    search(word: string): boolean {
        let node = this.root;
        for (const char of word) {
            const index = this.charToIndex(char);
            if (!node.children[index]) {
                return false;
            }
            node = node.children[index]!;
        }
        return node.isEndOfWord;
    }

    startsWith(prefix: string): boolean {
        let node = this.root;
        for (const char of prefix) {
            const index = this.charToIndex(char);
            if (!node.children[index]) {
                return false;
            }
            node = node.children[index]!;
        }
        return true;
    }
}
```
**Time:** O(m) for all operations
**Space:** O(26 × N × M) - more predictable memory usage

---

## Problem 2: Design Add and Search Words Data Structure

### Approach: DFS with Wildcard Support
```typescript
class TrieNode {
    children: Map<string, TrieNode>;
    isEndOfWord: boolean;

    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}

class WordDictionary {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    addWord(word: string): void {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isEndOfWord = true;
    }

    search(word: string): boolean {
        return this.searchHelper(word, 0, this.root);
    }

    private searchHelper(word: string, index: number, node: TrieNode): boolean {
        // Base case: reached end of word
        if (index === word.length) {
            return node.isEndOfWord;
        }

        const char = word[index];

        if (char === '.') {
            // Wildcard: try all possible children
            for (const child of node.children.values()) {
                if (this.searchHelper(word, index + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            // Regular character
            if (!node.children.has(char)) {
                return false;
            }
            return this.searchHelper(word, index + 1, node.children.get(char)!);
        }
    }
}
```
**Time:** O(m) for addWord, O(m × 26^k) for search where k is number of dots
**Space:** O(TOTAL_CHARS) for all stored words

---

## Problem 3: Word Search II

### Approach: Trie + Backtracking with Pruning
```typescript
class TrieNode {
    children: Map<string, TrieNode>;
    word: string | null;

    constructor() {
        this.children = new Map();
        this.word = null;
    }
}

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
        node.word = word;
    }

    const result: string[] = [];
    const m = board.length;
    const n = board[0].length;

    const dfs = (i: number, j: number, node: TrieNode): void => {
        // Check bounds and if character exists in trie
        if (i < 0 || i >= m || j < 0 || j >= n) return;

        const char = board[i][j];
        if (char === '#' || !node.children.has(char)) return;

        node = node.children.get(char)!;

        // Found a word
        if (node.word !== null) {
            result.push(node.word);
            node.word = null; // Avoid duplicates
        }

        // Mark as visited
        board[i][j] = '#';

        // Explore all 4 directions
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
**Time:** O(m × n × 4^L) where L is max word length
**Space:** O(TOTAL_CHARS) for Trie + O(L) for recursion

---

## Problem 4: Longest Word in Dictionary

### Approach: Trie with Layer-by-Layer Building
```typescript
function longestWord(words: string[]): string {
    class TrieNode {
        children: Map<string, TrieNode> = new Map();
        isEndOfWord: boolean = false;
    }

    const root = new TrieNode();
    root.isEndOfWord = true; // Empty string is valid

    // Build Trie
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isEndOfWord = true;
    }

    let longestWord = "";

    // DFS to find longest buildable word
    const dfs = (node: TrieNode, path: string): void => {
        // Update longest if current is longer or lexicographically smaller
        if (path.length > longestWord.length ||
            (path.length === longestWord.length && path < longestWord)) {
            longestWord = path;
        }

        // Continue only if we can build further
        for (const [char, child] of node.children) {
            if (child.isEndOfWord) {
                dfs(child, path + char);
            }
        }
    };

    dfs(root, "");
    return longestWord;
}
```
**Time:** O(N × M) where N is number of words, M is average length
**Space:** O(TOTAL_CHARS) for Trie

---

## Problem 5: Replace Words

### Approach: Trie for Efficient Prefix Search
```typescript
function replaceWords(dictionary: string[], sentence: string): string {
    class TrieNode {
        children: Map<string, TrieNode> = new Map();
        isRoot: boolean = false;
    }

    const root = new TrieNode();

    // Build Trie from dictionary
    for (const word of dictionary) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isRoot = true;
    }

    // Find shortest root for a word
    const findRoot = (word: string): string => {
        let node = root;
        let prefix = "";

        for (const char of word) {
            if (!node.children.has(char)) {
                return word; // No root found
            }
            prefix += char;
            node = node.children.get(char)!;

            if (node.isRoot) {
                return prefix; // Found shortest root
            }
        }
        return word;
    };

    // Process sentence
    const words = sentence.split(' ');
    const replaced = words.map(word => findRoot(word));
    return replaced.join(' ');
}
```
**Time:** O(D × M + S) where D is dictionary size, M is avg word length, S is sentence length
**Space:** O(D × M) for Trie

---

## Problem 6: Implement Magic Dictionary

### Approach: Trie with Fuzzy Search
```typescript
class MagicDictionary {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    buildDict(dictionary: string[]): void {
        for (const word of dictionary) {
            let node = this.root;
            for (const char of word) {
                if (!node.children.has(char)) {
                    node.children.set(char, new TrieNode());
                }
                node = node.children.get(char)!;
            }
            node.isEndOfWord = true;
        }
    }

    search(searchWord: string): boolean {
        return this.searchHelper(searchWord, 0, this.root, false);
    }

    private searchHelper(word: string, index: number, node: TrieNode, changed: boolean): boolean {
        if (index === word.length) {
            return node.isEndOfWord && changed;
        }

        const char = word[index];

        // Try exact match
        if (node.children.has(char)) {
            if (this.searchHelper(word, index + 1, node.children.get(char)!, changed)) {
                return true;
            }
        }

        // Try changing current character if not changed yet
        if (!changed) {
            for (const [childChar, child] of node.children) {
                if (childChar !== char) {
                    if (this.searchHelper(word, index + 1, child, true)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}

class TrieNode {
    children: Map<string, TrieNode> = new Map();
    isEndOfWord: boolean = false;
}
```
**Time:** O(N × M) for buildDict, O(M × 26) for search
**Space:** O(TOTAL_CHARS) for Trie

---

## Problem 7: Prefix and Suffix Search

### Approach: Combined Trie with Special Separator
```typescript
class WordFilter {
    private trie: TrieNode;

    constructor(words: string[]) {
        this.trie = new TrieNode();

        for (let weight = 0; weight < words.length; weight++) {
            const word = words[weight];
            // Insert all suffix#prefix combinations
            for (let i = 0; i <= word.length; i++) {
                const combined = word.substring(i) + '#' + word;
                let node = this.trie;

                for (const char of combined) {
                    if (!node.children.has(char)) {
                        node.children.set(char, new TrieNode());
                    }
                    node = node.children.get(char)!;
                    node.weight = weight; // Update to latest weight
                }
            }
        }
    }

    f(prefix: string, suffix: string): number {
        const searchWord = suffix + '#' + prefix;
        let node = this.trie;

        for (const char of searchWord) {
            if (!node.children.has(char)) {
                return -1;
            }
            node = node.children.get(char)!;
        }

        return node.weight;
    }
}

class TrieNode {
    children: Map<string, TrieNode> = new Map();
    weight: number = -1;
}
```
**Time:** O(N × L^2) for construction, O(P + S) for query
**Space:** O(N × L^2) where L is max word length

---

## Problem 8: Word Squares

### Approach: Trie with Prefix Search + Backtracking
```typescript
function wordSquares(words: string[]): string[][] {
    class TrieNode {
        children: Map<string, TrieNode> = new Map();
        words: string[] = [];
    }

    const n = words[0].length;
    const root = new TrieNode();

    // Build Trie with words at each prefix
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
            node.words.push(word);
        }
    }

    // Get words with given prefix
    const getWordsWithPrefix = (prefix: string): string[] => {
        let node = root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return [];
            }
            node = node.children.get(char)!;
        }
        return node.words;
    };

    const result: string[][] = [];

    const backtrack = (square: string[]): void => {
        if (square.length === n) {
            result.push([...square]);
            return;
        }

        const row = square.length;
        let prefix = "";

        // Build prefix from previous rows
        for (let i = 0; i < row; i++) {
            prefix += square[i][row];
        }

        // Try all words with this prefix
        for (const word of getWordsWithPrefix(prefix)) {
            square.push(word);
            backtrack(square);
            square.pop();
        }
    };

    // Try each word as the first word
    for (const word of words) {
        backtrack([word]);
    }

    return result;
}
```
**Time:** O(N × 26^L × L) where N is number of words, L is word length
**Space:** O(N × L) for Trie + O(L) for recursion

---

## Problem 9: Concatenated Words

### Approach: Trie + Dynamic Programming
```typescript
function findAllConcatenatedWordsInADict(words: string[]): string[] {
    class TrieNode {
        children: Map<string, TrieNode> = new Map();
        isEndOfWord: boolean = false;
    }

    const root = new TrieNode();

    // Build Trie
    for (const word of words) {
        if (word.length === 0) continue;
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isEndOfWord = true;
    }

    // Check if word can be formed by concatenation
    const isConcatenated = (word: string): boolean => {
        if (word.length === 0) return false;

        const dp = new Array(word.length + 1).fill(false);
        dp[0] = true;

        for (let i = 1; i <= word.length; i++) {
            let node = root;
            for (let j = i - 1; j >= 0; j--) {
                if (!node.children.has(word[j])) break;
                node = node.children.get(word[j])!;

                if (node.isEndOfWord && dp[j]) {
                    // Don't count the word itself
                    if (j === 0 && i === word.length) continue;
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[word.length];
    };

    return words.filter(word => isConcatenated(word));
}
```
**Time:** O(N × M^2) where N is number of words, M is max word length
**Space:** O(TOTAL_CHARS) for Trie + O(M) for DP

---

## Problem 10: Stream of Characters

### Approach: Reverse Trie for Suffix Matching
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

class TrieNode {
    children: Map<string, TrieNode> = new Map();
    isEndOfWord: boolean = false;
}
```
**Time:** O(M) for query where M is max word length
**Space:** O(TOTAL_CHARS) for Trie + O(M) for stream buffer