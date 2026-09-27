# Public Solution Review

## Overview
This document tracks current public work specific to the Gemma 4 Developer Agent competition, including notebooks, graph-guided approaches, and test-aware repairs.

## Tracked Methods

### METHOD: Evidence-First Baseline
- **SOURCE:** Initial architecture planning.
- **CORE IDEA:** Prioritize localization, evidence gathering, and targeted edits before attempting large reasoning loops.
- **REQUIRED RESOURCES:** Standard vLLM environment, basic tools (`read_file`, `search_similar_code`).
- **EXPECTED BENEFIT:** Reliable baseline, high precision on easier issues.
- **COST:** Minimal, fast execution.
- **LIMITATIONS:** Fails on deeply hidden root causes.
- **OUR EXPERIMENT:** Experiment E01.

### METHOD: Semantic Localization Improvements (Agentless-inspired)
- **SOURCE:** General Kaggle discussions & Public Notebooks.
- **CORE IDEA:** Pre-filter context using dense embeddings before the LLM takes over.
- **REQUIRED RESOURCES:** Embeddings DB (`embeddings/*.npz`).
- **EXPECTED BENEFIT:** Avoid context truncation limits.
- **COST:** Time spent orchestrating numpy arrays.
- **LIMITATIONS:** Requires precise retrieval thresholds.
- **OUR EXPERIMENT:** Pending E02.
