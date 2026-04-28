# Topic-06_Guidelines.md

---

## Team Information

**Team Name:** `Debugging Team`  
**Topic:** `Debugging`  
**Date:** `28.04.2026`  
**Authors:** `Mansi Sawant, `

---

## 1. Unified Guidelines

> **Note:** These are the merged, refined guidelines that your team recommends to the class. Each guideline should be actionable, specific, and usable during real SE/coding tasks.

### Guideline 1: `[Title]`

**Description:**  
What should developers do (i.e., state it clearly and concretely)?

**Reasoning:**  
Explain *why* this guideline is important. Reference:
- Relevant literature readings
- Grey literature (blogs, documentation, etc.)
- LLM experimentation insights

**Example:**  
Provide a (simple) illustrative example (code snippet, pseudo-code, or description).

**When to Apply:**  
Describe the conditions where this guideline is most effective.

**When to Avoid:**  
Describe edge cases or situations where this guideline may not work well.

---

### Guideline 3: `AutoSD: LLM-Driven Scientific Debugging​`

**Description:**  
Developers should use LLMs (e.g., GitHub Copilot, ChatGPT) as **reasoning partners** by following a structured debugging process instead of asking for direct fixes.
Specifically, developers should:
1. Ask the LLM to generate a **hypothesis** about the bug  
2. Define a **prediction** (what should happen if the hypothesis is correct)  
3. Design and run an **experiment** (e.g., print/debug statements or test execution)  
4. Observe the actual output (**observation**)  
5. Ask the LLM to draw a **conclusion**  
6. Repeat the process until confident and indicate completion using `<DONE>`  

---

**Reasoning:**  
This guideline is based on the concept of **Scientific Debugging**, where developers iteratively form and test hypotheses to understand program behavior.
- **Research literature:**  
  The AutoSD approach demonstrates that LLMs can emulate this process by generating hypotheses, interacting with code via execution, and producing reasoning traces that improve debugging quality and explainability. Developers using such structured explanations were shown to **make more accurate decisions when evaluating fixes**.  

- **Why it works:**  
  - Aligns with how developers naturally debug (hypothesis → test → refine)  
  - Uses **real execution results**, reducing hallucination  
  - Produces **transparent reasoning**, improving trust and understanding  
  - Allows the system to signal confidence via `<DONE>`  

- **LLM experimentation insights:**  
  In practice, directly asking for fixes often leads to:
  - unclear reasoning  
  - incorrect or unverifiable solutions  
  Using AutoSD instead leads to:
  - better root cause identification  
  - easier validation through observable outputs  
  - improved learning for developers  

---

**Example:**  
python
def calculate_average(scores):
    total = 0
    count = 0
    for s in scores:
        if s >= 0:
            total += s
        count += 1
    return total / count

**Step 1 – Hypothesis (LLM):**
Negative values are excluded from the total but still included in the count.

**Step 2 – Prediction:**
If true, the denominator will be larger than expected.

**Step 3 – Experiment:**
Add debug prints:
print("Total:", total, "Count:", count)

**Step 4 – Observation:**
Count increases even when value is negative.

**Step 5 – Conclusion:**
Hypothesis is supported.

**Step 6 – Fix:**
Move count += 1 inside the condition.
if s >= 0:
    total += s
    count += 1

**Step 7 – Completion:**
Output is correct → <DONE> / Yes, the debugging is complete.

---

**When to Apply:**  
- When debugging unfamiliar or complex code
- When correctness and reliability are important
- When developers need to understand the root cause, not just fix the issue
- When learning debugging or teaching programming concepts
- When validating LLM-generated fixes

**When to Avoid:**  
- Very simple or trivial bugs where direct fixes are sufficient
- Time-critical scenarios where rapid patching is preferred over explanation
- When execution/testing environment is unavailable (no way to run experiments)
- When poor experiments (e.g., incorrect debug statements) may mislead reasoning
- When over-reliance on LLM reasoning replaces developer judgment

---

**Sources**

Kang, S., Chen, B., Yoo, S., & Lou, J.-G. (2025). *Explainable automated debugging via large language model-driven scientific debugging*. Empirical Software Engineering, 30, 45. https://doi.org/10.1007/s10664-024-10594-x

---

### Guideline 4: `RepairAgent: Autonomous LLM-Based Program Repair`

**Description:**  
Developers should use LLM-based autonomous agents (e.g., RepairAgent) for debugging tasks that require more than a direct one-shot fix. Instead of only asking the LLM for code changes, the agent should follow a structured repair workflow.

Specifically, developers should allow the agent to:

1. Analyze failing tests, logs, or error messages  
2. Read relevant source code files and methods  
3. Generate a **hypothesis** about the bug location or cause  
4. Search the codebase for similar logic or repair patterns  
5. Suggest and apply a patch automatically  
6. Run tests to validate the patch  
7. Retry with new information until a correct fix is found  

---

**Reasoning:**  
This guideline is based on the concept of **Autonomous Program Repair**, where the LLM behaves like a developer that investigates, tests, and repairs bugs step by step.

- **Research literature:**  
The RepairAgent approach shows that LLMs become more effective when they are allowed to use tools such as reading code, searching files, generating patches, and executing tests. Instead of relying on one prompt, the system continuously gathers information and improves its repair attempts. RepairAgent successfully fixed **164 real-world bugs**, including **39 bugs not solved by previous methods**.

- **Why it works:**  
  - Mimics how real developers debug (understand → search → fix → test → refine)  
  - Uses external tools instead of relying only on memory  
  - Reduces hallucinated fixes through testing and validation  
  - Handles multi-line and more complex bugs better  
  - Improves repair accuracy through multiple iterations  

- **LLM experimentation insights:**  
  In practice, directly asking for fixes often leads to:

  - incomplete patches  
  - wrong assumptions  
  - missing project context  
  - unverifiable code changes  

  Using RepairAgent instead leads to:

  - better bug understanding  
  - more reliable fixes  
  - automatic validation with tests  
  - improved debugging workflow  

---

**Example:**  

```python id="f40hk7"
def divide(a, b):
    return a / b

### Step 1 – Bug Report:
Program crashes when `b = 0`

### Step 2 – Hypothesis (LLM Agent):
The function has no protection against division by zero.

### Step 3 – Search & Analyze:
Agent reads function and checks failing tests.

### Step 4 – Patch Generation:

```python id="i5g0rz"
def divide(a, b):
    if b == 0:
        return 0
    return a / b


### Step 5 – Validation:
Run tests again.

### Step 6 – Result:
Tests pass successfully.

### Step 7 – Completion:
Correct patch found → `<DONE>`

---

## When to Apply:

- When debugging medium or complex bugs  
- When multiple files or functions are involved  
- When failing tests are available  
- When developers need automated bug fixing support  
- When traditional prompting gives weak results  
- In CI/CD or automated maintenance workflows  

---

## When to Avoid:

- Very small syntax errors or trivial bugs  
- Time-critical situations needing instant manual fixes  
- Projects without tests or validation setup  
- Safety-critical systems requiring manual approval only  
- When debugging cost/token usage must stay minimal  

---

## Sources

Bouzenia, I., Devanbu, P., & Pradel, M. (2025). *RepairAgent: An autonomous, LLM-based agent for program repair*. IEEE/ACM 47th International Conference on Software Engineering (ICSE). https://arxiv.org/pdf/2403.17134

---

## 2. Raw Guidelines (Source Documents)

> **Note:** Include the original guidelines from each of the three sources before merging. This shows your curation process.

### 2.1 Guidelines from Literature Readings

**Readings Assigned:**  
- `[Primary reading 1]`  
- `[Primary reading 2]`  
- `[Additional required readings]`

**Extracted Guidelines:**  
For each relevant guideline from readings:

**Guideline X.Y: [Title]**  
**Source:** `[Citation]`  
**Description:** `[What the reading says]`  
**Reasoning:** `[Why the reading gives for this guideline]`  
**Example:** `[Any example from the reading]`

---

### 2.2 Guidelines from Grey Literature / Practitioner Sources

**Sources Explored:**  
- `[Blog post 1]`  
- `[Documentation 1]`  
- `[Tool guide 1]`  
- `[Community discussion 1]`

**Extracted Guidelines:**  
Format same as above.

---

### 2.3 Guidelines from LLM Experimentation

**Models Used:**  
- `[e.g., GPT-5.2, Claude 4.5 Sonnet, DeepSeek Coder, GitHub Copilot (Ask vs Agent etc.)]`

**Prompts Used:**  
- `[Prompt 1]`  
- `[Prompt 2]`  
- `[Prompt 3]`

**Extracted Guidelines:**  
Format same as above.

---

## 3. References

**Literature References:**  
[1] `[Full citation]`  
[2] `[Full citation]`  

**Grey Literature References:**  
[1] `[Blog post title and URL]`  
[2] `[Documentation title and URL]`  

**LLM Prompts (Full Log):**  
See Appendix A or provide a link to a separate file with full prompt-response logs.

---

## 4. Appendix (Optional)

- **A. Full Prompt Logs:** Link to detailed LLM interaction logs
- **B. Decision Matrix:** How you decided which guidelines to merge
- **C. Conflicts Resolved:** Examples of contradictory guidelines and how you resolved them

---

## Instructions for Use

1. **Replace all `[...]` placeholders** with your team's specific content
2. **Number guidelines consecutively** (Guideline 1, Guideline 2, etc.)
3. **Cite sources properly** using academic citation style (e.g., APA, ACM)
4. **Include concrete examples** - code or textual snippets (depending on SE task) are highly recommended
5. **Be specific about applicability** - when does this guideline work vs. fail?
6. **Submit as `Topic-XX_Guidelines.md`** where `XX` is your topic number

---

## Grading Criteria (for your reference)

- ✅ **Clarity:** Guidelines are specific and actionable
- ✅ **Evidence:** Each guideline is supported by reasoning and examples
- ✅ **Curation:** Shows thoughtful merging of multiple sources
- ✅ **Practicality:** Examples are relevant to real development tasks
- ✅ **Transparency:** Raw guidelines from all three sources are included

---

*Template version: 1.0 | Last updated: 24 February 2026*
