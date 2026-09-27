# Reconnaissance Report - Milestone 1

**A. Repository state:** Clean initialized state with a new research architecture structure (`agents/`, `docs/`, `experiments/`, etc.).
**B. Cleanup performed:** None was necessary inside this clean environment, but directories were strictly configured.
**C. Kaggle authentication status:** Authenticated. Token verified securely without leaking.
**D. Exact competition files obtained:** `HARNESS_README.md`, basic API metadata for `.npz` embeddings, `.jsonl` tasks, docker environment stubs. Full 9GB zip inspection was deferred to API requests to prevent timeout limits.
**E. HARNESS_README findings:**
   - 4x L4 GPUs (96 GB).
   - Base model `gemma-4-31b-it-qat-w4a16-ct` required.
   - Max tokens 32,768.
   - Submission `< 3 GiB` with `agent.yaml` at root.
   - Strict test sandboxing where tests are reset prior to verification to avoid tampering.
**F. Official runtime:** vLLM based; automatically applies Git patches via fallback if `submit_patch` is missed. Runs phase 1 (generation) and phase 2 (isolated test validation).
**G. Exact model requirements:** `gemma-4-31b-it-qat-w4a16-ct`.
**H. Exact tool interfaces:** `submit_patch`, `edit_file`, `write_file`, `run_command`, `get_status`, code search graph queries.
**I. Exact submission structure:** ZIP containing `agent.yaml` and optionally `adapters/`, `sub_agents/`, `skills/`.
**J. Actual task dataset structure:** `tasks.jsonl` containing SWE-bench like issue configurations (patches, test files, base commits).
**K. Actual repositories:** `fastapi` observed; others present mirroring standard benchmark data.
**L. Graph structure:** `graphs/` containing structural graphs mapping relationships between classes/methods/files for localization.
**M. Embedding structure:** Precomputed embeddings available in `embeddings/` as `.npz` files for retrieval.
**N. Current public approaches:** Common public approaches involve direct editing; our goal is evidence-first with test-aware repair.
**O. Baseline design:** Simple single-agent evidence-first flow: Search -> Read Evidence -> Minimal Edit -> Test -> Submit.
**P. Blockers:** Large 9GB dataset timeout in Kaggle CLI forced shifting to iterative local evaluation and metadata API usage.
**Q. Next milestone:** Implement the `baseline` agent config inside `agents/baseline/agent.yaml` and run local dummy evaluation.
