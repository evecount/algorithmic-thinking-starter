import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The expected original tests
original_tests = {
    'Contains Duplicate': [
        "    assert contains_duplicate([1, 2, 3, 1]) == True, 'Test 1 Failed'\n",
        "    assert contains_duplicate([1, 2, 3, 4]) == False, 'Test 2 Failed'\n",
        "    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True, 'Test 3 Failed'\n"
    ],
    'Two Sum': [
        "    assert two_sum([2, 7, 11, 15], 9) == [0, 1], 'Test 1 Failed'\n",
        "    assert two_sum([3, 2, 4], 6) == [1, 2], 'Test 2 Failed'\n",
        "    assert two_sum([3, 3], 6) == [0, 1], 'Test 3 Failed'\n"
    ],
    'Valid Palindrome': [
        "    assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test 1 Failed'\n",
        "    assert is_palindrome('race a car') == False, 'Test 2 Failed'\n",
        "    assert is_palindrome(' ') == True, 'Test 3 Failed'\n"
    ],
    'Longest Substring': [
        "    assert length_of_longest_substring('abcabcbb') == 3, 'Test 1 Failed'\n",
        "    assert length_of_longest_substring('bbbbb') == 1, 'Test 2 Failed'\n",
        "    assert length_of_longest_substring('pwwkew') == 3, 'Test 3 Failed'\n",
        "    assert length_of_longest_substring('') == 0, 'Test 4 Failed'\n"
    ],
    'Two Sum II': [
        "    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], 'Test 1 Failed'\n",
        "    assert two_sum_sorted([2, 3, 4], 6) == [1, 3], 'Test 2 Failed'\n",
        "    assert two_sum_sorted([-1, 0], -1) == [1, 2], 'Test 3 Failed'\n"
    ]
}

dummy_calls = {
    'Contains Duplicate': "contains_duplicate([])",
    'Two Sum': "two_sum([], 0)",
    'Valid Palindrome': "is_palindrome('')",
    'Longest Substring': "length_of_longest_substring('')",
    'Two Sum II': "two_sum_sorted([], 0)"
}

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('# Test Cases for'):
            title = source[0].strip()
            
            match_key = None
            for key in dummy_calls:
                if key in title:
                    match_key = key
                    break
                    
            if match_key:
                new_source = [
                    f"{title}\n",
                    f"if {dummy_calls[match_key]} is None:\n",
                    "    print('🚧 Wait! You need to write your code in the cell above first.')\n",
                    "else:\n"
                ]
                new_source.extend(original_tests[match_key])
                new_source.append(f"    print('[PASS] All {match_key} tests passed!')\n")
                
                cell['source'] = new_source

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully simplified test cells.")
