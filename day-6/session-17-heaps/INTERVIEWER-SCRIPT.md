# Interviewer Script: Heaps & Priority Queues

## Introduction (2 min)
"Welcome! Today we'll explore heap and priority queue problems. These data structures are crucial for efficiently handling priority-based operations and K-element problems. Let's start by checking your understanding of heap fundamentals."

---

## Concept Check (5 min)

### Question 1: Heap Properties
"Can you explain what makes a heap different from a regular binary tree?"

**Expected Answer:**
- Complete binary tree (all levels filled except possibly last)
- Heap property: parent-child relationship (max or min)
- Efficient array representation
- O(log n) insert/extract operations

### Question 2: Time Complexity
"What's the time complexity of building a heap from an array? Why?"

**Expected Answer:**
- O(n) using bottom-up heapify
- NOT O(n log n) despite n insertions
- Bottom-up processes nodes level by level
- Most nodes are near leaves with small bubble-down distance

### Question 3: When to Use Heaps
"When would you choose a heap over sorting?"

**Expected Answer:**
- K-element problems where K << n
- Streaming data (online algorithms)
- Need to maintain dynamic priority
- Space constraints (O(k) vs O(n))

**Scoring:**
- 3/3: Comprehensive understanding with examples
- 2/3: Good grasp but missing nuances
- 1/3: Basic understanding only
- 0/3: Significant gaps in knowledge

---

## Problem Selection

Based on performance, assign problems:

### Strong Performance (3/3)
Start with Problem 3: Find Median from Data Stream

### Good Performance (2/3)
Start with Problem 2: Top K Frequent Elements

### Needs Review (0-1/3)
Start with Problem 1: Kth Largest Element

---

## Problem 1: Kth Largest Element (15 min)

### Initial Presentation
"Given an unsorted array and a number k, find the kth largest element."

### Clarifying Questions to Expect:
- "Can I modify the input array?" → Yes
- "Are there duplicates?" → Yes, possible
- "Is k always valid?" → Yes, 1 <= k <= array length
- "What about negative numbers?" → Yes, possible

### Solution Approach:

#### If they use sorting:
"That works! Time complexity is O(n log n). Can we do better for small k?"

#### If they mention heap:
"Excellent! Walk me through your heap approach."

#### If stuck:
"What if we only needed to track k elements at any time?"

### Expected Solution:
```typescript
function findKthLargest(nums: number[], k: number): number {
    // Min heap of size k
    const minHeap = new MinHeap();

    for (const num of nums) {
        minHeap.push(num);
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    return minHeap.peek();
}
```

### Follow-up Questions:
1. "What's the space-time trade-off here?"
2. "How would QuickSelect compare?"
3. "What if k is very large (close to n)?"

**Time Expectation:** 10-15 minutes

---

## Problem 2: Top K Frequent Elements (15 min)

### Initial Presentation
"Given an array of integers, return the k most frequent elements."

### Key Insights to Guide:
- Two-phase problem: count then select
- Frequency map first
- Then heap or bucket sort

### If they struggle with counting:
"First step is to know the frequency of each element. How would you do that?"

### If they sort all frequencies:
"That's O(n log n). Since we only need k elements, can we optimize?"

### Expected Approach:
```typescript
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map();
    // Count frequencies

    // Min heap of size k by frequency
    const minHeap = new MinHeap((a, b) => freq.get(a) - freq.get(b));

    for (const [num, _] of freq) {
        minHeap.push(num);
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    return minHeap.toArray();
}
```

### Alternative to discuss:
"Have you heard of bucket sort? How could that apply here?"

---

## Problem 3: Find Median from Data Stream (20 min)

### Initial Presentation
"Design a class that can add numbers and find the median at any point."

### Guiding Questions:
1. "How would you find median in a sorted array?"
2. "Can we maintain sorted order efficiently?"
3. "What if we split the data into two halves?"

### Key Insight to Provide:
"Think about maintaining the smaller half and larger half separately."

### Expected Pattern Recognition:
- Two heaps: max heap for smaller half, min heap for larger half
- Balance the heaps
- Median from heap tops

### Implementation Focus:
```typescript
class MedianFinder {
    private maxHeap: MaxHeap; // smaller half
    private minHeap: MinHeap; // larger half

    addNum(num: number): void {
        // Add to appropriate heap
        // Balance heaps
        // Maintain invariant
    }

    findMedian(): number {
        // Check heap sizes
        // Return median
    }
}
```

### Edge Cases to Test:
- Single element
- Two elements
- Even vs odd count
- All same values

---

## Problem Complexity Analysis

For each problem, ensure they analyze:

### Time Complexity:
- Heap operations: O(log n) or O(log k)
- Building heap: O(n) with heapify
- Overall complexity

### Space Complexity:
- Heap storage: O(k) or O(n)
- Additional structures

### Trade-offs:
- Heap vs sorting
- Space vs time
- Online vs offline algorithms

---

## Common Mistakes to Address

### Heap Property Violations:
"Let's trace through your bubble-up. Is the heap property maintained?"

### Wrong Heap Type:
"You're using a max heap for k smallest. Think about what stays in the heap."

### Size Management:
"Your heap grows unbounded. How can we maintain size k?"

### Index Calculations:
"Check your parent/child index formulas for off-by-one errors."

---

## Hints Progression

### Level 1 (Gentle):
- "What data structure maintains priority efficiently?"
- "Think about the pattern - we need k elements"
- "Consider processing elements one at a time"

### Level 2 (Direct):
- "Try using a heap of size k"
- "For median, think about two heaps"
- "Min heap for k largest, max heap for k smallest"

### Level 3 (Detailed):
- "Walk through the heap operations step by step"
- "Draw the heap structure"
- "Show the array representation"

---

## Behavioral Questions

### Question 1:
"Tell me about a time you optimized an algorithm's performance."

Look for:
- Problem identification
- Solution approach
- Measurement/validation
- Trade-off consideration

### Question 2:
"How do you decide between different data structures?"

Look for:
- Requirements analysis
- Complexity awareness
- Practical considerations
- Real-world constraints

---

## Closing (3 min)

### Summary Points:
1. Heap mastery demonstrated
2. Problem-solving approach
3. Complexity analysis
4. Code quality

### Feedback Structure:
- "You excelled at [specific strength]"
- "Consider improving [specific area]"
- "For next time, practice [specific skill]"

### Final Question:
"Do you have any questions about heaps or the problems we discussed?"

---

## Evaluation Rubric

### Technical Skills (60%):
- Heap implementation: 20%
- Algorithm design: 20%
- Complexity analysis: 10%
- Code correctness: 10%

### Problem Solving (25%):
- Pattern recognition: 10%
- Edge case handling: 10%
- Optimization: 5%

### Communication (15%):
- Clarity: 5%
- Questioning: 5%
- Collaboration: 5%

### Overall Rating:
- **Strong Hire**: 85%+ with exceptional heap understanding
- **Hire**: 70-84% with solid fundamentals
- **Maybe**: 55-69% with potential but gaps
- **No Hire**: <55% significant knowledge gaps

---

## Additional Evaluation Scenarios

### Scenario 1: Candidate Struggles with Implementation
If the candidate struggles with heap implementation:
- Suggest using a simplified approach first
- Allow them to use sorting as a baseline
- Guide them toward the heap solution gradually
- Focus on understanding over perfect implementation

### Scenario 2: Candidate Finishes Early
If time permits after main problems:
- Ask about heap variations (binomial, Fibonacci)
- Discuss real-world applications
- Present a system design scenario using heaps
- Challenge with optimization questions

### Scenario 3: Candidate Uses Library
If candidate uses built-in heap/priority queue:
- Ask them to implement key operations
- Discuss the underlying implementation
- Compare library vs custom implementation trade-offs
- Test understanding of complexity

---

## Post-Interview Debrief Template

### Strengths Observed:
- Problem-solving approach
- Code quality and style
- Communication clarity
- Algorithm knowledge
- Debugging skills

### Areas for Improvement:
- Specific technical gaps
- Problem-solving speed
- Edge case consideration
- Complexity analysis
- Code organization

### Recommended Next Steps:
1. Practice areas identified
2. Resources to review
3. Similar problems to solve
4. Concepts to deepen

---

## Interview Calibration Guide

### Strong Hire Indicators:
- Implements heap correctly from scratch
- Recognizes patterns quickly
- Optimizes without prompting
- Handles edge cases naturally
- Explains clearly throughout

### Hire Indicators:
- Understands heap concepts well
- Solves problems with minor hints
- Good complexity analysis
- Clean, readable code
- Learns from feedback quickly

### Maybe Indicators:
- Basic understanding present
- Needs significant hints
- Makes progress but slowly
- Some confusion on complexity
- Potential shown but gaps exist

### No Hire Indicators:
- Cannot explain heap properties
- Struggles with basic operations
- Poor problem-solving approach
- Unable to debug errors
- Lacks fundamental knowledge

---

## Notes for Interviewer

### Maintain Objectivity:
- Use consistent rubric
- Document specific examples
- Avoid bias in questioning
- Give equal opportunity to all

### Create Safe Environment:
- Encourage questions
- Provide positive feedback
- Allow thinking time
- Reduce interview stress

### Calibrate Difficulty:
- Adjust based on experience level
- Consider role requirements
- Factor in interview nerves
- Balance challenge and achievability

---

**Interview Duration:** 45-60 minutes
**Problems Covered:** 2-3 depending on pace
**Focus:** Heap operations and K-element patterns