# Kaggle Gemma 4 Developer Agent - Winning Strategies

This document synthesizes the core competitive insights extracted from "The Google Gemma 4 Developer Agent Competition: An Exhaustive Strategic and Technical Blueprint".

## 1. The Fallacy of Graph and Semantic Tools
While semantic graphs (AST) and embeddings are provided, they are dangerous to rely upon as primary navigation mechanics.
- **Embedding Failures:** The embedding space is dominated by singular directional variance, yielding false positives. `search_similar_code` fails with natural language.
- **AST Graph Omissions:** The NetworkX AST graphs explicitly omit asynchronous function definitions. Because ~52% of the dataset is FastAPI (heavy async), using `get_code_neighbors` results in silent truncation, rendering the agent blind.
- **Conclusion:** Treat graph tools strictly as secondary heuristics. The primary localization engine must be built upon deterministic lexical retrieval (e.g., `git grep -n`, `rg`).

## 2. Flat vs. Nested Agent Architectures (E12 > E11)
- Multi-agent delegation within the SWE-bench harness introduces significant token bloat and frequent parsing exceptions.
- A highly optimized, **flat single-agent architecture** (where all tools are mounted to a single monolithic entity) eliminates routing overhead.
- This ensures the LLM maintains a cohesive, uninterrupted view of the codebase, improving determinism.

## 3. Hardware Constraints & Generation Configurations
- **Memory Envelopes:** The agent is severely VRAM constrained on dual T4 GPUs. Prolonged exploration exhausts the KV cache.
- **Token Economics:**
  - `temperature: 0.1` and `top_p: 0.95` to eliminate sampling hallucinations.
  - `thinking_budget: 2048` tokens allows CoT logic.
  - **Crucial:** `include_thoughts: false` must be set. Forwarding thoughts back into context causes exponential prompt bloat and OOM failures.

## 4. SWE-Bench Topography & Micro-Surgical Patches
- **Dataset Make-up:** FastAPI (~51.94%), Rich (~37.21%), Requests (~10.08%). The system prompt should expect these frameworks.
- **Minimal Patches:** 50% of benchmark issues are resolved in <= 12 lines, 75% in <= 45 lines.
- **Axiom:** Absolutely avoid refactoring. Enforce minimal, localized payloads via `edit_file`. Explicitly bar the use of `write_file` except for `/tmp/` reproducer scripts.

## 5. The Optimal 4-Phase Execution Pipeline
The strategy implements an "Agentless" style localization with SWE-agent's defensive execution principles.

**Phase I: Agentless Deterministic Localization**
- Ignore stochastic/AST tools initially.
- Extract exact filenames and unique literals from the issue.
- Execute rapid `run_command` with `git grep -n`.
- Issue highly constrained `read_file` (max 150 lines).

**Phase II: Inline Offline Reproduction**
- Do not run the entire test suite immediately (often fails due to environment).
- Synthesize a minimal reproducer using a shell heredoc (`cat << 'EOF' > /tmp/repro.py`).
- Run with strict timeout (`timeout 5s python3 /tmp/repro.py`).

**Phase III: Micro-Surgical, Defensive Repair**
- Formulate a fix < 15 lines.
- Use `edit_file` with unique contextual boundaries in `old_string`.
- Execute `python3 -m py_compile` immediately after to catch syntax errors.

**Phase IV: Validation and Terminal Submission**
- Re-run `/tmp/repro.py`.
- Perform a narrow regression check using `pytest` on the specific module's test file.
- Purge artifacts, check `git diff`, and invoke `submit_patch()`.

## 6. Budget & Pacing
- The global budget is 12 hours.
- Per-task budgets must be aggressive to iterate across 129 repos without hitting the global kill switch:
  - `timeout_seconds: 60` (per command)
  - `max_time_minutes: 5` (per task)
