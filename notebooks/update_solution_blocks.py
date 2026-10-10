import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

commented_solutions = {
    'Contains Duplicate': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def contains_duplicate(nums: list[int]) -> bool:
    # 1. We create an empty Hash Set. Think of this as our 'clipboard'.
    seen = set()
    
    # 2. We look at each number in the array one by one.
    for num in nums:
        # 3. We ask the clipboard: 'Is this number already on you?'
        if num in seen:
            return True  # Yes! We found a duplicate. Stop immediately.
            
        # 4. If not, write it down on the clipboard so we remember it for later.
        seen.add(num)
        
    # 5. If we checked every person and nobody was on the clipboard twice, they are all unique.
    return False
```
</details>""",

    'Two Sum': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    # 1. Create a Hash Map. It stores {number_we_saw: its_index}
    prev_map = {}
    
    # 2. Loop through the array, keeping track of the index (i) and the number (num)
    for i, num in enumerate(nums):
        # 3. Calculate exactly what number we need to hit the target
        complement = target - num
        
        # 4. CRUCIAL TRAP: We must check the map BEFORE saving our current number!
        # If we saved first, a number might incorrectly match with itself.
        # Check our map: Have we seen this exact complement before?
        if complement in prev_map:
            # Yes! Return the index of the complement we saved, and our current index.
            return [prev_map[complement], i]
            
        # 5. No? Save the current number and its index into the map for the future.
        prev_map[num] = i
        
    return []
```
</details>""",

    'Valid Palindrome': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def is_palindrome(s: str) -> bool:
    # 1. Place a pointer at the very start (left) and the very end (right)
    left, right = 0, len(s) - 1
    
    # 2. Keep squeezing inward until they cross in the middle
    while left < right:
        # 3. Skip over spaces and punctuation on the left side
        while left < right and not s[left].isalnum():
            left += 1
            
        # 4. Skip over spaces and punctuation on the right side
        while left < right and not s[right].isalnum():
            right -= 1
            
        # 5. Check if the actual letters match (ignoring upper/lower case)
        if s[left].lower() != s[right].lower():
            return False # They don't match! It's not a palindrome.
            
        # 6. They matched. Squeeze both pointers one step inward.
        left += 1
        right -= 1
        
    return True
```
</details>""",

    'Longest Substring': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def length_of_longest_substring(s: str) -> int:
    # 1. Create a Set to track the characters inside our current 'window'
    char_set = set()
    left = 0
    max_len = 0
    
    # 2. Expand the window by moving the 'right' boundary one step at a time
    for right in range(len(s)):
        # 3. If the new character is already inside our window (a repeat!)
        while s[right] in char_set:
            # Shrink the window from the left until the duplicate is kicked out
            char_set.remove(s[left])
            left += 1
            
        # 4. Add the new unique character into our window
        char_set.add(s[right])
        
        # 5. Record the size of the window if it's the biggest one we've seen so far
        max_len = max(max_len, right - left + 1)
        
    return max_len
```
</details>""",

    'Two Sum II': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    # 1. Place pointers at the absolute extremes: smallest (left) and largest (right)
    left, right = 0, len(numbers) - 1
    
    # 2. Squeeze inward until we find the target
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # 3. Found it! (The problem asks for 1-indexed, so we add 1)
            return [left + 1, right + 1]
            
        elif current_sum < target:
            # 4. Our sum is too small. We need a bigger number, so move left pointer to the right.
            left += 1
            
        else:
            # 5. Our sum is too big. We need a smaller number, so move right pointer to the left.
            right -= 1
            
    return []
```
</details>"""
}

# The cells we want to replace are Markdown cells that start with <details> and contain "Click here to view the solution"
# We need to map them correctly. The easiest way is to track the previous test cell title.

current_problem = None
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and len(cell['source']) > 0 and cell['source'][0].startswith('# Test Cases for'):
        # Track which problem we just saw
        title = cell['source'][0]
        for key in commented_solutions.keys():
            if key in title:
                current_problem = key
                break
                
    elif cell['cell_type'] == 'markdown' and len(cell['source']) > 0 and '<details>' in cell['source'][0] and current_problem:
        # This is the solution markdown cell for the current_problem
        cell['source'] = [commented_solutions[current_problem]]
        current_problem = None  # Reset

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully replaced raw solutions with heavily commented solutions.")
