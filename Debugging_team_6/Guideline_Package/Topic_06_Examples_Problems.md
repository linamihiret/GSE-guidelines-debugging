### Problem 01: Debugging Incorrect Average Calculation

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

**Guidelines 3 steps to Apply:**

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

### Problem 02: Debugging List Deduplication Logic

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

**Guidelines 3 steps to Apply:**

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



