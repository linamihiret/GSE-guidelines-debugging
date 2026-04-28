
### Problem D_1: Debugging Incorrect Average Calculation

**Task Description:**
You are working with a small analytics function that calculates the average score from a list. However, users report that the result is incorrect when negative values appear in the input. The developer intended to ignore invalid (negative) scores, but something is wrong.

Your task is to use an LLM (e.g., GitHub Copilot Chat) and apply the AutoSD (Scientific Debugging) method to identify the root cause and fix the issue.

Follow the structured debugging loop:

Hypothesis → Prediction → Experiment → Observation → Conclusion → <DONE>

**Prerequisites:**  
- Python installed  
- VS Code with GitHub Copilot (or any LLM tool)

**Starter Artefacts:**  
You can find the artifacts [here](./problems/01-debugging-average/calculate_average.py).

**Guidelines 2 steps to Apply:**

**Step 01:** Clearly describe the bug scenario and expected behavior
**Step 02:** Use the LLM to generate a hypothesis before asking for a fix
**Step 03:** Define a prediction (what should happen if the hypothesis is correct)
**Step 04:** Design and run experiments (print/debug statements) to validate assumptions
**Step 05:** Use observations to confirm or reject the hypothesis
**Step 06:** Repeat the process until confident and indicate completion using <DONE>

**Expected Process (AutoSD Style):**

- **Hypothesis:** Negative values are counted in denominator
- **Experiment:** Print total and count at each step
- **Observation:** Count increases even for invalid values
- **Conclusion:** Hypothesis supported
- **Fix:** Move count += 1 inside the condition
- **<DONE>** when output matches expected

**Time Estimate:** approx. 15–20 min

--- 

### Problem D_1: Debugging List Deduplication Logic

**Task Description:**  
A developer wrote a function to remove duplicate elements from a sorted list. However, the function produces incorrect results and sometimes includes duplicates.  

Your task is to use an LLM (e.g., GitHub Copilot Chat) and apply the **AutoSD (Scientific Debugging)** methodology to:
- Identify the root cause of the bug  
- Validate it using real execution  
- Iteratively refine your reasoning  
- Fix the issue with confidence  

Follow the structured debugging loop:
> Hypothesis → Prediction → Experiment → Observation → Conclusion → `<DONE>`

**Prerequisites:**  
- Python installed  
- VS Code with GitHub Copilot (or any LLM tool)

**Starter Artefacts:**  
You can find the artifacts [here](./problems/02-deduplication/remove_duplicates.py).

**Guidelines 2 steps to Apply:**

**Step 01:** Clearly describe the bug scenario and expected behavior
**Step 02:** Use the LLM to generate a hypothesis before asking for a fix
**Step 03:** Define a prediction (what should happen if the hypothesis is correct)
**Step 04:** Design and run experiments (print/debug statements) to validate assumptions
**Step 05:** Use observations to confirm or reject the hypothesis
**Step 06:** Repeat the process until confident and indicate completion using <DONE>

**Expected Process (AutoSD Style):**

- **Hypothesis:** The first element comparison is incorrect due to negative indexing (nums[-1])
- **Prediction:** At index 0, the last element of the list is incorrectly used
- **Experiment:** Print index, current value, and previous value during iteration
- **Observation:** At index 0, nums[-1] refers to the last element, causing incorrect comparison
- **Conclusion:** Hypothesis supported
- **New Hypothesis:** Handle the first element separately
- **Fix:** Initialize result with first element and start loop from index 1
- **<DONE>** when output matches expected result

**Time Estimate:** approx. 20 min

---

**Evaluation:** Use the [here](./Evaluation.md) file to assess your solutions.



---

### Problem D_2: The Silent Average Bug (No Tests Available)

**Task Description:**
The function below is supposed to compute the average of a list of numbers. It has a bug. Your job is to find and fix it — but *without* running the code and *without* simply asking the AI to "fix it." You must use the **Explain-Then-Fix** approach (Guideline 1):

1. Prompt the LLM to explain the code line-by-line and compare it to the spec.
2. Only then prompt it to produce a fix.

Compare this to a "baseline" attempt where you just paste the code and say "fix the bug."

**Starter Code (Python):**
```python
def running_average(numbers: list[float]) -> list[float]:
    """
    Returns a list where each element i is the average of
    numbers[0..i] (inclusive).

    Example:
        running_average([2, 4, 6]) -> [2.0, 3.0, 4.0]
    """
    result = []
    total = 0
    for i, n in enumerate(numbers):
        total += n
        result.append(total / i)   # <-- bug is here
    return result
```

**Guidelines to Apply:**
- Guideline 1: Explain-Then-Fix (Rubber Duck Self-Debugging)


*Turn 1 (Explain):*
```
You are a careful Python code reviewer.

Explain what the following function does, line by line.
Then state whether it correctly implements this specification:
"Returns a list where element i equals the average of numbers[0] through numbers[i] inclusive."
Identify any discrepancy between the code and the spec.

def running_average(numbers: list[float]) -> list[float]:
    result = []
    total = 0
    for i, n in enumerate(numbers):
        total += n
        result.append(total / i)
    return result
```

*Turn 2 (Fix):*
```
Based on your explanation above, provide a corrected version of the function.
```

**Time Estimate:** 10 minutes
---

### Problem D_2: Off-by-One in Binary Search (Execution Trace Available)

**Task Description:**
The binary search below passes some inputs but crashes or returns wrong results on others. You have a unit test and its output. Use the **Execution Trace Feedback** approach (Guideline 2): paste the full execution output into your prompt and ask the LLM to explain and fix.

**Starter Code (Python):**
```python
def binary_search(arr: list[int], target: int) -> int:
    """
    Returns the index of target in sorted arr, or -1 if not found.
    """
    lo, hi = 0, len(arr)          # bug: hi should be len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Failing Unit Test:**
```python
arr = [1, 3, 5, 7, 9]
assert binary_search(arr, 9) == 4
```

**Execution Output to paste into your prompt:**
```
IndexError: list index out of range
  File "solution.py", line 8, in binary_search
    if arr[mid] == target:
```

**Guidelines to Apply:**
 Feed Execution Traces Back into the Prompt

**Suggested Prompt (Guideline-Driven Attempt):**
```
The following Python function is supposed to return the index of a target value
in a sorted list, or -1 if not found.


def binary_search(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

[FAILING TEST]
arr = [1, 3, 5, 7, 9]
assert binary_search(arr, 9) == 4

[EXECUTION OUTPUT]
IndexError: list index out of range
  File "solution.py", line 8, in binary_search
    if arr[mid] == target:

Explain what went wrong and provide a corrected version.
```



---

## 4. References

[1] Chen, X., Lin, M., Schärli, N., & Zhou, D. (2024). Teaching Large Language Models to Self-Debug. *ICLR 2024*. https://arxiv.org/abs/2304.05128
[2] Hunt, A., & Thomas, D. (2000). *The Pragmatic Programmer*. Addison Wesley.

---

*Template version: 1.0 | Topic: Debugging | Team 6 | Spring Semester 2026*




