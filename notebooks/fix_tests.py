import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('# Test Cases for'):
            # The test cells look like:
            # # Test Cases for Contains Duplicate
            # assert contains_duplicate(...) == True, 'Test 1 Failed'
            # ...
            # print('[PASS] All Contains Duplicate tests passed!')
            
            # Find the function name being tested
            func_name = ""
            for line in source:
                if 'assert ' in line:
                    func_name = line.split('assert ')[1].split('(')[0]
                    break
            
            if func_name:
                # Rewrite the test block to catch NotImplemented or None returns
                new_source = [
                    f"# Test Cases for {func_name.replace('_', ' ').title()}\n",
                    "try:\n",
                    f"    result = {func_name}([]) # Quick test to see if it's implemented\n",
                    "    if result is None:\n",
                    "        print('🚧 Wait! You need to write your code in the cell above first.')\n",
                    "        print('Replace the `pass` keyword with your solution and run this cell again!')\n",
                    "    else:\n"
                ]
                # Indent the original asserts
                for line in source[1:]:
                    if line.strip():
                        new_source.append("        " + line)
                new_source.extend([
                    "except AssertionError as e:\n",
                    "    print(f'❌ {e}')\n",
                    "except Exception as e:\n",
                    "    print(f'⚠️ Error in your code: {e}')\n"
                ])
                cell['source'] = new_source

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully wrapped test cells with friendly error handling.")
