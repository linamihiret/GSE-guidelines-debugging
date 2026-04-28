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

*Guideline 1 Evaluation:** 

**Step 1 — Did the model correctly locate the bug?**
Read the explanation the model produced. It should name the exact variable, line, or logical condition that is wrong — not just say "there is an error." If it says something like `"the division on line 5 uses i instead of i+1, which causes a ZeroDivisionError when i = 0"` that is a good localisation. If it says `"the code has a problem with the loop"` without being specific, that is not.

**Step 2 — Is the explanation accurate?**
Compare the model's explanation to what you know the bug actually is. Does the explanation correctly describe the cause-and-effect chain? A wrong but confident explanation is worse than no explanation — it means the fix may be incorrect even if it looks plausible.

**Step 3 — Did the prompt follow the right guideline?**
For Guideline 1 (Explain-Then-Fix): check that there were two separate turns — an explanation turn first, then a fix turn. If the model jumped straight to a fix in turn 1 without explaining, the guideline was not applied.
For Guideline 2 (Execution Trace): check that the exact error output from running the code was pasted verbatim into the prompt. If the error was paraphrased or summarised, the guideline was not applied correctly.

**Step 4 — Does the fix pass all test cases?**
Run the fixed code against the test cases listed for the problem. Every case must pass — not just the happy path. Pay particular attention to the edge cases (empty input, single element, value not found) because those are the ones the baseline attempt most often misses.

**Step 5 — Is the fix minimal?**
Count the lines changed. A good fix changes only what is necessary. If the model rewrote the entire function to fix a one-character bug, that is not a minimal fix and introduces unnecessary risk of new bugs. Prefer a fix that is a strict improvement over the original.

**Step 6 — Compare baseline vs. guideline-driven.**
Write two sentences: what the baseline attempt produced and what the guideline-driven attempt produced. Which one found the bug more precisely? Which fix was more correct on the first try? This comparison is what goes in your evidence log.

---



### Step 1 — Run the Guideline 1 attempt (two turns)

**Turn 1 — paste this exactly:**

```
You are a careful Python code reviewer.

Explain what the following function does, line by line.
Then state whether it correctly implements this specification:
"Returns a list where element i equals the average of
numbers[0] through numbers[i] inclusive."
Identify any discrepancy between the code and the spec,
including any edge cases that would cause a crash.

def running_average(numbers: list[float]) -> list[float]:
    result = []
    total = 0
    for i, n in enumerate(numbers):
        total += n
        result.append(total / i)
    return result
```

Read the explanation carefully before continuing.

**Turn 2 — paste this exactly:**

```
Based on your explanation above, provide a corrected version
of the function. Change only what is necessary to fix the bug.
```

### Step 2 — Check the explanation from Turn 1

Ask yourself these questions in order:

Did the explanation mention that `enumerate` starts `i` at `0`? If not, it missed the root cause.

Did the explanation say that `total / i` will crash when `i = 0`? If not, it missed the most critical edge case.

Did the explanation say that even after the first element, `i` is still wrong because the count of elements seen is `i + 1`, not `i`? If not, it caught the crash but not the logic error.

If the answer to all three is yes, the explanation is high quality. If only the first or second question is yes, the explanation is partial. If none are yes, the explanation failed and the guideline was not effective on this attempt — record that as a counterexample.

### Step 3 — Check the fix from Turn 2

Run the fixed code against these four inputs and confirm the outputs match:

`running_average([2, 4, 6])` should return `[2.0, 3.0, 4.0]`

`running_average([10])` should return `[10.0]`

`running_average([])` should return `[]` — or raise a `ValueError` if the spec says so, but it must not crash silently

`running_average([0, 0, 0])` should return `[0.0, 0.0, 0.0]`

If all three pass, the fix is correct. If `running_average([10])` fails, the model fixed the wrong-denominator case but still crashes on a single element. If `running_average([2, 4, 6])` fails, the model may have just added an `if i == 0: continue` guard — which avoids the crash but produces wrong results for every other element.

### Step 4 — Check fix minimality

The only correct minimal fix is changing `total / i` to `total / (i + 1)`. If the model rewrote the loop with `range(len(numbers))` instead of `enumerate`, or added extra guard clauses, note it,  it works but is not minimal.

### Step 5 — Common mistakes to watch for

If the baseline produced a fix that passes `running_average([2, 4, 6])` but fails `running_average([10])`, record that as evidence that the baseline missed the edge case. This is the most common baseline failure on this problem.

If the guideline-driven fix added `if not numbers: return []` as a separate guard rather than relying on the loop doing nothing on an empty list, that is acceptable — it is explicit and readable — but make a note that it is not the minimal change.

### Correct reference solution

```python
def running_average(numbers: list[float]) -> list[float]:
    result = []
    total = 0
    for i, n in enumerate(numbers):
        total += n
        result.append(total / (i + 1))   # i+1 is the count of elements seen so far
    return result
```

---


## 5. References

[1] Chen, X., Lin, M., Schärli, N., & Zhou, D. (2024). Teaching Large Language Models to Self-Debug. *ICLR 2024*. https://arxiv.org/abs/2304.05128

---

*Template version: 2.0 | Topic: Debugging | Team 6 | Spring Semester 2026*






