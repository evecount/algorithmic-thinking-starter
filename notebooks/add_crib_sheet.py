import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

crib_sheet_md = """---

# 📚 Python Operations Crib Sheet
*Here is a quick reference for all the Python syntax we used tonight!*

### 1. Hash Sets (The Bouncer's Clipboard)
* **`seen = set()`** : Create a new empty Hash Set.
* **`seen.add(5)`** : Add the number `5` to the set.
* **`5 in seen`** : Check if `5` is already in the set (Very fast! $O(1)$).
* **`seen.remove(5)`** : Remove the number `5` from the set.

### 2. Hash Maps (Dictionaries)
* **`prev_map = {}`** : Create a new empty Hash Map (dictionary).
* **`prev_map[5] = 2`** : Store the number `5` as a key, and `2` as its value.
* **`5 in prev_map`** : Check if the number `5` is stored as a key in the map.

### 3. Arrays & Two Pointers
* **`len(nums)`** : Get the total length (number of items) in an array or string.
* **`left += 1`** : Move a pointer one step to the right (increment).
* **`right -= 1`** : Move a pointer one step to the left (decrement).
* **`nums[0]`** : Look at the first item in the array (0-indexed).
* **`nums[-1]`** : Look at the last item in the array.
* **`for i, num in enumerate(nums):`** : Loop through an array and automatically keep track of BOTH the index (`i`) and the value (`num`).

### 4. Strings & Math
* **`char.isalnum()`** : Check if a character is a letter or number (ignores spaces and punctuation).
* **`char.lower()`** : Convert a character to lowercase.
* **`max(10, 15)`** : Returns the biggest number (returns 15).
"""

crib_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [crib_sheet_md]
}

# Check if we already added a crib sheet to avoid duplicates
already_exists = False
if len(nb['cells']) > 0 and 'Python Operations Crib Sheet' in ''.join(nb['cells'][-1]['source']):
    already_exists = True

if not already_exists:
    nb['cells'].append(crib_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully appended the Python Crib Sheet to the end of the notebook.")
