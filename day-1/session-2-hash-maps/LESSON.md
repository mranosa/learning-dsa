# Lesson: Hash Maps

---

## 📹 Video 1: Hash Map Fundamentals (20 min)

**"Hash Tables - Beau teaches JavaScript" by freeCodeCamp**
https://www.youtube.com/watch?v=F95z5Wxd9ks

**Alternative:**
"Hash Table Data Structure" by NeetCode (10 min): https://www.youtube.com/watch?v=0M_urPuuC-E

**Focus on:**
- How hash functions work
- Collision resolution (chaining, open addressing)
- Why O(1) average case
- When worst case O(n) happens

---

## 📹 Video 2: Hash Map Patterns (15 min)

**"Two Sum - Hash Map" by NeetCode**
https://www.youtube.com/watch?v=KLlXCFG5TnA

**Also watch:**
"Group Anagrams Explained" by NeetCode (8 min): https://www.youtube.com/watch?v=vzdNOK2oB2E

**Focus on:**
- Two Sum pattern
- Frequency counting
- Grouping with hash maps
- When to use Map vs Set

---

## 🎯 Hash Maps: Creation & Syntax

### Creating Hash Maps

```typescript
// Map - key-value pairs, any type
const map = new Map<string, number>();
const numMap = new Map<number, string>();
const objMap = new Map<object, any>();

// Set - unique values only
const set = new Set<number>();
const strSet = new Set<string>();

// Initialize with values
const map2 = new Map([["a", 1], ["b", 2]]);
const set2 = new Set([1, 2, 3, 2]);  // {1, 2, 3}

// Object as hash map (legacy)
const obj: { [key: string]: number } = {};
```

---

## 🔧 TypeScript Map Functions

### Core Functions (Must Know)

| Function | Description | Example | Time |
|----------|-------------|---------|------|
| `set(k, v)` | Add/update key-value | `map.set("a", 1)` | O(1) |
| `get(k)` | Retrieve value | `map.get("a")` | O(1) |
| `has(k)` | Check key exists | `map.has("a")` | O(1) |
| `delete(k)` | Remove key-value | `map.delete("a")` | O(1) |
| `size` | Get count | `map.size` | O(1) |
| `clear()` | Remove all | `map.clear()` | O(n) |

```typescript
const map = new Map<string, number>();

// Basic operations
map.set("apple", 5);        // Add
map.set("apple", 10);       // Update (overwrites)
map.get("apple");           // 10
map.has("apple");           // true
map.delete("apple");        // true (returns boolean)
map.size;                   // 0
```

---

### Iteration Functions

| Function | Description | Returns | Time |
|----------|-------------|---------|------|
| `keys()` | Get all keys | Iterator | O(n) |
| `values()` | Get all values | Iterator | O(n) |
| `entries()` | Get key-value pairs | Iterator | O(n) |
| `forEach(fn)` | Execute function on each | undefined | O(n) |

```typescript
const map = new Map([["a", 1], ["b", 2], ["c", 3]]);

// Iteration
for (let [key, value] of map) {
  console.log(key, value);
}

for (let key of map.keys()) {
  console.log(key);
}

for (let value of map.values()) {
  console.log(value);
}

map.forEach((value, key) => {
  console.log(key, value);
});

// Convert to array
const entries = Array.from(map);           // [["a",1],["b",2],["c",3]]
const keys = [...map.keys()];              // ["a","b","c"]
const values = [...map.values()];          // [1, 2, 3]
```

---

## 🔧 TypeScript Set Functions

### Core Functions

| Function | Description | Example | Time |
|----------|-------------|---------|------|
| `add(v)` | Add value | `set.add(1)` | O(1) |
| `has(v)` | Check exists | `set.has(1)` | O(1) |
| `delete(v)` | Remove value | `set.delete(1)` | O(1) |
| `size` | Get count | `set.size` | O(1) |
| `clear()` | Remove all | `set.clear()` | O(n) |

```typescript
const set = new Set<number>();

// Basic operations
set.add(1);                 // {1}
set.add(2);                 // {1, 2}
set.add(1);                 // {1, 2} (no duplicates)
set.has(1);                 // true
set.delete(1);              // true
set.size;                   // 1

// Remove duplicates from array
const arr = [1, 2, 2, 3, 3, 3];
const unique = [...new Set(arr)];  // [1, 2, 3]

// Iteration
for (let value of set) {
  console.log(value);
}
```

---

## 📊 Big O Notation for Hash Maps

### What is a Hash Map?

Hash maps provide O(1) lookups by trading space for time.

**Key concept:** Hash function converts keys to array indices for direct access.

---

### Complexity Table

| Operation | Average | Worst Case | Notes |
|-----------|---------|------------|-------|
| **Insert** | O(1) | O(n) | Worst: all keys collide |
| **Lookup** | O(1) | O(n) | Worst: linear scan chain |
| **Delete** | O(1) | O(n) | Worst: all keys collide |
| **Space** | O(n) | O(n) | n = number of elements |

**Examples:**

```typescript
// O(1) - Insert
map.set("key", value);

// O(1) - Lookup
map.get("key");

// O(1) - Delete
map.delete("key");

// O(n) - Iteration
for (let [key, value] of map) {
  console.log(key, value);
}
```

---

### Why O(1)?

**Hash function:** Key → Index → Direct access

```
Hash("apple") = 42 → bucket[42]
Hash("banana") = 17 → bucket[17]
```

**Collision resolution:**
- **Chaining:** Linked list at each bucket
- **Open addressing:** Probe next slots

**Say this:** "Hash maps trade O(n) space for O(1) time. Instead of scanning every element, we compute an index directly."

---

## 🧩 Common Hash Map Patterns

### Pattern 1: Frequency Counting

**📹 Learn:** Search "NeetCode top k frequent elements" on YouTube (~10 min)

Used when: Count occurrences, find duplicates, most/least frequent.

```typescript
function countFrequency(arr: number[]): Map<number, number> {
  const freq = new Map<number, number>();

  for (let num of arr) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  return freq;
}

// Example: [1, 2, 2, 3, 3, 3]
// Result: Map {1 => 1, 2 => 2, 3 => 3}
```

**Time:** O(n) | **Space:** O(k) where k = unique elements

---

### Pattern 2: Two Sum Pattern

**📹 Learn:** [Two Sum Hash Map](https://www.youtube.com/watch?v=KLlXCFG5TnA) by NeetCode (~9 min)

Used when: Find pairs, complements, target sums.

```typescript
function twoSum(nums: number[], target: number): number[] {
  const seen = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) {
      return [seen.get(complement)!, i];
    }
    seen.set(nums[i], i);
  }

  return [];
}
```

**Key insight:** Store value→index, check complement before adding current.

**Time:** O(n) | **Space:** O(n)

---

### Pattern 3: Anagram Detection

**📹 Learn:** Search "NeetCode valid anagram" on YouTube (~8 min)

Used when: Compare character frequencies, group anagrams.

```typescript
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const charCount = new Map<string, number>();

  for (let char of s) {
    charCount.set(char, (charCount.get(char) || 0) + 1);
  }

  for (let char of t) {
    if (!charCount.has(char)) return false;
    const count = charCount.get(char)! - 1;
    if (count < 0) return false;
    if (count === 0) {
      charCount.delete(char);
    } else {
      charCount.set(char, count);
    }
  }

  return charCount.size === 0;
}
```

**Key insight:** Count chars in first string, decrement for second.

**Time:** O(n) | **Space:** O(k) where k = unique chars

---

### Pattern 4: Grouping/Categorizing

**📹 Learn:** Search "NeetCode group anagrams" on YouTube (~8 min)

Used when: Group by property, categorize elements.

```typescript
function groupAnagrams(strs: string[]): string[][] {
  const groups = new Map<string, string[]>();

  for (let str of strs) {
    // Use sorted string as key
    const key = str.split('').sort().join('');

    if (!groups.has(key)) {
      groups.set(key, []);
    }
    groups.get(key)!.push(str);
  }

  return Array.from(groups.values());
}
```

**Key insight:** Anagrams have identical sorted strings.

**Time:** O(n × k log k) where n = strings, k = max length | **Space:** O(n × k)

---

## 💡 Interview Tips

### Map vs Object vs Set

**Use Map when:**
- Keys are not strings
- Need insertion order
- Frequent add/delete
- Need size property

**Use Object when:**
- Simple string keys
- JSON serialization needed
- Static configuration

**Use Set when:**
- Only need unique values
- Membership testing
- Remove duplicates

**Say this:**
```typescript
// ❌ Wrong - Object coerces keys to strings
const obj = {};
obj[1] = "one";     // Actually obj["1"] = "one"

// ✅ Correct - Map preserves key types
const map = new Map();
map.set(1, "one");  // Key is number 1
```

---

### TypeScript Gotchas

```typescript
// ❌ Wrong - get() can return undefined
const value = map.get(key).toUpperCase();  // Error if key doesn't exist

// ✅ Correct - check first
if (map.has(key)) {
  const value = map.get(key)!.toUpperCase();
}

// ✅ Or provide default
const value = map.get(key) || "default";

// ❌ Wrong - using includes() on array
if (arr.includes(target)) { }  // O(n)

// ✅ Correct - use Set
const set = new Set(arr);
if (set.has(target)) { }        // O(1)
```

---

### Frequency Counting Template

```typescript
// Template for frequency counting
function frequencyPattern<T>(arr: T[]): Map<T, number> {
  const freq = new Map<T, number>();

  for (let item of arr) {
    freq.set(item, (freq.get(item) || 0) + 1);
  }

  return freq;
}
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **Hash map insert/lookup:** O(1) average
- **Worst case (collisions):** O(n)
- **Frequency counting:** `map.set(key, (map.get(key) || 0) + 1)`
- **Two Sum:** Store complement, check before adding
- **Space:** O(n) for n elements

---

[Back to Session README](./README.md)
