## 2. Evaluation Specifically for Example Problems

---

### Problem 01: Debugging Incorrect Average Calculation

**Evaluation Description:**  
A strong solution should not only fix the bug but also demonstrate a clear **AutoSD reasoning process**. Special emphasis should be placed on correctly identifying the **root cause (incorrect counting logic)** and validating it using **execution-based evidence**.

---

**Test Cases:**  
- **Test Case 1:** [10, 20, 30] → 20.0  
- **Test Case 2:** [10, -5, 15] → 12.5  
- **Test Case 3 (Edge Case):** [-1, -2, -3] → Error or handled case (division by zero)  
- **Test Case 4 (Edge Case):** [0, 0, 10] → 3.33 (or expected handling depending on logic)  

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

**Test Cases:**  
- **Test Case 1:** [1, 1, 2, 2, 3] → [1, 2, 3]  
- **Test Case 2:** [1, 1, 1, 1] → [1]  
- **Test Case 3 (Edge Case):** [] → []  
- **Test Case 4 (Edge Case):** [5] → [5]  

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