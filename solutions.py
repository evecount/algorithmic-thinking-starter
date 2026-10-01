"""
Algorithmic Thinking Starter - Reference Implementation & Test Suite
NTU Coding Nights 3.0: Night 1 (WIT x IEEE)
Lead Instructor: Gwendalynn Lim Wan Ting
"""

from typing import List


# ==============================================================================
# Track 2: HashMaps & Sets (O(1) Direct Access)
# ==============================================================================

def contains_duplicate(nums: List[int]) -> bool:
    """
    Problem 1.1: Contains Duplicate
    Time Complexity:  O(n) - Single linear pass
    Space Complexity: O(n) - Set stores up to n distinct elements
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True  # Early exit upon finding first duplicate
        seen.add(num)
    return False


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Problem 1.2: Two Sum (Single-Pass Hash Map)
    Time Complexity:  O(n) - Single pass through nums
    Space Complexity: O(n) - Dictionary stores up to n entries
    """
    prev_map = {}  # value -> original index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in prev_map:
            return [prev_map[complement], i]
        prev_map[num] = i
    return []


# ==============================================================================
# Track 3: Two Pointers & Sliding Window
# ==============================================================================

def is_palindrome(s: str) -> bool:
    """
    Problem 2.1: Valid Palindrome (Inward Converging Pointers)
    Time Complexity:  O(n) - Each character inspected at most twice
    Space Complexity: O(1) - Zero heap string allocations
    """
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


def length_of_longest_substring(s: str) -> int:
    """
    Problem 2.2: Longest Substring Without Repeats (Sliding Window)
    Time Complexity:  O(n) - Each character added and removed at most once
    Space Complexity: O(min(n, m)) - Set bounded by string length and character set
    """
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


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Problem 2.3: Two Sum II - Input Array Is Sorted (Monotonic Two Pointers)
    Time Complexity:  O(n) - At most n total pointer shifts
    Space Complexity: O(1) - Zero auxiliary memory allocation
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            # Specification requires 1-indexed output
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1   # Need a larger sum
        else:
            right -= 1  # Need a smaller sum
    return []


# ==============================================================================
# Verification Suite
# ==============================================================================

def run_tests():
    # 1. Contains Duplicate
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("[PASS] Contains Duplicate Passed!")

    # 2. Two Sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("[PASS] Two Sum Passed!")

    # 3. Valid Palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome(".,") is True
    print("[PASS] Valid Palindrome Passed!")

    # 4. Longest Substring Without Repeats
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("[PASS] Longest Substring Without Repeats Passed!")

    # 5. Two Sum II (Sorted Array)
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    print("[PASS] Two Sum II (Sorted Array) Passed!")

    print("\nAll algorithmic benchmarks verified successfully!")


if __name__ == "__main__":
    run_tests()
