# 🔰 Beginner's Guide: How to Use this Workbook
> **A complete step-by-step walkthrough for students new to Python, Google Colab, and GitHub.**  
> *Prepared for NTU Coding Nights 3.0 (WIT x IEEE)*

---

## 🚀 Quick Start: Choose Your Environment

| Method | Best For | Setup Time | Prerequisites | Launch Link |
| :--- | :--- | :--- | :--- | :--- |
| **Google Colab** *(Recommended)* | Running in browser without installing Python | **30 seconds** | Google Account | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/evecount/algorithmic-thinking-starter/blob/main/notebooks/interactive_workbook.ipynb) |
| **Local VS Code / Python** | Offline practice & building a local portfolio | **5 minutes** | Python 3.10+, VS Code | [See Local Instructions](#option-2-running-locally-on-your-computer) |
| **PythonTutor Trace** | Visualizing pointer movements frame-by-frame | **Instant** | Browser | [pythontutor.com](https://pythontutor.com) |

---

## ⚡ Option 1: Using Google Colab (Zero Installation)

Google Colab allows you to write and execute Python code in your web browser with zero configuration.

### Step 1: Open the Colab Workbook
Click the badge below to open the interactive notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/evecount/algorithmic-thinking-starter/blob/main/notebooks/interactive_workbook.ipynb)

---

### Step 2: Save a Copy to Your Google Drive *(Crucial!)*
By default, Colab opens in a temporary **"Playground"** mode. If you close your browser tab, your solutions will be lost!

1. In the top-left menu, click **File** $\to$ **Save a copy in Drive**.
2. A new tab will open titled `Copy of interactive_workbook.ipynb`.
3. You can now edit and save your code permanently to your Google Drive!

```
  File ──► Save a copy in Drive ──► Opens your personal editable copy
```

---

### Step 3: Running Code Cells
A Jupyter notebook consists of **Cells** (text cells and code cells).

- Click on any code cell to select it.
- Press **`Shift + Enter`** on your keyboard (or click the round **`▶ Play`** button on the left of the cell).
- The cell will execute and display the output directly beneath it.

> **Colab Hotkeys Cheat Sheet:**
> - **`Shift + Enter`**: Run active cell and move to next cell.
> - **`Ctrl + Enter`**: Run active cell and stay on current cell.
> - **`Ctrl + M + B`**: Insert a new code cell below.
> - **`Ctrl + M + D`**: Delete the selected cell.

---

### Step 4: Solving the Problems & Running the Tests
Each problem in the notebook is split into two cells:
1. **The Function Cell:** Contains the starter template with `# TODO`.
2. **The Test Cell:** Contains automated `assert` statements that verify your solution against edge cases.

#### Example: Solving Problem 1.1 (Contains Duplicate)
Replace the `pass` statement in the template:

```python
# 1. Fill in your implementation:
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

Then click the test cell below it and press **`Shift + Enter`**:
```python
# 2. Run the test cell:
assert contains_duplicate([1, 2, 3, 1]) == True, "Test 1 Failed"
assert contains_duplicate([1, 2, 3, 4]) == False, "Test 2 Failed"
print("[PASS] All Contains Duplicate tests passed!")
```

- If your solution is correct, you will see:  
  `[PASS] All Contains Duplicate tests passed!`
- If your solution fails, Python will throw an `AssertionError: Test X Failed`.

---

## 💻 Option 2: Running Locally on Your Computer

If you already have Python and VS Code installed, you can clone the repository to run everything offline.

### Step 1: Clone the Repository
Open your Terminal (macOS/Linux) or PowerShell (Windows) and run:

```bash
git clone https://github.com/evecount/algorithmic-thinking-starter.git
cd algorithmic-thinking-starter
```

### Step 2: Run the Automated Test Suite
To verify the reference solutions against all benchmarks:

```bash
python solutions.py
```

Output:
```text
[PASS] Contains Duplicate Passed!
[PASS] Two Sum Passed!
[PASS] Valid Palindrome Passed!
[PASS] Longest Substring Without Repeats Passed!
[PASS] Two Sum II (Sorted Array) Passed!

All algorithmic benchmarks verified successfully!
```

### Step 3: Run the Jupyter Notebook in VS Code
1. Open the folder in VS Code:
   ```bash
   code .
   ```
2. Open `notebooks/interactive_workbook.ipynb`.
3. VS Code will prompt you to install the **Jupyter Extension** (click Install).
4. Select your local Python environment in the top-right corner (`Select Kernel`).
5. Run and edit cells just like in Colab!

---

## 🔍 Option 3: Visualizing with PythonTutor

If you find pointer movements or dictionary state changes confusing, use **PythonTutor**:

1. Go to [https://pythontutor.com/visualize.html](https://pythontutor.com/visualize.html).
2. Select **Python 3.11**.
3. Paste any solution from [`solutions.py`](./solutions.py).
4. Click **Visualize Execution**.
5. Use the **Next >** button to watch:
   - The loop counter increment.
   - Pointers (`left` and `right`) advance.
   - The dictionary (`prev_map`) grow in memory step-by-step.

---

## 🛠️ Common Beginner Errors & How to Fix Them

### 1. `IndentationError: expected an indented block`
- **Cause:** Python uses whitespace indentation instead of curly braces `{}`. Lines inside a function, loop, or `if` statement must be indented by exactly **4 spaces**.
- **Fix:** Make sure your code aligns cleanly under the `def` and `for` lines.

### 2. `IndexError: string index out of range` or `list index out of range`
- **Cause:** You tried to access `arr[i]` where index `i` is greater than or equal to `len(arr)`.
- **Fix:** Always ensure pointer while-loops have a boundary check: `while left < right and ...`.

### 3. `TypeError: 'NoneType' object is not subscriptable`
- **Cause:** Your function finished without reaching an explicit `return` statement, defaulting to `None`.
- **Fix:** Make sure every execution path has a valid `return` value (e.g. `return []` or `return False` at the end).

### 4. Cell Never Finishes Running (Infinite Loop)
- **Cause:** A `while` loop condition never becomes false (e.g. forgot `left += 1`).
- **Fix:** In Colab, click **Runtime** $\to$ **Interrupt execution** (or press the Stop button on the cell), fix your loop increment, and re-run.

---

## 💬 Getting Help
- Check the official reference solutions in [`solutions.py`](./solutions.py).
- Review the detailed 39-slide lecture breakdown in [`README.md`](./README.md).
- Ask questions in the workshop or email the organizers at `NTUWIT@e.ntu.edu.sg` and `ieeentu-branch@e.ntu.edu.sg`.
