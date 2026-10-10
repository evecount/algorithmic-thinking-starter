import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Heavily commented, fully working solutions
working_solutions = {
    'def contains_duplicate': [
        "def contains_duplicate(nums: list[int]) -> bool:\n",
        "    # 1. We create an empty Hash Set. Think of this as our 'clipboard'.\n",
        "    seen = set()\n",
        "    \n",
        "    # 2. We look at each number in the array one by one.\n",
        "    for num in nums:\n",
        "        # 3. We ask the clipboard: 'Is this number already on you?'\n",
        "        if num in seen:\n",
        "            return True  # Yes! We found a duplicate. Stop immediately.\n",
        "            \n",
        "        # 4. If not, write it down on the clipboard so we remember it for later.\n",
        "        seen.add(num)\n",
        "        \n",
        "    # 5. If we checked every person and nobody was on the clipboard twice, they are all unique.\n",
        "    return False\n"
    ],
    'def two_sum': [
        "def two_sum(nums: list[int], target: int) -> list[int]:\n",
        "    # 1. Create a Hash Map. It stores {number_we_saw: its_index}\n",
        "    prev_map = {}\n",
        "    \n",
        "    # 2. Loop through the array, keeping track of the index (i) and the number (num)\n",
        "    for i, num in enumerate(nums):\n",
        "        # 3. Calculate exactly what number we need to hit the target\n",
        "        complement = target - num\n",
        "        \n",
        "        # 4. Check our map: Have we seen this exact complement before?\n",
        "        if complement in prev_map:\n",
        "            # Yes! Return the index of the complement we saved, and our current index.\n",
        "            return [prev_map[complement], i]\n",
        "            \n",
        "        # 5. No? Save the current number and its index into the map for the future.\n",
        "        prev_map[num] = i\n",
        "        \n",
        "    return []\n"
    ],
    'def is_palindrome': [
        "def is_palindrome(s: str) -> bool:\n",
        "    # 1. Place a pointer at the very start (left) and the very end (right)\n",
        "    left, right = 0, len(s) - 1\n",
        "    \n",
        "    # 2. Keep squeezing inward until they cross in the middle\n",
        "    while left < right:\n",
        "        # 3. Skip over spaces and punctuation on the left side\n",
        "        while left < right and not s[left].isalnum():\n",
        "            left += 1\n",
        "            \n",
        "        # 4. Skip over spaces and punctuation on the right side\n",
        "        while left < right and not s[right].isalnum():\n",
        "            right -= 1\n",
        "            \n",
        "        # 5. Check if the actual letters match (ignoring upper/lower case)\n",
        "        if s[left].lower() != s[right].lower():\n",
        "            return False # They don't match! It's not a palindrome.\n",
        "            \n",
        "        # 6. They matched. Squeeze both pointers one step inward.\n",
        "        left += 1\n",
        "        right -= 1\n",
        "        \n",
        "    return True\n"
    ],
    'def length_of_longest_substring': [
        "def length_of_longest_substring(s: str) -> int:\n",
        "    # 1. Create a Set to track the characters inside our current 'window'\n",
        "    char_set = set()\n",
        "    left = 0\n",
        "    max_len = 0\n",
        "    \n",
        "    # 2. Expand the window by moving the 'right' boundary one step at a time\n",
        "    for right in range(len(s)):\n",
        "        # 3. If the new character is already inside our window (a repeat!)\n",
        "        while s[right] in char_set:\n",
        "            # Shrink the window from the left until the duplicate is kicked out\n",
        "            char_set.remove(s[left])\n",
        "            left += 1\n",
        "            \n",
        "        # 4. Add the new unique character into our window\n",
        "        char_set.add(s[right])\n",
        "        \n",
        "        # 5. Record the size of the window if it's the biggest one we've seen so far\n",
        "        max_len = max(max_len, right - left + 1)\n",
        "        \n",
        "    return max_len\n"
    ],
    'def two_sum_sorted': [
        "def two_sum_sorted(numbers: list[int], target: int) -> list[int]:\n",
        "    # 1. Place pointers at the absolute extremes: smallest (left) and largest (right)\n",
        "    left, right = 0, len(numbers) - 1\n",
        "    \n",
        "    # 2. Squeeze inward until we find the target\n",
        "    while left < right:\n",
        "        current_sum = numbers[left] + numbers[right]\n",
        "        \n",
        "        if current_sum == target:\n",
        "            # 3. Found it! (The problem asks for 1-indexed, so we add 1)\n",
        "            return [left + 1, right + 1]\n",
        "            \n",
        "        elif current_sum < target:\n",
        "            # 4. Our sum is too small. We need a bigger number, so move left pointer to the right.\n",
        "            left += 1\n",
        "            \n",
        "        else:\n",
        "            # 5. Our sum is too big. We need a smaller number, so move right pointer to the left.\n",
        "            right -= 1\n",
        "            \n",
        "    return []\n"
    ]
}

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('def '):
            # Replace the hints/TODOs with the actual working commented solutions
            for key, new_source in working_solutions.items():
                if source[0].startswith(key):
                    cell['source'] = new_source
                    break

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully injected working, commented solutions into the Colab notebook.")
