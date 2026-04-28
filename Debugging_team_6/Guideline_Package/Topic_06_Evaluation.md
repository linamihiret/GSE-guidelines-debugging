## 2. Evaluation Specifically for Example Problems

---

### Problem 01: Debugging Incorrect Average Calculation

**Evaluation Description:**  
A strong solution should not only fix the bug but also demonstrate a clear **AutoSD reasoning process**. Special emphasis should be placed on correctly identifying the **root cause (incorrect counting logic)** and validating it using **execution-based evidence**.

---

**Prompts to Follow (AutoSD Workflow):**

- **Prompt 1 (Hypothesis Generation):**  
  `"Analyze the following function and propose a hypothesis explaining why it produces incorrect results when negative values are present. Do not provide a fix yet."`

- **Prompt 2 (Prediction):**  
  `"If your hypothesis is correct, what should we observe during execution? Explain what values (e.g., total, count) might look like."`

- **Prompt 3 (Experiment Design):**  
  `"Suggest a debugging experiment (e.g., print statements) to test this hypothesis. Show exactly what should be added to the code."`

- **Prompt 4 (Observation & Analysis):**  
  `"Given the following execution output, does it support or reject the hypothesis? Explain your reasoning."`

- **Prompt 5 (Refinement / Iteration):**  
  `"Based on the conclusion, propose the next hypothesis or confirm whether debugging is complete."`

- **Prompt 6 (Completion Signal):**  
  `"If you are confident the bug is fully understood and fixed, explicitly output <DONE>. Otherwise, continue debugging."` 

---

**Correct Solution Code:**  
You can find the solution [here](./problems/01-debugging-average/solution.py).

---

**Evaluation Criteria:**  
- **Root Cause Identification:** Correctly identifies that negative values are included in the count but not in total  
- **Use of Experiments:** Includes meaningful debug steps (e.g., printing total and count)  
- **Evidence-Based Reasoning:** Uses observed outputs to support conclusions  
- **Correct Fix:** Moves `count += 1` inside the conditional block  
- **Completion Signal:** Clearly indicates debugging completion using `<DONE>` or equivalent  

---

**Common Mistakes to Avoid:**  
- **Direct Fix Without Reasoning:** Skipping hypothesis and experimentation steps  
- **Incorrect Counting Logic:** Fixing total but not count  
- **No Edge Case Handling:** Ignoring cases where all values are invalid  
- **Blind Trust in LLM Output:** Accepting fixes without verifying via execution  

---

### Problem 02: Debugging List Deduplication Logic

**Evaluation Description:**  
A strong solution should demonstrate the ability to identify **indexing-related bugs** and validate them through step-by-step reasoning. Special emphasis should be placed on understanding **boundary conditions (first element handling)**.

---

**Prompts to Follow (AutoSD Workflow):**

- **Prompt 1 (Hypothesis Generation):**  
  `"Analyze the following function and propose a hypothesis explaining why it produces incorrect results. Focus on indexing and boundary conditions. Do not provide a fix yet."`

- **Prompt 2 (Prediction):**  
  `"If your hypothesis is correct, what should we observe during execution, especially at index 0? Explain expected values for nums[i] and nums[i-1]."`

- **Prompt 3 (Experiment Design):**  
  `"Suggest a debugging experiment (e.g., print index, current value, and previous value) to test this hypothesis. Show exactly what should be added to the code."`

- **Prompt 4 (Observation & Analysis):**  
  `"Given the execution output, does it support or reject the hypothesis? Explain why the behavior at index 0 is correct or incorrect."`

- **Prompt 5 (Refinement / Iteration):**  
  `"Based on the conclusion, propose the next hypothesis or confirm whether the issue is fully understood."`

- **Prompt 6 (Completion Signal):**  
  `"If you are confident the bug is fully understood and fixed, explicitly output <DONE>. Otherwise, continue debugging."`
  

---

**Correct Solution Code:**  
You can find the solution [here](./problems/02-deduplication/solution.py).

---

**Evaluation Criteria:**  
- **Root Cause Identification:** Correctly identifies issue with `nums[i-1]` at index 0  
- **Use of Experiments:** Prints index and values to observe incorrect comparisons  
- **Evidence-Based Reasoning:** Uses execution output to validate hypothesis  
- **Correct Fix:** Handles first element separately and iterates from index 1  
- **Completion Signal:** Indicates completion using `<DONE>` or equivalent  

---

**Common Mistakes to Avoid:**  
- **Ignoring Boundary Cases:** Not handling index 0 properly  
- **Incorrect Fix:** Changing logic without understanding cause  
- **No Experimentation:** Skipping debug prints or observations  
- **Partial Deduplication:** Fix works only for specific inputs  

---

### Problem 03: Debugging Division by Zero in Average Calculation

**Evaluation Description:**  
A strong solution should not only fix the bug but also demonstrate a clear **AutoSD reasoning process**. Special emphasis should be placed on correctly identifying the **root cause (division by zero)** and validating it using **execution-based evidence**.

---

**Test Cases:**  
- **Test Case 1:** [15, 25, 35] → 25.0  
- **Test Case 2:** [5, 0, 10] → 5.0  
- **Test Case 3 (Edge Case):** [] → Error or handled case (empty list or division by zero)  
- **Test Case 4 (Edge Case):** [-1, -3, -5] → Error or handled case (no valid scores)  
- **Test Case 5 (Edge Case):** [0, 0, 0] → 0.0 (all zeroes as valid inputs)

---

**Correct Solution Code:**  
You can find the solution [here](./problems/03-average-calculation-debugging/solution.py).

---

**Evaluation Criteria: Guideline 2**  
- **Root Cause Identification:** Correctly identifies that division by zero occurs when there are no valid (non-negative) scores.  
- **Use of Experiments:** Includes meaningful debug steps (e.g., printing total and count of valid values).  
- **Evidence-Based Reasoning:** Uses **test results** to support the fix, showing that the fix prevents division by zero errors.  
- **Correct Fix:** Adds a check for `count == 0` and raises a **ValueError** when no valid scores are found.  
- **Completion Signal:** Clearly indicates debugging completion using `<DONE>` or equivalent when the output matches expected results.

---

**Common Mistakes to Avoid:**  
- **Skipping Hypothesis Testing:** Not experimenting to identify the root cause of division by zero.  
- **Incorrect Fix:** Applying a fix without thoroughly verifying it through multiple test cases.  
- **No Edge Case Handling:** Failing to handle edge cases, such as **empty lists**, **lists with only negative values**, or **lists with all### General Evaluation Criteria

These criteria apply to *any* debugging task in this topic, regardless of the specific problem.

**Correctness**
Does the fixed code produce the correct output for all provided test cases, including edge cases?

**Bug Localisation**
Did the LLM (or the student guided by the LLM) correctly identify *where* the bug is, not just produce a fix that happens to work? A good debugging session includes a clear explanation of *why* the original code was wrong.

**Explanation Quality**
Is the code explanation accurate and specific? It should reference actual variable names, line numbers, and the logical discrepancy between implementation and spec — not vague statements like "the code has an error."

**Guideline Adherence**
- For Guideline 1 (Explain-Then-Fix): Was a two-turn prompt used? Did turn 1 produce an explanation *before* a fix was requested?
- For Guideline 2 (Execution Trace): Was the full, unparaphrased execution output included in the prompt?

**Fix Quality**
Is the fix minimal (changes only what is necessary)? Does it introduce any new bugs? Is it readable?

**Edge Case Handling**
Does the fix handle the edge cases that triggered the original bug, plus at least one additional boundary case?

---

## 2. Evaluation Specifically for Example Problems

### Problem D_1: The Silent Average Bug

**Evaluation Description:**
The correct fix must resolve *both* the ZeroDivisionError on empty/first-element input and the wrong denominator for all subsequent elements.

**Test Cases:**

| Input | Expected Output |
|---|---|
| `running_average([2, 4, 6])` | `[2.0, 3.0, 4.0]` |
| `running_average([10])` | `[10.0]` |
| `running_average([])` | `[]` (or raise ValueError — must be consistent with spec) |
| `running_average([0, 0, 0])` | `[0.0, 0.0, 0.0]` |

**Correct Solution:**
```python
def running_average(numbers: list[float]) -> list[float]:
    result = []
    total = 0
    for i, n in enumerate(numbers):
        total += n
        result.append(total / (i + 1))   # fix: i+1 is the count of elements seen
    return result
```

**Scoring Rubric for Explain-Then-Fix:**

| Criterion | Full marks | Partial | Zero |
|---|---|---|---|
| Turn 1 explanation identifies the `/ i` issue | Yes, explicitly | Mentions "division problem" vaguely | No mention |
| Turn 1 explanation identifies ZeroDivisionError risk | Yes | Mentions only wrong result, not crash | No |
| Turn 2 fix is correct for all test cases | All 4 pass | 2–3 pass | <2 pass |
| Fix is minimal (only the denominator changes) | Yes | Yes but adds unnecessary code | Rewrites entire function |

**Common Mistakes to Avoid:**
- Fixing the crash but not the wrong-denominator logic (e.g., adding an `if i == 0: continue` guard instead of using `i + 1`).
- Baseline prompt producing a "correct-looking" fix that passes the happy path but still fails on `running_average([5])` because `total / i` with `i = 0` was never tested.
- Accepting a fix without running it against the edge-case tests.

---

### Problem D_2: Off-by-One in Binary Search

**Evaluation Description:**
The correct fix must change `hi = len(arr)` to `hi = len(arr) - 1`. The fix must be validated against both the failing test and at least two additional inputs.

**Test Cases:**

| Input | Expected Output |
|---|---|
| `binary_search([1,3,5,7,9], 9)` | `4` |
| `binary_search([1,3,5,7,9], 1)` | `0` |
| `binary_search([1,3,5,7,9], 6)` | `-1` |
| `binary_search([], 1)` | `-1` |

**Correct Solution:**
```python
def binary_search(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1    # fix: exclusive upper bound → inclusive
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

**Scoring Rubric for Execution Trace Feedback:**

| Criterion | Full marks | Partial | Zero |
|---|---|---|---|
| Prompt included verbatim execution output | Yes | Paraphrased it | Not included |
| LLM explanation correctly links `IndexError` to `hi = len(arr)` | Yes | Mentions off-by-one generically | No |
| Fix passes all 4 test cases above | Yes | 2–3 | <2 |
| Student verified fix by running it | Yes | Says they did, unclear | No |

**Common Mistakes to Avoid:**
- Changing the loop condition to `lo < hi` instead of fixing the initial `hi` assignment — this changes the algorithm's semantics for single-element arrays.
- Paraphrasing the error message in the prompt ("it gives an IndexError") instead of including the actual traceback — models perform better with the raw trace.
- Not testing the empty array case after fixing.

---

### Counterexample: Race Condition (Limitation Demo)

**Evaluation Description:**
The goal here is *not* to fix the code with the LLM, but to demonstrate that Guideline 1 (Explain-Then-Fix) fails to detect this class of bug.

**Expected Observation:**
- Baseline attempt (just ask LLM to fix): LLM likely says the code looks correct, or adds a lock without explaining why.
- Guideline 1 attempt (explain first): LLM explains the code correctly at the static level but does **not** identify the race condition, because it cannot observe non-deterministic interleaving.
- This is a valid and instructive **counterexample** — document it as such in your portfolio.

**Correct Fix (for reference):**
```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)  # reliably 200_000
```

**Guideline Refinement (document this in your portfolio):**
> Guideline 1 (Explain-Then-Fix) works when the bug is statically detectable. It **fails** for concurrency bugs, I/O side effects, and non-deterministic failures. In these cases, switch to Guideline 2 with actual runtime evidence, or escalate to a human reviewer.

---
 zero values**.  
- **Blind Trust in LLM Fixes:** Accepting fixes generated by AI without reasoning or validation.

---


