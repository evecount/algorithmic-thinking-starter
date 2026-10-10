import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

hints = {
    'def contains_duplicate': [
        "def contains_duplicate(nums: list[int]) -> bool:\n",
        "    # Hint 1: We need a way to remember numbers we've already seen.\n",
        "    # What data structure gives us instant O(1) lookups?\n",
        "    \n",
        "    # Hint 2: Loop through each number. If it's in our memory, we found a duplicate!\n",
        "    # If it's not, add it to our memory and keep going.\n",
        "    pass\n"
    ],
    'def two_sum': [
        "def two_sum(nums: list[int], target: int) -> list[int]:\n",
        "    # Hint 1: We want to store what we've seen so far, but we need both the number AND its index.\n",
        "    # A dictionary (Hash Map) is perfect: {number: index}\n",
        "    \n",
        "    # Hint 2: For every number, calculate what its 'partner' must be (target - number).\n",
        "    # If that partner is already in our dictionary, we have our answer!\n",
        "    pass\n"
    ],
    'def is_palindrome': [
        "def is_palindrome(s: str) -> bool:\n",
        "    # Hint 1: Put a pointer (index) at the very start, and one at the very end.\n",
        "    # Hint 2: Move them towards the middle. If they point to a non-alphanumeric character, skip it.\n",
        "    # Hint 3: Compare the letters (make sure to lowercase them). If they don't match, return False.\n",
        "    pass\n"
    ],
    'def length_of_longest_substring': [
        "def length_of_longest_substring(s: str) -> int:\n",
        "    # Hint 1: Imagine a window on the string. We need a 'left' pointer and a 'right' pointer.\n",
        "    # Hint 2: We need a Set to keep track of the letters currently inside our window.\n",
        "    # Hint 3: Expand the right side. If you hit a duplicate letter, shrink the left side until the duplicate is gone!\n",
        "    pass\n"
    ],
    'def two_sum_sorted': [
        "def two_sum_sorted(numbers: list[int], target: int) -> list[int]:\n",
        "    # Hint 1: The array is sorted! This means we can use Two Pointers instead of a Hash Map.\n",
        "    # Hint 2: Start at the extremes (left=0, right=end).\n",
        "    # Hint 3: If their sum is too big, move the right pointer left. If it's too small, move left pointer right.\n",
        "    pass\n"
    ]
}

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('def '):
            # Find which function this is
            for key, new_source in hints.items():
                if source[0].startswith(key):
                    cell['source'] = new_source
                    break

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully injected code hints into the Colab notebook.")
