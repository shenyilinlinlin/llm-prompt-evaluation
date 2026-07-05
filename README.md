# LLM Prompt Evaluation

This project explores how prompt design affects the performance of large language models (Gemini-1.5-Flash) on structured code generation tasks.

We conduct systematic experiments comparing original prompts vs. improved prompts and evaluate model outputs using handcrafted test cases.

---

## 🔍 Project Overview

This project contains two tasks:

### Option A: Parentheses Group Parsing
Given a string, extract outermost balanced parentheses groups and count unmatched characters.

### Option B: Digit Counting Problem
Count numbers that start with a digit x OR end with digit y under constraints.

---

## 🧪 Methodology

We evaluate LLM outputs using:

- 10+ unit-style test cases per task
- Edge cases (invalid input, nested structures, boundary values)
- Comparison between:
  - original prompt behavior
  - improved prompt behavior

We iteratively refine prompts to improve correctness and robustness.

---

## 📊 Key Findings

- Adding explicit constraints significantly improves correctness
- LLMs often fail on:
  - nested structure parsing
  - ambiguity in input handling
- Few-shot examples improve consistency
- Overly vague prompts lead to incomplete or incorrect logic

---

## 📁 Structure

- option_a/ : parentheses parsing task
- option_b/ : digit counting task
- evaluation/ : test runner utilities
- notebooks/ : prompt experiments

---

## ⚙️ How to Run

```bash
python evaluation/run_tests.py
