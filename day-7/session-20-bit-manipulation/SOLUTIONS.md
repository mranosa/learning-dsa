# Solutions: Bit Manipulation

## Problem 1: Single Number

### Approach 1: XOR Operation
**Time:** O(n) | **Space:** O(1)

```typescript
function singleNumber(nums: number[]): number {
    let result = 0;
    for (const num of nums) {
        result ^= num;
    }
    return result;
}

// One-liner using reduce
function singleNumberReduce(nums: number[]): number {
    return nums.reduce((acc, num) => acc ^ num, 0);
}
```

**Explanation:**
- XOR properties: a^a=0, a^0=a, commutative and associative
- All duplicate numbers cancel out: a^b^a = a^a^b = 0^b = b
- The single number remains after all XOR operations

### Approach 2: Mathematical (Alternative)
**Time:** O(n) | **Space:** O(n)

```typescript
function singleNumberMath(nums: number[]): number {
    const uniqueNums = new Set(nums);
    const sumUnique = Array.from(uniqueNums).reduce((a, b) => a + b, 0);
    const sumAll = nums.reduce((a, b) => a + b, 0);
    return 2 * sumUnique - sumAll;
}
```

---

## Problem 2: Number of 1 Bits

### Approach 1: Brian Kernighan's Algorithm
**Time:** O(k) where k is number of set bits | **Space:** O(1)

```typescript
function hammingWeight(n: number): number {
    let count = 0;
    while (n !== 0) {
        n &= (n - 1); // Remove rightmost set bit
        count++;
    }
    return count;
}
```

**Explanation:**
- n & (n-1) removes the rightmost set bit
- Loops only k times where k is the number of 1s

### Approach 2: Bit Checking
**Time:** O(32) | **Space:** O(1)

```typescript
function hammingWeightBitCheck(n: number): number {
    let count = 0;
    for (let i = 0; i < 32; i++) {
        if ((n >> i) & 1) {
            count++;
        }
    }
    return count;
}
```

### Approach 3: Using Built-in
**Time:** O(32) | **Space:** O(1)

```typescript
function hammingWeightBuiltin(n: number): number {
    return n.toString(2).split('1').length - 1;
}
```

---

## Problem 3: Counting Bits

### Approach 1: Dynamic Programming with Last Bit
**Time:** O(n) | **Space:** O(n)

```typescript
function countBits(n: number): number[] {
    const result: number[] = new Array(n + 1).fill(0);

    for (let i = 1; i <= n; i++) {
        // i >> 1 removes last bit, i & 1 checks if last bit is 1
        result[i] = result[i >> 1] + (i & 1);
    }

    return result;
}
```

**Explanation:**
- For any number i, count of 1s = count of 1s in i/2 + last bit
- i >> 1 is equivalent to Math.floor(i/2)
- i & 1 checks if the last bit is 1

### Approach 2: Dynamic Programming with Last Set Bit
**Time:** O(n) | **Space:** O(n)

```typescript
function countBitsLastSet(n: number): number[] {
    const result: number[] = new Array(n + 1).fill(0);

    for (let i = 1; i <= n; i++) {
        // i & (i-1) removes last set bit
        result[i] = result[i & (i - 1)] + 1;
    }

    return result;
}
```

### Approach 3: Offset Pattern
**Time:** O(n) | **Space:** O(n)

```typescript
function countBitsOffset(n: number): number[] {
    const result: number[] = new Array(n + 1).fill(0);
    let offset = 1;

    for (let i = 1; i <= n; i++) {
        if (offset * 2 === i) {
            offset = i;
        }
        result[i] = result[i - offset] + 1;
    }

    return result;
}
```

---

## Problem 4: Reverse Bits

### Approach 1: Bit by Bit
**Time:** O(32) | **Space:** O(1)

```typescript
function reverseBits(n: number): number {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        // Get the last bit of n
        const bit = n & 1;
        // Shift result left and add the bit
        result = (result << 1) | bit;
        // Shift n right to process next bit
        n >>>= 1; // Use >>> for unsigned shift
    }

    return result >>> 0; // Ensure unsigned result
}
```

### Approach 2: Divide and Conquer
**Time:** O(log 32) = O(1) | **Space:** O(1)

```typescript
function reverseBitsDivideConquer(n: number): number {
    // Swap 16-bit blocks
    n = ((n & 0xffff0000) >>> 16) | ((n & 0x0000ffff) << 16);
    // Swap 8-bit blocks
    n = ((n & 0xff00ff00) >>> 8) | ((n & 0x00ff00ff) << 8);
    // Swap 4-bit blocks
    n = ((n & 0xf0f0f0f0) >>> 4) | ((n & 0x0f0f0f0f) << 4);
    // Swap 2-bit blocks
    n = ((n & 0xcccccccc) >>> 2) | ((n & 0x33333333) << 2);
    // Swap 1-bit blocks
    n = ((n & 0xaaaaaaaa) >>> 1) | ((n & 0x55555555) << 1);

    return n >>> 0;
}
```

---

## Problem 5: Missing Number

### Approach 1: XOR
**Time:** O(n) | **Space:** O(1)

```typescript
function missingNumber(nums: number[]): number {
    let xor = nums.length; // Start with n

    for (let i = 0; i < nums.length; i++) {
        xor ^= i ^ nums[i];
    }

    return xor;
}
```

**Explanation:**
- XOR all indices [0...n] with all numbers in array
- All present numbers cancel out, missing number remains

### Approach 2: Sum Formula
**Time:** O(n) | **Space:** O(1)

```typescript
function missingNumberSum(nums: number[]): number {
    const n = nums.length;
    const expectedSum = (n * (n + 1)) / 2;
    const actualSum = nums.reduce((a, b) => a + b, 0);
    return expectedSum - actualSum;
}
```

### Approach 3: Bit Manipulation Alternative
**Time:** O(n) | **Space:** O(1)

```typescript
function missingNumberBit(nums: number[]): number {
    const n = nums.length;
    let missing = n;

    for (let i = 0; i < n; i++) {
        missing = missing ^ i ^ nums[i];
    }

    return missing;
}
```

---

## Problem 6: Sum of Two Integers

### Approach 1: Bit Manipulation with Carry
**Time:** O(32) | **Space:** O(1)

```typescript
function getSum(a: number, b: number): number {
    while (b !== 0) {
        // Calculate carry (AND then shift left)
        const carry = (a & b) << 1;
        // Add without carry using XOR
        a = a ^ b;
        // Set b to carry for next iteration
        b = carry;
    }
    return a;
}
```

**Explanation:**
- XOR gives sum without carry: 1^1=0, 1^0=1, 0^0=0
- AND gives carry positions: 1&1=1 (carry), others=0
- Shift carry left by 1 to add in next position
- Repeat until no carry

### Approach 2: Recursive Version
**Time:** O(32) | **Space:** O(32)

```typescript
function getSumRecursive(a: number, b: number): number {
    if (b === 0) return a;
    return getSumRecursive(a ^ b, (a & b) << 1);
}
```

---

## Problem 7: Single Number II

### Approach 1: Bit by Bit Counting
**Time:** O(32n) | **Space:** O(1)

```typescript
function singleNumberII(nums: number[]): number {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        let count = 0;
        for (const num of nums) {
            count += (num >> i) & 1;
        }
        // If count % 3 != 0, the single number has a 1 at this bit
        if (count % 3 !== 0) {
            result |= (1 << i);
        }
    }

    return result;
}
```

### Approach 2: State Machine with Ones and Twos
**Time:** O(n) | **Space:** O(1)

```typescript
function singleNumberIIStateMachine(nums: number[]): number {
    let ones = 0, twos = 0;

    for (const num of nums) {
        // Add to twos if already in ones
        twos |= ones & num;
        // XOR with ones
        ones ^= num;
        // Remove from ones and twos if in both
        const threes = ones & twos;
        ones &= ~threes;
        twos &= ~threes;
    }

    return ones;
}
```

---

## Problem 8: Single Number III

### Approach: XOR with Bit Masking
**Time:** O(n) | **Space:** O(1)

```typescript
function singleNumberIII(nums: number[]): number[] {
    // XOR all numbers to get xor of two unique numbers
    let xor = 0;
    for (const num of nums) {
        xor ^= num;
    }

    // Find rightmost set bit (where the two numbers differ)
    const rightmostBit = xor & -xor;

    // Divide numbers into two groups and XOR each
    let num1 = 0, num2 = 0;
    for (const num of nums) {
        if (num & rightmostBit) {
            num1 ^= num;
        } else {
            num2 ^= num;
        }
    }

    return [num1, num2];
}
```

**Explanation:**
- First XOR gives a^b where a and b are the two unique numbers
- rightmostBit finds a bit where a and b differ
- Divide array into two groups based on this bit
- Each group contains one unique number and pairs

---

## Problem 9: Bitwise AND of Numbers Range

### Approach 1: Common Prefix
**Time:** O(32) | **Space:** O(1)

```typescript
function rangeBitwiseAnd(left: number, right: number): number {
    let shift = 0;

    // Find common prefix
    while (left !== right) {
        left >>= 1;
        right >>= 1;
        shift++;
    }

    // Shift back to get the result
    return left << shift;
}
```

**Explanation:**
- Numbers in range differ in lower bits
- AND of differing bits is always 0
- Find common prefix (higher bits that don't change)

### Approach 2: Brian Kernighan's Algorithm
**Time:** O(32) | **Space:** O(1)

```typescript
function rangeBitwiseAndKernighan(left: number, right: number): number {
    while (right > left) {
        right &= (right - 1); // Remove rightmost set bit
    }
    return right;
}
```

---

## Problem 10: Maximum XOR of Two Numbers

### Approach 1: Bit Prefix with HashSet
**Time:** O(32n) | **Space:** O(n)

```typescript
function findMaximumXOR(nums: number[]): number {
    let maxXor = 0;
    let prefixMask = 0;

    for (let i = 31; i >= 0; i--) {
        // Update prefix mask
        prefixMask |= (1 << i);

        // Get all prefixes with current mask
        const prefixes = new Set<number>();
        for (const num of nums) {
            prefixes.add(num & prefixMask);
        }

        // Try to update maxXor
        const candidate = maxXor | (1 << i);
        for (const prefix of prefixes) {
            if (prefixes.has(candidate ^ prefix)) {
                maxXor = candidate;
                break;
            }
        }
    }

    return maxXor;
}
```

### Approach 2: Trie-based Solution
**Time:** O(32n) | **Space:** O(32n)

```typescript
class TrieNode {
    children: (TrieNode | null)[] = [null, null];
}

function findMaximumXORTrie(nums: number[]): number {
    const root = new TrieNode();

    // Build trie
    for (const num of nums) {
        let node = root;
        for (let i = 31; i >= 0; i--) {
            const bit = (num >> i) & 1;
            if (!node.children[bit]) {
                node.children[bit] = new TrieNode();
            }
            node = node.children[bit]!;
        }
    }

    // Find max XOR
    let maxXor = 0;
    for (const num of nums) {
        let node = root;
        let currentXor = 0;

        for (let i = 31; i >= 0; i--) {
            const bit = (num >> i) & 1;
            // Try to go opposite direction for max XOR
            const toggledBit = 1 - bit;

            if (node.children[toggledBit]) {
                currentXor |= (1 << i);
                node = node.children[toggledBit]!;
            } else {
                node = node.children[bit]!;
            }
        }

        maxXor = Math.max(maxXor, currentXor);
    }

    return maxXor;
}
```

---

## Key Takeaways

1. **XOR is powerful** for finding unique elements
2. **Brian Kernighan's algorithm** efficiently counts/manipulates bits
3. **Bit masking** helps isolate specific bits
4. **Common prefix** approach works for range problems
5. **Trie structure** optimizes bit-based searches
6. **State machines** can track complex bit patterns

Remember: Most bit manipulation problems have elegant solutions using basic operations!