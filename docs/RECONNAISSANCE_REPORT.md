# First Execution Milestone Reconnaissance Report

## A. Repository State
- Checked initial state: found legacy files and configs from a previous failure.

## B. Cleanup Performed
- Wiped the working directory clean using `rm -rf` on all non-`.git` contents.
- Strict preservation of `.git` metadata confirmed.

## C. Kaggle Authentication Status
- `KAGGLE_API_TOKEN` confirmed present.
- CLI configured successfully.
- Verified access by querying competition files securely. (Token was not logged).

## D. Exact Competition Files Obtained
- Downloaded `HARNESS_README.md`, `tasks.jsonl`, and Docker artifacts into `competition_data/`.
- Deferred downloading massive `.npz` and `.json` graphs/embeddings to prevent accidental packaging into submission.

## E. HARNESS_README Findings
- The system heavily relies on `adk-submission`, `adk-eval-core`, and `swegemma`.
- Strict execution sandboxing separating agent vs. evaluation tasks.
- 9 official tools allowed.

## F. Official Runtime
- **Hardware**: 4x NVIDIA L4 GPUs (96 GB total VRAM).
- **Time Limits**: 12 hours global budget.
- **Constraints**: 4GiB RAM / 2 vCPUs per sandbox container.

## G. Exact Model Requirements
- `gemma-4-31b-it-qat-w4a16-ct` is the **only** permitted base model.
- Maximum context length is strictly 32,768 tokens (enforced by vLLM `max_model_len`).

## H. Exact Tool Interfaces
- `run_command(command: str)` (Timeout protected, capped stdout).
- `read_file`, `edit_file`, `write_file` (Capped returns and strict truncation).
- Graph tools: `get_code_neighbors`, `search_similar_code`, `get_code_subgraph`.
- State tools: `get_status`, `submit_patch`.

## I. Exact Submission Structure
- A standard `.zip` archive containing an `agent.yaml` at the root.
- Unpacked size must be under 3 GiB.
- No malicious path traversal.
- Strict prohibition of credentials or raw datasets in the bundle.

## J. Actual Task Dataset Structure
- `tasks.jsonl` contains 129 SWE-bench-style tasks.
- Each provides an `instance_id`, `repo`, `base_commit`, `patch`, `test_patch`, and `problem_statement`.

## K. Actual Repositories
- `fastapi/fastapi` (67)
- `Textualize/rich` (48)
- `psf/requests` (13)
- `encode/httpx` (1)

## L. Graph Structure
- Pre-computed AST/dependency graphs available as `data/graphs/<repo>.json`.
- Not yet downloaded locally.

## M. Embedding Structure
- Node embeddings available as `data/embeddings/<repo>.npz`.
- Not yet downloaded locally.

## N. Current Public Approaches
- (Pending analysis in milestone 2).

## O. Baseline Design
- See `agents/baseline/agent.yaml`. Minimal tools: `run_command`, `read_file`, `edit_file`, `write_file`, `get_status`, `submit_patch`.
- Max tokens set to 16,384, thinking set to 4,096.

## P. Blockers
- None currently.

## Q. Next Milestone
- Build a reproducible evaluation framework to test the baseline agent against the public tasks.
