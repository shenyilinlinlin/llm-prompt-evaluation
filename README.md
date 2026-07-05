# LLM Prompt Evaluation (Gemini-1.5-Flash)

This project is a prompt engineering and evaluation study exploring how different levels of prompt specificity affect the performance of large language models on structured code generation tasks.

We conduct controlled experiments using Gemini-1.5-Flash and analyze model behavior under progressively refined prompt conditions.

---

# 🧠 Project Motivation

Large language models are highly sensitive to how instructions are written.

This project investigates:

- How prompt detail affects correctness
- How ambiguity leads to failure cases
- How structured constraints improve reasoning consistency
- How to systematically design prompts for reliable code generation

---

# Tasks

## Option A: Parentheses Group Parsing

Given a string containing parentheses and noise characters, extract only outermost balanced groups and count unmatched parentheses.

Key challenges:
- Nested structure handling
- Depth tracking
- Unbalanced parentheses detection
- Noise filtering

---

## Option B: Digit Constraint Counting

Compute the number of n-digit integers that:
- start with digit x OR
- end with digit y

Key challenges:
- Combinatorial counting
- Overlap correction (avoid double counting)
- Leading zero edge cases
- Input validation

---

# Methodology

We design a **prompt ablation study**, where prompts are progressively refined:

### Prompt Stages:
- v1: Minimal / ambiguous prompt
- v2: Basic constraints added
- v3: Structured specification
- v4: Fully constrained + edge-case aware prompt (final)

Each version is evaluated using:
- 10+ handcrafted test cases per task
- Edge cases (invalid inputs, boundary values, malformed structures)
- Pass/fail analysis of LLM-generated outputs

---

# Key Findings

## 1. Prompt specificity strongly improves performance
More structured prompts significantly reduce hallucinated logic.

## 2. LLM failure modes observed:
- Incorrect parsing of nested structures (Option A)
- Misinterpretation of combinatorial overlap (Option B)
- Weak handling of edge cases in ambiguous prompts

## 3. Most effective prompt strategies:
- Explicit constraint enumeration
- Step-by-step rule decomposition
- Clear definition of valid input space
- Overlap and boundary case clarification

---

# Prompt Design Strategy

We iteratively improved prompts using:

- Constraint tightening
- Explicit edge-case enumeration
- Structural decomposition of logic
- Removal of ambiguity in definitions
- Addition of behavioral rules (e.g., no double counting)

---

# Models Used

- Gemini-1.5-Flash (Google GenAI API)

---

# Project Structure
option_a/
prompts.py
solution.py
tests.json

option_b/
prompts.py
solution.py
tests.json

evaluation/
run_tests.py


---

# How to Run

```bash
pip install google-genai
python evaluation/run_tests.py


