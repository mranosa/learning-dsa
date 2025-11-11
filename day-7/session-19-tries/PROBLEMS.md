# Practice Problems: Tries

## Problem 1: Implement Trie (Prefix Tree)
**Difficulty:** Medium
**LeetCode:** [208. Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)

Implement a trie with `insert`, `search`, and `startsWith` methods.

### Example:
```typescript
const trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
```

### Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters
- At most 3 * 10^4 calls will be made to insert, search, and startsWith

---

## Problem 2: Design Add and Search Words Data Structure
**Difficulty:** Medium
**LeetCode:** [211. Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:
- `void addWord(word)` Adds word to the data structure
- `boolean search(word)` Returns true if there is any string matching word, where '.' can match any letter

### Example:
```typescript
const wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad");  // returns false
wordDictionary.search("bad");  // returns true
wordDictionary.search(".ad");  // returns true
wordDictionary.search("b..");  // returns true
```

### Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters
- word in search consists of '.' or lowercase English letters
- At most 10^4 calls will be made to addWord and search

---

## Problem 3: Word Search II
**Difficulty:** Hard
**LeetCode:** [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

Given an m × n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

### Example:
```typescript
const board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
];
const words = ["oath","pea","eat","rain"];
findWords(board, words); // ["eat","oath"]
```

### Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- All strings in words are unique

---

## Problem 4: Longest Word in Dictionary
**Difficulty:** Medium
**LeetCode:** [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)

Given an array of strings words, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

### Example:
```typescript
const words = ["w","wo","wor","worl","world"];
longestWord(words); // "world"

const words2 = ["a","banana","app","appl","ap","apply","apple"];
longestWord(words2); // "apple"
```

### Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 30
- words[i] consists of lowercase English letters

---

## Problem 5: Replace Words
**Difficulty:** Medium
**LeetCode:** [648. Replace Words](https://leetcode.com/problems/replace-words/)

You have a dictionary of root words and a sentence. Replace all successors in the sentence with their roots.

A successor is a word that has a root as its prefix. If a successor has many roots, replace it with the root that has the shortest length.

### Example:
```typescript
const dictionary = ["cat","bat","rat"];
const sentence = "the cattle was rattled by the battery";
replaceWords(dictionary, sentence);
// "the cat was rat by the bat"
```

### Constraints:
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lowercase letters
- 1 <= sentence.length <= 10^6
- sentence consists of only lowercase letters and spaces
- Number of words in sentence is in range [1, 1000]
- Length of each word in sentence is in range [1, 1000]

---

## Problem 6: Implement Magic Dictionary
**Difficulty:** Medium
**LeetCode:** [676. Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

Design a data structure that is initialized with a list of different words. Search if you can change exactly one character in the search word to match any word in the dictionary.

### Example:
```typescript
const magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "hallo", "leetcode"]);
magicDictionary.search("hello");   // false (exact match, need to change 1 char)
magicDictionary.search("hhllo");   // true (change 2nd 'h' to 'e' or 'a')
magicDictionary.search("hell");    // false (different length)
magicDictionary.search("leetcoded"); // false (different length)
```

### Constraints:
- 1 <= dictionary.length <= 100
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lowercase English letters
- All strings in dictionary are unique
- 1 <= searchWord.length <= 100
- searchWord consists of only lowercase English letters
- At most 100 calls will be made to search

---

## Problem 7: Prefix and Suffix Search
**Difficulty:** Hard
**LeetCode:** [745. Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

Design a special data structure that searches for words with given prefix and suffix efficiently.

Implement the WordFilter class:
- `WordFilter(string[] words)` Initializes with an array of words
- `int f(string prefix, string suffix)` Returns the index of the word that has both prefix and suffix. If multiple valid answers, return the largest index. If no such word, return -1.

### Example:
```typescript
const wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e");  // returns 0
// "apple" has prefix "a" and suffix "e"
```

### Constraints:
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 7
- 1 <= prefix.length, suffix.length <= 7
- words[i], prefix and suffix consist of lowercase English letters only
- At most 10^4 calls will be made to f

---

## Problem 8: Word Squares
**Difficulty:** Hard
**LeetCode:** [425. Word Squares](https://leetcode.com/problems/word-squares/)

Given an array of unique strings words, return all the word squares you can build from words. You can use each word at most once.

A word square is a sequence of words where the kth row and column read the same string.

### Example:
```typescript
const words = ["area","lead","wall","lady","ball"];
wordSquares(words);
// [
//   ["ball","area","lead","lady"],
//   ["wall","area","lead","lady"]
// ]
// Explanation:
// b a l l
// a r e a
// l e a d
// l a d y
```

### Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 5
- All words have the same length
- words[i] consists of only lowercase English letters
- All words are unique

---

## Problem 9: Concatenated Words
**Difficulty:** Hard
**LeetCode:** [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/)

Given an array of strings words, return all the concatenated words in words.

A concatenated word is a string that is comprised entirely of at least two other words in words.

### Example:
```typescript
const words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"];
findAllConcatenatedWordsInADict(words);
// ["catsdogcats","dogcatsdog","ratcatdogcat"]
// "catsdogcats" can be formed by "cats", "dog", "cats"
// "dogcatsdog" can be formed by "dog", "cats", "dog"
// "ratcatdogcat" can be formed by "rat", "cat", "dog", "cat"
```

### Constraints:
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 30
- words[i] consists of only lowercase English letters
- All strings in words are unique

---

## Problem 10: Stream of Characters
**Difficulty:** Hard
**LeetCode:** [1032. Stream of Characters](https://leetcode.com/problems/stream-of-characters/)

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string from a given array of strings.

Implement the StreamChecker class:
- `StreamChecker(string[] words)` Initializes with the given words
- `boolean query(char letter)` Accepts a new character from the stream and returns true if any non-empty suffix is a word

### Example:
```typescript
const streamChecker = new StreamChecker(["cd","f","kl"]);
streamChecker.query('a'); // false
streamChecker.query('b'); // false
streamChecker.query('c'); // false
streamChecker.query('d'); // true, "cd" is a suffix
streamChecker.query('e'); // false
streamChecker.query('f'); // true, "f" is a suffix
streamChecker.query('g'); // false
streamChecker.query('h'); // false
streamChecker.query('i'); // false
streamChecker.query('j'); // false
streamChecker.query('k'); // false
streamChecker.query('l'); // true, "kl" is a suffix
```

### Constraints:
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 200
- words[i] consists of lowercase English letters
- letter is a lowercase English letter
- At most 4 * 10^4 calls will be made to query