# Lesson: Hash Maps

## 📹 Video Assignment (20 minutes)

**Primary Video:**
"Hash Table Data Structure - Intro" by NeetCode
https://www.youtube.com/watch?v=0M_urPuuC-E

**Alternative Videos** (if you need different explanations):
- "Hash Tables Explained" by CS Dojo (16 min): https://www.youtube.com/watch?v=shs0KM3wKv8
- "Hash Tables - Beau teaches JavaScript" by freeCodeCamp (8 min): https://www.youtube.com/watch?v=F95z5Wxd9ks

**What to focus on:**
- How hash functions work
- Collision resolution strategies
- Why O(1) average case
- When hash maps fail (worst case)

---

## 📚 Hash Maps - Core Concepts

### What is a Hash Map?

A hash map (hash table) is a data structure that implements an associative array, mapping keys to values. It uses a **hash function** to compute an index into an array of buckets.

**Key insight:** Trade space for time - use extra memory for lightning-fast lookups.

### How Hash Maps Work

```typescript
// Simplified hash map internals
class SimpleHashMap {
    private buckets: Array<[string, any][]>;

    constructor(size = 100) {
        this.buckets = new Array(size).fill(null).map(() => []);
    }

    private hash(key: string): number {
        let hash = 0;
        for (let char of key) {
            hash = (hash + char.charCodeAt(0)) % this.buckets.length;
        }
        return hash;
    }

    set(key: string, value: any): void {
        const index = this.hash(key);
        this.buckets[index].push([key, value]);
    }

    get(key: string): any {
        const index = this.hash(key);
        const bucket = this.buckets[index];
        for (let [k, v] of bucket) {
            if (k === key) return v;
        }
        return undefined;
    }
}
```

---

### TypeScript Hash Structures

#### 1. Map<K, V> - The Modern Choice

```typescript
// Creating and using Maps
const map = new Map<string, number>();

// Basic operations
map.set("apple", 5);        // Add/Update
map.get("apple");            // Retrieve (returns 5)
map.has("apple");            // Check existence (returns true)
map.delete("apple");         // Remove
map.size;                    // Get count
map.clear();                 // Remove all

// Iteration
for (let [key, value] of map) {
    console.log(key, value);
}

// Convert to/from arrays
const entries = Array.from(map);
const newMap = new Map(entries);
```

**When to use Map:**
- Need to preserve insertion order
- Keys are not just strings
- Frequent additions/deletions
- Need size property
- Need iteration capabilities

#### 2. Set<T> - Unique Values Only

```typescript
// Creating and using Sets
const set = new Set<number>();

// Basic operations
set.add(1);                  // Add element
set.has(1);                  // Check existence (returns true)
set.delete(1);               // Remove element
set.size;                    // Get count
set.clear();                 // Remove all

// Convert array to set (removes duplicates!)
const uniqueNumbers = new Set([1, 2, 2, 3, 3, 3]);
// uniqueNumbers = Set {1, 2, 3}

// Convert back to array
const array = Array.from(uniqueNumbers);
// or
const array2 = [...uniqueNumbers];
```

**When to use Set:**
- Need unique values only
- Quick membership testing
- Removing duplicates from arrays

#### 3. Object as Hash Map

```typescript
// Using objects as hash maps
const obj: { [key: string]: number } = {};

// Operations
obj["apple"] = 5;            // Add/Update
obj["apple"];                // Retrieve
"apple" in obj;              // Check existence
delete obj["apple"];         // Remove
Object.keys(obj).length;     // Get count (slower!)

// Iteration
for (let key in obj) {
    console.log(key, obj[key]);
}
```

**When to use Object:**
- Simple string keys
- JSON serialization needed
- Working with existing APIs
- Static configuration

---

## 🎯 Common Patterns

### Pattern 1: Frequency Counter

```typescript
function countFrequency(arr: number[]): Map<number, number> {
    const freq = new Map<number, number>();

    for (let num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    return freq;
}

// Example: [1, 2, 2, 3, 3, 3] => Map {1 => 1, 2 => 2, 3 => 3}
```

### Pattern 2: Two Sum Pattern

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

### Pattern 3: Grouping/Categorizing

```typescript
function groupBy<T>(arr: T[], keyFn: (item: T) => string): Map<string, T[]> {
    const groups = new Map<string, T[]>();

    for (let item of arr) {
        const key = keyFn(item);
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key)!.push(item);
    }

    return groups;
}

// Example: Group words by length
const words = ["cat", "dog", "bird", "fish"];
const byLength = groupBy(words, w => w.length.toString());
// Map {"3" => ["cat", "dog"], "4" => ["bird", "fish"]}
```

### Pattern 4: Anagram Detection

```typescript
function areAnagrams(s1: string, s2: string): boolean {
    if (s1.length !== s2.length) return false;

    const charCount = new Map<string, number>();

    // Count chars in s1
    for (let char of s1) {
        charCount.set(char, (charCount.get(char) || 0) + 1);
    }

    // Decrement for chars in s2
    for (let char of s2) {
        if (!charCount.has(char)) return false;
        charCount.set(char, charCount.get(char)! - 1);
        if (charCount.get(char)! < 0) return false;
    }

    return true;
}
```

### Pattern 5: Caching/Memoization

```typescript
function memoize<T, R>(fn: (arg: T) => R): (arg: T) => R {
    const cache = new Map<T, R>();

    return (arg: T): R => {
        if (cache.has(arg)) {
            return cache.get(arg)!;
        }

        const result = fn(arg);
        cache.set(arg, result);
        return result;
    };
}

// Example: Memoized fibonacci
const fib = memoize((n: number): number => {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
});
```

---

## ⚠️ Edge Cases to Consider

1. **Empty map/set operations**
```typescript
const map = new Map();
map.get("key");              // returns undefined
map.has("key");              // returns false
map.delete("key");           // returns false
```

2. **Undefined/null as keys**
```typescript
const map = new Map();
map.set(undefined, "value");  // Valid!
map.set(null, "value");       // Valid!
```

3. **Object keys (reference equality)**
```typescript
const map = new Map();
const obj1 = { id: 1 };
const obj2 = { id: 1 };

map.set(obj1, "value1");
map.get(obj1);                // "value1"
map.get(obj2);                // undefined (different reference!)
```

4. **NaN as key**
```typescript
const map = new Map();
map.set(NaN, "value");
map.get(NaN);                 // "value" (NaN is equal to itself in Map)
```

---

## 🔥 Performance Tips

### Do's:
- ✅ Use Map for frequent additions/deletions
- ✅ Use Set for unique value collections
- ✅ Pre-size maps when possible (performance hint)
- ✅ Use has() before get() when unsure
- ✅ Clear references to allow garbage collection

### Don'ts:
- ❌ Use Object.keys() for size (O(n))
- ❌ Mutate keys after insertion
- ❌ Use arrays for lookups (O(n) vs O(1))
- ❌ Forget about worst-case O(n) scenarios
- ❌ Use complex objects as keys carelessly

---

## 💡 Interview Tips

1. **Start with clarifying questions:**
   - Can I use extra space? (Usually yes for hash maps)
   - Are keys unique?
   - What should I return if not found?

2. **Verbalize your approach:**
   - "I'll use a hash map for O(1) lookups..."
   - "The space complexity will be O(n)..."
   - "This avoids the O(n²) nested loop approach..."

3. **Consider alternatives:**
   - Sometimes sorting + two pointers is better
   - For small datasets, arrays might be simpler
   - Consider memory constraints

4. **Common follow-ups:**
   - "How would you handle collisions?"
   - "What if we can't use extra space?"
   - "How does this scale to distributed systems?"

---

## 🎓 Quick Quiz

Test your understanding:

1. What's the average time complexity for hash map insertion?
2. When would you use Set instead of Map?
3. How do hash maps handle collisions?
4. Why is Map better than Object for non-string keys?
5. What's the space complexity of frequency counting?

Answers:
1. O(1) average case
2. When you only need unique values, not key-value pairs
3. Chaining (linked lists) or open addressing (probing)
4. Map accepts any type as key, Object coerces to string
5. O(k) where k is the number of unique elements

---

**Ready to practice?** Head to PROBLEMS.md to start solving!