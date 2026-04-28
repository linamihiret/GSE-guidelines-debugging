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

**Evaluation Criteria:**  
- **Root Cause Identification:** Correctly identifies that division by zero occurs when there are no valid (non-negative) scores.  
- **Use of Experiments:** Includes meaningful debug steps (e.g., printing total and count of valid values).  
- **Evidence-Based Reasoning:** Uses **test results** to support the fix, showing that the fix prevents division by zero errors.  
- **Correct Fix:** Adds a check for `count == 0` and raises a **ValueError** when no valid scores are found.  
- **Completion Signal:** Clearly indicates debugging completion using `<DONE>` or equivalent when the output matches expected results.

---

**Common Mistakes to Avoid:**  
- **Skipping Hypothesis Testing:** Not experimenting to identify the root cause of division by zero.  
- **Incorrect Fix:** Applying a fix without thoroughly verifying it through multiple test cases.  
- **No Edge Case Handling:** Failing to handle edge cases, such as **empty lists**, **lists with only negative values**, or **lists with all zero values**.  
- **Blind Trust in LLM Fixes:** Accepting fixes generated by AI without reasoning or validation.

---
