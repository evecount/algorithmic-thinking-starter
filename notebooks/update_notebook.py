import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Intuition mapping based on the problem title
intuitions = {
    'Contains Duplicate': "> **What are we solving for?** We need to find out if there are any repeating elements. Instead of comparing every number to every other number (which is slow), we use a Hash Set (like a bouncer's clipboard). As we check each number, we ask 'Are you on the clipboard?' If not, we add it. If yes, we found a duplicate!\n\n",
    'Two Sum (Hash Map)': "> **What are we solving for?** We need two numbers that add up to a target. Instead of trying every possible pair, we calculate the exact 'complement' (Target - Current Number) we need. Then we ask our Hash Map if we've already seen that complement earlier. If we have, we're done!\n\n",
    'Valid Palindrome': "> **What are we solving for?** A palindrome is symmetrical. We want to check if the left side perfectly mirrors the right side. Instead of creating reversed copies of the string, we place one pointer at the start and one at the end, and squeeze them inward, checking if they match at every step.\n\n",
    'Longest Substring Without Repeats': "> **What are we solving for?** We want to find the longest chain of unique characters. We use a 'Sliding Window' (a left and right boundary). We expand the right side as long as characters are unique. If we hit a duplicate, we shrink the left side until the duplicate is gone, keeping track of the largest window size we ever had.\n\n",
    'Two Sum II (Sorted Array)': "> **What are we solving for?** Just like Two Sum, but the array is sorted! Because it's sorted, we don't even need a Hash Map. We put pointers at the far left (smallest) and far right (largest). If their sum is too big, we move the right pointer left. If it's too small, we move the left pointer right.\n\n"
}

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('## Problem'):
            title_line = source[0]
            
            # Find matching intuition
            match_key = None
            for key in intuitions.keys():
                if key in title_line:
                    match_key = key
                    break
            
            if match_key:
                # Check if we already injected it so we don't duplicate
                already_injected = False
                for line in source:
                    if "**What are we solving for?**" in line:
                        already_injected = True
                        break
                
                if not already_injected:
                    # Insert the intuition after the Description (usually line 1)
                    source.insert(2, intuitions[match_key])

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully injected intuitive explanations into the Colab notebook.")
