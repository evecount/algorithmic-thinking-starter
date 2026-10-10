import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# These are DRY, ACADEMIC, purely technical comments so the students don't know she is using the "bouncer/clipboard" metaphors from a script.
technical_solutions = {
    'Contains Duplicate': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def contains_duplicate(nums: list[int]) -> bool:
    # Initialize a hash set for O(1) membership testing
    seen = set()
    
    # Iterate through the array in a single pass
    for num in nums:
        # Check if the element has been encountered previously
        if num in seen:
            return True
            
        # Add the element to our set tracking state
        seen.add(num)
        
    # If the loop completes, all elements are unique
    return False
```
</details>""",

    'Two Sum': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    # Maps array values to their original indices
    prev_map = {}
    
    for i, num in enumerate(nums):
        # Determine the exact difference required to reach the target sum
        complement = target - num
        
        # Verify if the required complement exists in our map
        # Note: This check occurs prior to insertion to prevent self-matching
        if complement in prev_map:
            return [prev_map[complement], i]
            
        # Store the current element for future iterations
        prev_map[num] = i
        
    return []
```
</details>""",

    'Valid Palindrome': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def is_palindrome(s: str) -> bool:
    # Initialize two pointers at opposite ends of the string
    left, right = 0, len(s) - 1
    
    while left < right:
        # Advance the left pointer past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
            
        # Retreat the right pointer past non-alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Perform case-insensitive comparison
        if s[left].lower() != s[right].lower():
            return False
            
        # Move pointers inward
        left += 1
        right -= 1
        
    return True
```
</details>""",

    'Longest Substring': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def length_of_longest_substring(s: str) -> int:
    # Maintain a set of characters currently in the sliding window
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If a duplicate is detected, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        # Expand the window bounds
        char_set.add(s[right])
        
        # Update the maximum recorded window size
        max_len = max(max_len, right - left + 1)
        
    return max_len
```
</details>""",

    'Two Sum II': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    # Initialize pointers at the array boundaries
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        # Target achieved (adjusting for 1-indexed constraints)
        if current_sum == target:
            return [left + 1, right + 1]
            
        # If sum is deficient, increase it by moving the left pointer rightward
        elif current_sum < target:
            left += 1
            
        # If sum is excessive, decrease it by moving the right pointer leftward
        else:
            right -= 1
            
    return []
```
</details>"""
}

current_problem = None
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and len(cell['source']) > 0 and cell['source'][0].startswith('# Test Cases for'):
        title = cell['source'][0]
        for key in technical_solutions.keys():
            if key in title:
                current_problem = key
                break
                
    elif cell['cell_type'] == 'markdown' and len(cell['source']) > 0 and '<details>' in cell['source'][0] and current_problem:
        cell['source'] = [technical_solutions[current_problem]]
        current_problem = None 

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully replaced solution comments with dry, technical alternatives.")
