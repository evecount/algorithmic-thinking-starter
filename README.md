<p align="center">
  <img src="./NTU%20DSA%20Event%20Banner.png" alt="NTU Coding Nights - Data Structures & Algorithms Workshop" width="100%" style="border-radius: 8px;" />
</p>

# Algorithmic Thinking Starter
> **Core Algorithmic Mechanics from First Principles**  
> *Official companion repository for NTU Coding Nights 3.0 (Night 1: Data Structures & Algorithms Workshop)*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/evecount/algorithmic-thinking-starter/blob/main/notebooks/interactive_workbook.ipynb)
[![Beginner Guide](https://img.shields.io/badge/Guide-How%20to%20Use-orange.svg)](./HOW_TO_USE.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Organized by WIT x IEEE](https://img.shields.io/badge/Organizers-NTU%20WIT%20%C3%97%20IEEE-9cf.svg)](#organizers--acknowledgments)

> 🚀 **New to Python, GitHub, or Google Colab?**  
> Read our step-by-step [**Beginner's How-To Guide (`HOW_TO_USE.md`)**](./HOW_TO_USE.md) (or view the [Web Documentation](https://evecount.github.io/algorithmic-thinking-starter/)) to learn how to run, edit, and save your solutions in Google Colab with zero installation!

---

## 📌 Executive Overview

Most technical interview preparation fails because students attempt to memorize hundreds of arbitrary solutions on LeetCode. When an interviewer introduces a minor constraint mutation, panic sets in.

**Algorithmic Thinking Starter** strips away the interview panic. We deconstruct computer science mechanics from first principles:
- **Heuristics over Math Paralysis:** Understand asymptotic scaling without getting bogged down in epsilon-delta definitions.
- **Structural Invariants:** Learn to recognize *when* and *why* a problem demands a specific data structure.
- **The Memory-Compute Exchange:** Master the space-time trade-off to systematically pull $O(n^2)$ bottlenecks down to $O(n)$ or $O(1)$.
- **Zero-Panic Interview Delivery:** Execute a repeatable 5-step framework that proves senior-level communication and intentionality.

---

## 👥 Organizers & Acknowledgments

This masterclass is a student-led initiative hosted at **Nanyang Technological University (NTU)**:
- **Jointly Presented by:**
  - [**NTU Women In Tech (WIT @ NTU)**](https://www.linkedin.com/company/ntu-women-in-tech/) — Empowering students in STEM through learning, mentorship, and industry engagement (*SheBuilds Datathon*, *SheLearns*, *Beyond Binary Techathon*, *woMENTORS*).
  - [**IEEE NTU Student Branch**](https://www.linkedin.com/company/ieee-ntu-student-branch/) — Advancing innovation and technology education since 1991 (*iNTUition Hackathon*, *Synapse*, *Industry Projects*).
- **Student Organizing Leads:** Called in by **Rishika Mehta** and **Saba Azad** to structure and deliver this foundational technical masterclass.
- **Lead Instructor & Speaker:** **Gwendalynn Lim Wan Ting**, CTO & Systems Architect at [Eve Count Quantum Systems](https://github.com/evecount), specializing in agentic operating frameworks, applied computing, and AI orchestration.
- **Event Date:** Monday, October 12 | 18:00 – 21:00 SGT | NTU Campus

---

## 🗺️ Masterclass Curriculum & Problem Tracks

```
                        ┌─────────────────────────────────┐
                        │      Algorithmic Thinking       │
                        │        First Principles         │
                        └────────────────┬────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐            ┌──────────────────┐
│   Track 1:       │           │   Track 2:       │            │   Track 3:       │
│   Big-O Growth   │           │   HashMaps/Sets  │            │   Two Pointers   │
│   Rate Models    │           │   O(1) Direct    │            │   O(1) Auxiliary │
└────────┬─────────┘           └────────┬─────────┘            └────────┬─────────┘
         │                              │                               │
         │ • Ignore Stopwatches         │ • Frequency Counters          │ • Converging Pointers
         │ • Asymptotic Bounds          │ • Contains Duplicate          │ • Valid Palindrome
         │ • Space-Time Currency        │ • Look-Behind Complements     │ • Sliding Window
         │ • Worst-Case Analysis        │ • Two Sum                     │ • In-Place Manipulation
         │                              │                               │ • Two Sum II (Sorted)
         └──────────────────────────────┼───────────────────────────────┘
                                         │
                                         ▼
                        ┌─────────────────────────────────┐
                        │   Track 4: 5-Step Interview     │
                        │   Whiteboard Deconstruction     │
                        └─────────────────────────────────┘
```

---

### Track 1: Big-O Intuition & Asymptotic Mental Models
Wall-clock benchmarks (`time.time()`) depend on hardware, CPU caches, and OS scheduling. Asymptotic notation measures the mathematical rate of growth in operations as input size $n \to \infty$.

| Complexity | Class Name | Operations for $n = 10^5$ | Typical Mechanism | Interview Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **$O(1)$** | Constant | 1 op | Hash table lookup, direct array index | **Optimal Target** |
| **$O(\log n)$** | Logarithmic | $\approx 17$ ops | Binary search, halving search space | **Scale Standard** |
| **$O(n)$** | Linear | $10^5$ ops | Single loop, Two Pointers, HashMap pass | **Golden Standard** |
| **$O(n \log n)$** | Linearithmic | $\approx 1.7 \times 10^6$ ops | Timsort, Merge Sort, Divide & Conquer | **Sorting Baseline** |
| **$O(n^2)$** | Quadratic | $10^{10}$ ops | Nested loops comparing all pairs $(i, j)$ | **TLE Risk ($>10^4$)** |
| **$O(2^n)$** | Exponential | $10^{30,000}$ ops | Naive backtracking / subsets | **Collapse** |

> **The Golden Axiom:** RAM is plentiful; clock cycles are bounded. Spend $O(n)$ memory in an auxiliary hash map to annihilate an $O(n^2)$ nested loop.

---

### Track 2: Hash Tables & Sets ($O(1)$ Direct Access)
When you find yourself wanting to write a nested loop to ask *"Have I seen this element before?"*, stop. A nested loop repeatedly scans past data. An auxiliary Hash Set or Hash Map remembers it in $O(1)$ amortized time.

#### 1. Frequency Counter Pattern
Instead of rescanning an array to compute counts, build a running frequency tally in one pass:
```python
counts = {}
for item in collection:
    counts[item] = counts.get(item, 0) + 1
```

#### 2. Problem 1.1 — Contains Duplicate
- **Task:** Return `True` if any value appears at least twice in an integer array `nums`.
- **Brute Force:** Compare every pair $\to O(n^2)$ time, $O(1)$ space.
- **Optimal (Hash Set):**
  ```python
  def contains_duplicate(nums: list[int]) -> bool:
      seen = set()
      for num in nums:
          if num in seen:
              return True
          seen.add(num)
      return False
  ```
- **Complexity:** $O(n)$ Time | $O(n)$ Space

#### 3. Problem 1.2 — Two Sum (The Look-Behind Complement)
- **Task:** Return the **indices** of two numbers in `nums` that add up to `target`.
- **The Mental Shift:** Instead of searching forward into the array with an inner loop, compute the required complement $y = \text{target} - x$ and look backward into a visited dictionary:
  ```python
  def two_sum(nums: list[int], target: int) -> list[int]:
      prev_map = {}  # value -> index
      for i, num in enumerate(nums):
          complement = target - num
          if complement in prev_map:
              return [prev_map[complement], i]
          prev_map[num] = i
      return []
  ```
- **Complexity:** $O(n)$ Time | $O(n)$ Space

---

### Track 3: Two Pointers & In-Place Mechanics
When an interviewer says *"Can you do this in $O(1)$ auxiliary space?"*, you cannot allocate a hash table. You must exploit the underlying sequence ordering using coordinated pointers.

#### 1. Inward Converging Pointers — Valid Palindrome
- **Task:** Verify if a string reads identically forward and backward after stripping non-alphanumerics.
- **The Junior Mistake:** `cleaned = ''.join(...)` allocates a brand-new $O(n)$ string in heap RAM.
- **Zero-Allocation In-Place Solution:**
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
  ```
- **Complexity:** $O(n)$ Time | $O(1)$ Auxiliary Space

#### 2. Sliding Window Dynamics — Longest Substring Without Repeats
- **Task:** Find the length of the longest continuous substring with all unique characters.
- **Mechanism:** Expand the `right` boundary to ingest characters. The moment a duplicate enters the window, squeeze the `left` boundary forward until the window becomes valid again:
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
  ```
- **Complexity:** $O(n)$ Time | $O(\min(n, m))$ Space ($m$ = character set size)

#### 3. In-Place Directional Steering — Two Sum II (Sorted Input)
- **Task:** Find two indices whose values sum to `target` in an array that is **already sorted** in non-decreasing order.
- **The Monotonicity Compass:**
  - $\text{sum} < \text{target} \implies$ We need a larger sum $\to \text{left} \mathrel{+}= 1$
  - $\text{sum} > \text{target} \implies$ We need a smaller sum $\to \text{right} \mathrel{-}= 1$
  ```python
  def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
      left, right = 0, len(numbers) - 1
      while left < right:
          current_sum = numbers[left] + numbers[right]
          if current_sum == target:
              return [left + 1, right + 1]  # 1-indexed specification
          elif current_sum < target:
              left += 1
          else:
              right -= 1
      return []
  ```
- **Complexity:** $O(n)$ Time | $O(1)$ Space *(Zero memory overhead!)*

---

### Track 4: The 5-Step Technical Interview Deconstruction Framework

Never start typing immediately when an interviewer finishes presenting a problem. Premature coding is the #1 signal of an inexperienced candidate.

```
  ┌─────────────────────────┐
  │ 1. Clarify Constraints  │ Confirm bounds, empty inputs, negatives, return types.
  └────────────┬────────────┘
               ▼
  ┌─────────────────────────┐
  │ 2. State Brute Force    │ Articulate naive baseline (e.g. O(n²)) and identify bottleneck.
  └────────────┬────────────┘
               ▼
  ┌─────────────────────────┐
  │ 3. Identify Pattern     │ Select HashMap, Two Pointers, or Window; get interviewer buy-in.
  └────────────┬────────────┘
               ▼
  ┌─────────────────────────┐
  │ 4. Code Idiomatically   │ Write clean, modular Python with robust boundary guards.
  └────────────┬────────────┘
               ▼
  ┌─────────────────────────┐
  │ 5. Manual Dry-Run Trace │ Construct a state table on paper/whiteboard before running code.
  └─────────────────────────┘
```

#### Example Dry-Run State Table (`nums = [3, 2, 4]`, `target = 6`)
| Step | Index ($i$) | Number | Needed Complement | Check `complement in prev_map` | `prev_map` State | Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Start** | — | — | — | — | `{}` | Initialize empty dict |
| **1** | `0` | `3` | $6 - 3 = 3$ | `3 in {}` $\to$ **False** | `{3: 0}` | Store `3: 0` |
| **2** | `1` | `2` | $6 - 2 = 4$ | `4 in {3: 0}` $\to$ **False** | `{3: 0, 2: 1}` | Store `2: 1` |
| **3** | `2` | `4` | $6 - 4 = 2$ | `2 in {3:0, 2:1}` $\to$ **True!** | Found index `1` | **Return `[1, 2]`** |

---

## 🚀 Repository Structure

```
algorithmic-thinking-starter/
├── README.md                                    # Comprehensive curriculum & first-principles guide
├── solutions.py                                 # Reference Python implementations with test assertions
├── interactive_workbook.md                      # Complete student workbook with problem templates
├── NTU_DSA_Night_1_Dynamite_Script.md           # 39-slide DYNAMITE master presentation script
├── slides_img/                                  # High-resolution slide captures (slide_01 to slide_39)
└── .gitignore                                   # Lightweight git hygiene
```

---

## 🧪 Running the Reference Solutions

All five core problem solutions are fully implemented, typed, and unit-tested in [`solutions.py`](./solutions.py):

```bash
# Clone the repository
git clone https://github.com/evecount/algorithmic-thinking-starter.git
cd algorithmic-thinking-starter

# Execute test suite
python solutions.py
```

Expected output:
```text
[✓] Contains Duplicate Passed!
[✓] Two Sum Passed!
[✓] Valid Palindrome Passed!
[✓] Longest Substring Without Repeats Passed!
[✓] Two Sum II (Sorted Array) Passed!
All algorithmic benchmarks verified successfully!
```

---

## 📈 Post-Session Roadmap & Sustainable Practice

- **Focus on Pattern Clusters:** Don't solve 500 disconnected problems. Solve 5 problems per pattern until the mental model is second nature.
- **Curated Curriculum:**
  - **Week 1:** Arrays & Hashing (*Contains Duplicate*, *Two Sum*, *Group Anagrams*)
  - **Week 2:** Two Pointers (*Valid Palindrome*, *Two Sum II*, *3Sum*, *Container With Most Water*)
  - **Week 3:** Sliding Window (*Longest Substring Without Repeats*, *Minimum Window Substring*)
- **Interactive Visualizers:** Use [pythontutor.com](https://pythontutor.com) to trace pointer movements and heap frames frame-by-frame.
- **Night 2 Preview:** Technical Mock Interviews and Online Assessment (OA) simulation on **October 19, 2026**.

---

<p align="center">
  <b>Developed with precision for NTU Coding Nights 3.0</b><br>
  <sub>Hosted by NTU Women In Tech & IEEE NTU Student Branch • Instructed by Gwendalynn Lim</sub>
</p>
