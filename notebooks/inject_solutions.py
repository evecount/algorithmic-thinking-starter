import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

solutions = {
    'Contains Duplicate': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
</details>""",

    'Two Sum': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    prev_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in prev_map:
            return [prev_map[complement], i]
        prev_map[num] = i
    return []
```
</details>""",

    'Valid Palindrome': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

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
</details>""",

    'Longest Substring': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

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
</details>""",

    'Two Sum II': """<details>
<summary><b>👀 Click here to view the solution if you get stuck!</b></summary>

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```
</details>"""
}

new_cells = []
for cell in nb['cells']:
    new_cells.append(cell)
    if cell['cell_type'] == 'code':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('# Test Cases for'):
            # Find which problem this test block is for
            for key, solution_md in solutions.items():
                if key in source[0]:
                    # Create a new markdown cell with the solution
                    solution_cell = {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [solution_md]
                    }
                    new_cells.append(solution_cell)
                    break

nb['cells'] = new_cells

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully injected solution blocks into the Colab notebook.")
