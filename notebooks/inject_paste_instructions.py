import json

notebook_path = r'D:\NTU_DSA_Workbook\notebooks\interactive_workbook.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        if len(source) > 0 and source[0].startswith('def '):
            # It's an active coding cell. Add explicit instructions.
            # Check if we already added the warning so we don't duplicate
            if not source[0].startswith('# 👇'):
                new_source = [
                    "# 👇 IF YOU GET STUCK: Highlight this entire cell, delete it, and paste the solution here!\n",
                    "\n"
                ]
                
                # Add the original function definition and hints
                for line in source:
                    new_source.append(line)
                    
                # Find where 'pass' is and insert a 'write code here' line above it
                for i in range(len(new_source)):
                    if new_source[i].strip() == 'pass':
                        # Get the indentation of 'pass'
                        indent = new_source[i][:len(new_source[i]) - len(new_source[i].lstrip())]
                        new_source.insert(i, indent + "# --- WRITE YOUR CODE BELOW THIS LINE ---\n")
                        break
                        
                cell['source'] = new_source

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Successfully injected pasting instructions into the active code cells.")
