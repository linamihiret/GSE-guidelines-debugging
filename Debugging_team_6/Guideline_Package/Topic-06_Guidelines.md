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

### Guideline N: `[Title]`

(Repeat the same structure for each guideline.)

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
