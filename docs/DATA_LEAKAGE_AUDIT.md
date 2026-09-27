# Data Leakage Audit

## Overview
The raw `tasks.jsonl` contains the following fields:
- `instance_id` (AGENT_TASK)
- `repo` (AGENT_TASK)
- `base_commit` (RESEARCH_ONLY - although the harness uses it for snapshots, the agent code should just observe its local tree, preventing leakage).
- `patch` (RESEARCH_ONLY / GOLD) - MUST NEVER EXPOSE
- `test_patch` (RESEARCH_ONLY / GOLD) - MUST NEVER EXPOSE
- `problem_statement` (AGENT_TASK)
- `hints_text` (AGENT_TASK)
- `created_at` (RESEARCH_ONLY)

## Sanitization
A `task_sanitizer.py` has been implemented in `evaluation/`.
During any mocked local execution, tasks are parsed from JSON and immediately passed through this sanitizer *before* the prompt or context is formed.

Unit tests in `tests/test_task_sanitizer.py` assert that `patch` and `test_patch` are hard-dropped.
