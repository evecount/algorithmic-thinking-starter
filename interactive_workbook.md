# Coding Nights 3.0: Night 1 — Interactive Student Workbook
> **Organized by:** NTU Women In Tech (WIT) & IEEE NTU Student Branch  
> **Lead Instructor:** Gwendalynn Lim Wan Ting (CTO & Systems Architect @ Eve Count Quantum Systems)  
> **Event Date:** Monday, October 12 | 18:00 – 21:00 SGT

---

## 🕒 Masterclass Schedule

| Time Slot | Segment | Core Focus & Objective |
| :--- | :--- | :--- |
| **18:00 – 18:40** | Registration & Dinner | Networking & environment setup |
| **18:40 – 18:50** | Welcome & Introduction | Community intros (WIT x IEEE) & Speaker introduction |
| **18:50 – 19:10** | Big-O Mental Models | Asymptotic growth rates, space-time currency exchange |
| **19:10 – 19:20** | Live Interactive Quiz | Kahoot complexity checkpoint & memory intuition |
| **19:20 – 19:50** | HashMaps & Sets ($O(1)$ Magic) | Direct access, Frequency Counters, and Complement Lookups |
| **19:50 – 20:30** | Two Pointers & Sliding Window | Converging pointers, Sliding windows, and In-place scans |
| **20:30 – 20:50** | Live Technical Interview Breakdown | 5-step problem deconstruction method & dry-run tracing |
| **20:50 – 21:00** | Q&A & Sustainable Practice | NeetCode 75 habit, pythontutor tracing, Night 2 preview |

---

## Part 1: Big-O Complexity Quick Reference

Big-O measures the mathematical rate of growth in operations as input size $n \to \infty$.

| Notation | Classification | Common Python Operations | Practical Rule |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Constant | `dict[k]`, `set.add()`, list index `arr[0]`, `len(arr)` | Immediate lookup |
| **$O(\log n)$** | Logarithmic | Binary search (`bisect`), halving search intervals | Scales to billions |
| **$O(n)$** | Linear | Single `for` loop, `min()`, `max()`, `x in list` | Golden standard |
| **$O(n \log n)$** | Linearithmic | Python Timsort (`sorted()` or `.sort()`), Merge Sort | Sorting ceiling |
| **$O(n^2)$** | Quadratic | Nested loops checking all pairs $(i, j)$ | Avoid for $n > 10^4$ |
| **$O(2^n)$** | Exponential | Naive recursive permutations and subsets | Prohibitive |

---

## Part 2: Pattern 1 — HashMaps & Sets ($O(1)$ Direct Access)

### Problem 1.1: Contains Duplicate
**Description:** Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

```python
def contains_duplicate(nums: list[int]) -> bool:
    # TODO: Implement single-pass check using a Hash Set for O(n) runtime
    pass

# Test Cases
print(contains_duplicate([1, 2, 3, 1]))  # Expected: True
print(contains_duplicate([1, 2, 3, 4]))  # Expected: False
```

<details>
<summary><b>View Optimized Solution</b></summary>

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time Complexity:  O(n)
# Space Complexity: O(n)
```
</details>

---

### Problem 1.2: Two Sum (The Universal Interview Benchmark)
**Description:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may not use the same element twice.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    # TODO: Implement single-pass complement lookup using a Hash Map
    pass

# Test Cases
print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(two_sum([3, 2, 4], 6))        # Expected: [1, 2]
```

<details>
<summary><b>View Optimized Solution & Trace</b></summary>

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    prev_map = {}  # value -> original index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in prev_map:
            return [prev_map[complement], i]
        prev_map[num] = i
    return []

# Time Complexity:  O(n)
# Space Complexity: O(n)
```

**State Trace (`nums = [3, 2, 4]`, `target = 6`):**
| Step | Index `i` | Num | Complement ($6 - \text{num}$) | Condition (`in prev_map`) | `prev_map` State | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 3 | 3 | False | `{3: 0}` | Store index |
| 2 | 1 | 2 | 4 | False | `{3: 0, 2: 1}` | Store index |
| 3 | 2 | 4 | 2 | **True!** | Matches index 1 | **Return `[1, 2]`** |
</details>

---

## Part 3: Pattern 2 — Two Pointers & Sliding Window

### Problem 2.1: Valid Palindrome (Inward Squeeze)
**Description:** A phrase is a palindrome if, after converting uppercase to lowercase and removing non-alphanumeric characters, it reads the same forward and backward. Implement in $O(1)$ auxiliary memory.

```python
def is_palindrome(s: str) -> bool:
    # TODO: Inward converging pointers without allocating auxiliary strings
    pass

# Test Cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(is_palindrome("race a car"))                      # Expected: False
```

<details>
<summary><b>View Optimized Solution</b></summary>

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Time Complexity:  O(n)
# Space Complexity: O(1)
```
</details>

---

### Problem 2.2: Longest Substring Without Repeats (Sliding Window)
**Description:** Given a string `s`, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    # TODO: Variable-size sliding window with a set boundary tracker
    pass

# Test Cases
print(length_of_longest_substring("abcabcbb"))  # Expected: 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # Expected: 1 ("b")
print(length_of_longest_substring("pwwkew"))    # Expected: 3 ("wke")
```

<details>
<summary><b>View Optimized Solution</b></summary>

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

# Time Complexity:  O(n)
# Space Complexity: O(min(n, m)) where m is character set size
```
</details>

---

### Problem 2.3: Two Sum II (Sorted Array — Directional Steering)
**Description:** Given a 1-indexed array of integers `numbers` that is **already sorted in non-decreasing order**, find two numbers that add up to `target`. Return `[index1 + 1, index2 + 1]`. Must use $O(1)$ extra space.

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    # TODO: Exploit sorted monotonicity with two pointers
    pass

# Test Cases
print(two_sum_sorted([2, 7, 11, 15], 9))  # Expected: [1, 2]
print(two_sum_sorted([2, 3, 4], 6))       # Expected: [1, 3]
```

<details>
<summary><b>View Optimized Solution</b></summary>

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1   # Need a larger sum
        else:
            right -= 1  # Need a smaller sum
    return []

# Time Complexity:  O(n)
# Space Complexity: O(1)
```
</details>

---

## Part 4: The 5-Step Technical Interview Deconstruction Framework

When given an unseen coding problem:
1. **Clarify Constraints & Boundaries:** Ask about negative numbers, duplicates, empty inputs, memory constraints, and expected output formats.
2. **State the Brute Force Solution:** Articulate the naive approach (e.g. $O(n^2)$ nested loops) and explain its computational bottleneck.
3. **Identify the Optimal Pattern:** Look for clues (Sorted $\to$ Two Pointers/Binary Search; Lookup $\to$ Hash Map; Contiguous $\to$ Sliding Window).
4. **Write Clean, Idiomatic Code:** Use descriptive variable names, write robust loop boundary guards, and avoid premature optimizations.
5. **Dry-Run with an Example:** Trace your code manually using a state table before declaring completion.
