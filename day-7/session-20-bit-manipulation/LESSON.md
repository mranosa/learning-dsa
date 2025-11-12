# Lesson: Bit Manipulation

---

## 📹 Video 1: Binary & Bitwise Operators (15 min)

**"Bit Manipulation Tutorial" by NeetCode**
https://www.youtube.com/watch?v=5rtVTYAk9KQ

**Focus on:**
- Binary number system basics
- All bitwise operators (AND, OR, XOR, NOT)
- Bit shifting (left, right, unsigned)
- Two's complement for negatives

---

## 📹 Video 2: XOR Properties & Applications (12 min)

**"XOR - The Most Magical Operator" by Reducible**
https://www.youtube.com/watch?v=_GJLzz3j7Jg

**Alternative - NeetCode XOR:**
https://www.youtube.com/watch?v=qMPX1AOa83k

**Focus on:**
- XOR truth table and properties
- Finding unique elements
- XOR for swapping
- Cancellation patterns

---

## 📹 Video 3: Bit Manipulation Patterns (20 min)

**"Bit Manipulation Tricks" by Back To Back SWE**
https://www.youtube.com/results?search_query=back+to+back+swe+bit+manipulation

**Search "NeetCode bit manipulation" or "William Fiset bit manipulation" on YouTube**

**Focus on:**
- n & (n-1) trick
- Isolating rightmost set bit
- Brian Kernighan's algorithm
- Bit masking techniques

---

## 🎯 Binary Number System

### Decimal to Binary Conversion

```typescript
// 13 in decimal = 1101 in binary
// Position: 2³  2²  2¹  2⁰
// Value:    8 + 4 + 0 + 1 = 13

// Manual conversion
function toBinary(n: number): string {
  if (n === 0) return "0";
  let binary = "";
  while (n > 0) {
    binary = (n % 2) + binary;
    n = Math.floor(n / 2);
  }
  return binary;
}

// Built-in conversion
const binary = (13).toString(2);  // "1101"
const decimal = parseInt("1101", 2);  // 13
```

### Two's Complement (Negative Numbers)

```typescript
// -5 in 8-bit binary
// Step 1: Binary of 5 = 00000101
// Step 2: Invert bits  = 11111010
// Step 3: Add 1        = 11111011

// JavaScript uses 32-bit signed integers
const negative = -5;
console.log((negative >>> 0).toString(2));  // 32-bit representation
```

---

## 🔧 Bitwise Operators

### AND (&) - Both bits must be 1

```typescript
// 5 & 3 = 1
//   0101  (5)
// & 0011  (3)
// ------
//   0001  (1)

const result = 5 & 3;  // 1
```

**Use cases:**
- Check if bit is set: `(n & (1 << i)) !== 0`
- Extract specific bits (masking)
- Check if even: `(n & 1) === 0`

---

### OR (|) - At least one bit must be 1

```typescript
// 5 | 3 = 7
//   0101  (5)
// | 0011  (3)
// ------
//   0111  (7)

const result = 5 | 3;  // 7
```

**Use cases:**
- Set specific bit: `n | (1 << i)`
- Combine bit flags
- Build masks

---

### XOR (^) - Bits must be different

```typescript
// 5 ^ 3 = 6
//   0101  (5)
// ^ 0011  (3)
// ------
//   0110  (6)

const result = 5 ^ 3;  // 6
```

**Use cases:**
- Find unique element
- Toggle bit: `n ^ (1 << i)`
- Swap without temp: `a ^= b; b ^= a; a ^= b;`

---

### NOT (~) - Flip all bits

```typescript
// ~5 = -6 (in two's complement)
// ~00000101 = 11111010 (which is -6)

const result = ~5;  // -6
```

**Use cases:**
- Create inverse mask: `~(1 << i)`
- Clear bit with AND: `n & ~(1 << i)`

---

### Left Shift (<<) - Multiply by 2^n

```typescript
// 5 << 1 = 10
// 0101 << 1 = 1010

const result = 5 << 1;  // 10
const result2 = 5 << 2;  // 20 (5 * 4)
```

**Use cases:**
- Fast multiplication by power of 2
- Create bit mask: `1 << i`
- Build bit patterns

---

### Right Shift (>>) - Divide by 2^n (signed)

```typescript
// 5 >> 1 = 2
// 0101 >> 1 = 0010

const result = 5 >> 1;  // 2

// Negative numbers preserve sign
const negResult = -5 >> 1;  // -3 (not -2!)
```

---

### Unsigned Right Shift (>>>) - Fills with zeros

```typescript
// 5 >>> 1 = 2
// -5 >>> 1 = 2147483645

const result = 5 >>> 1;  // 2
const negResult = -5 >>> 1;  // 2147483645
```

**Use cases:**
- Divide positive numbers
- Handle unsigned operations
- Ensure positive result

---

## 🎯 XOR Properties (CRITICAL!)

### Property 1: Identity
```typescript
a ^ 0 = a  // XOR with 0 returns original
```

### Property 2: Self-Inverse
```typescript
a ^ a = 0  // XOR with itself returns 0
```

### Property 3: Commutative
```typescript
a ^ b = b ^ a  // Order doesn't matter
```

### Property 4: Associative
```typescript
(a ^ b) ^ c = a ^ (b ^ c)  // Grouping doesn't matter
```

### Finding Unique Element

```typescript
// Array where all elements appear twice except one
function singleNumber(nums: number[]): number {
  // All pairs cancel out: a^a = 0
  // 0^unique = unique
  return nums.reduce((acc, num) => acc ^ num, 0);
}

// Example: [1,2,1,2,3]
// 1^2^1^2^3 = (1^1)^(2^2)^3 = 0^0^3 = 3
```

---

## 🧩 Common Bit Tricks

### 1. Check if Power of 2

**📹 Learn:** Search "NeetCode power of 2" on YouTube (~5 min)

```typescript
function isPowerOfTwo(n: number): boolean {
  return n > 0 && (n & (n - 1)) === 0;
}

// Why it works:
// Power of 2:  8 = 1000, 7 = 0111, 8 & 7 = 0000
// Not power:   6 = 0110, 5 = 0101, 6 & 5 = 0100
```

**Time:** O(1) | **Space:** O(1)

---

### 2. Count Set Bits (Brian Kernighan's)

**📹 Learn:** Search "Brian Kernighan algorithm" on YouTube (~8 min)

```typescript
function countSetBits(n: number): number {
  let count = 0;
  while (n > 0) {
    n &= (n - 1);  // Remove rightmost set bit
    count++;
  }
  return count;
}

// Example: 13 = 1101
// Step 1: 1101 & 1100 = 1100 (count = 1)
// Step 2: 1100 & 1011 = 1000 (count = 2)
// Step 3: 1000 & 0111 = 0000 (count = 3)
```

**Time:** O(k) where k = number of set bits | **Space:** O(1)

**Key:** Only loops for each set bit, not all 32 bits!

---

### 3. Get i-th Bit

```typescript
function getBit(n: number, i: number): number {
  return (n >> i) & 1;
}

// Example: Get 2nd bit of 13 (1101)
// 1101 >> 2 = 0011
// 0011 & 1 = 1
```

---

### 4. Set i-th Bit

```typescript
function setBit(n: number, i: number): number {
  return n | (1 << i);
}

// Example: Set 1st bit of 5 (0101)
// 1 << 1 = 0010
// 0101 | 0010 = 0111 (7)
```

---

### 5. Clear i-th Bit

```typescript
function clearBit(n: number, i: number): number {
  return n & ~(1 << i);
}

// Example: Clear 2nd bit of 7 (0111)
// 1 << 2 = 0100
// ~0100 = 1011
// 0111 & 1011 = 0011 (3)
```

---

### 6. Toggle i-th Bit

```typescript
function toggleBit(n: number, i: number): number {
  return n ^ (1 << i);
}

// Example: Toggle 1st bit of 5 (0101)
// 1 << 1 = 0010
// 0101 ^ 0010 = 0111 (7)
```

---

### 7. Isolate Rightmost Set Bit

```typescript
function rightmostSetBit(n: number): number {
  return n & -n;
}

// Example: 12 = 1100
// -12 in two's complement = 0100
// 1100 & 0100 = 0100 (4)
```

---

## 🧩 Problem-Solving Patterns

### Pattern 1: XOR for Unique Elements

**📹 Learn:** Search "NeetCode single number" on YouTube (~10 min)

```typescript
// Problem: All elements appear twice except one
function singleNumber(nums: number[]): number {
  return nums.reduce((acc, num) => acc ^ num, 0);
}
```

**When to use:** Finding unique elements, cancellation patterns

**Time:** O(n) | **Space:** O(1)

---

### Pattern 2: Bit Masking

**📹 Learn:** Search "bit masking tutorial" on YouTube (~12 min)

```typescript
// Using bits as flags
const READ = 1 << 0;     // 001
const WRITE = 1 << 1;    // 010
const EXECUTE = 1 << 2;  // 100

let permissions = 0;

// Add permission
permissions |= READ;     // Set bit
permissions |= WRITE;

// Check permission
if (permissions & READ) {
  console.log("Has READ");
}

// Remove permission
permissions &= ~WRITE;   // Clear bit
```

**When to use:** Flags, permissions, state tracking

---

### Pattern 3: Bit Counting with DP

```typescript
function countBits(n: number): number[] {
  const result: number[] = new Array(n + 1);
  result[0] = 0;

  for (let i = 1; i <= n; i++) {
    // i >> 1 removes last bit
    // i & 1 checks if last bit is 1
    result[i] = result[i >> 1] + (i & 1);
  }

  return result;
}
```

**Key insight:** Count of i = count of i/2 + last bit

**Time:** O(n) | **Space:** O(n)

---

### Pattern 4: Addition Without Arithmetic

```typescript
function add(a: number, b: number): number {
  while (b !== 0) {
    const carry = (a & b) << 1;  // Calculate carry
    a = a ^ b;                    // Add without carry
    b = carry;                    // Set carry for next iteration
  }
  return a;
}

// Example: 5 + 3
// a=0101, b=0011
// carry = (0101 & 0011) << 1 = 0001 << 1 = 0010
// a = 0101 ^ 0011 = 0110
// b = 0010
// Next iteration...
```

**When to use:** Arithmetic without +/- operators

---

## 💡 TypeScript/JavaScript Specifics

### 32-bit Integer Limits

```typescript
// JavaScript uses 32-bit signed integers for bitwise ops
const MAX_INT = 2147483647;   // 2^31 - 1
const MIN_INT = -2147483648;  // -2^31

// Beyond this, precision may be lost
const large = 1 << 31;  // Overflows to negative!
```

---

### Unsigned vs Signed Shift

```typescript
// Signed right shift (>>)
-5 >> 1;   // -3 (preserves sign)

// Unsigned right shift (>>>)
-5 >>> 1;  // 2147483645 (fills with 0)

// Always use >>> for unsigned operations
function reverseBits(n: number): number {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    result = (result << 1) | (n & 1);
    n >>>= 1;  // Use >>> not >>
  }
  return result >>> 0;  // Ensure unsigned
}
```

---

### Ensure Positive Result

```typescript
// Use >>> 0 to ensure 32-bit unsigned integer
const n = -1;
const unsigned = n >>> 0;  // 4294967295
```

---

## 💡 Interview Tips

### Complexity Analysis

**Quick rules:**
- Single bit operation → O(1)
- Loop through bits → O(32) = O(1) for fixed-size integers
- XOR all elements → O(n)
- Brian Kernighan → O(k) where k = set bits

**Say this:**
- "Using XOR gives O(n) time and O(1) space since pairs cancel out."
- "Brian Kernighan only loops k times where k is number of set bits."
- "Bit masking reduces space from O(n) boolean array to O(1) integer."

---

### When to Use Bit Manipulation

| Problem Type | Pattern | Example |
|--------------|---------|---------|
| Find unique element | XOR | Single Number |
| Check parity/power of 2 | n & (n-1) | Power of Two |
| Count set bits | Brian Kernighan | Hamming Weight |
| Toggle/Set/Clear bit | Masking | Bit operations |
| Space optimization | Bit flags | Permission systems |
| Arithmetic without +/- | XOR + AND | Sum of Two Integers |

---

### TypeScript Gotchas

```typescript
// ❌ Wrong - logical operators
if (a && b)  // Boolean AND, not bitwise

// ✅ Correct - bitwise operators
if (a & b)   // Bitwise AND

// ❌ Wrong - signed shift on unsigned data
const result = n >> 1;  // May give negative

// ✅ Correct - unsigned shift
const result = n >>> 1;  // Always positive

// ❌ Wrong - operator precedence
if (n & 1 === 0)  // Parses as: n & (1 === 0)

// ✅ Correct - use parentheses
if ((n & 1) === 0)  // Check if even
```

---

## ✅ Ready to Practice

**Say:** `"Claude, I watched the videos"` for concept check!

**Quick Reference:**
- **XOR properties:** a^a=0, a^0=a, commutative, associative
- **Remove rightmost set bit:** n & (n-1)
- **Isolate rightmost set bit:** n & -n
- **Check power of 2:** n > 0 && (n & (n-1)) === 0
- **Count set bits:** Brian Kernighan's algorithm
- **Use >>> for unsigned:** Always for bit reversal/unsigned ops

---

## 🔗 Additional Resources

**Essential bit tricks:**
- https://graphics.stanford.edu/~seander/bithacks.html

**Video playlists:**
- Search "NeetCode bit manipulation" for problem walkthroughs
- Search "Back To Back SWE bit" for detailed explanations
- Search "William Fiset bit manipulation" for advanced topics

---

[Back to Session README](./README.md)
