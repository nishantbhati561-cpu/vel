# Milestone 2B Report: Baseline Audit & Data Leakage Prevention

**A. Existing implementation audited:** Both `agents/baseline/agent.yaml` and `agents/evidence_first/agent.yaml` were confirmed to match harness schema expectations.
**B. Actual tasks.jsonl schema:** Explored directly via python script. The schema contains: `instance_id`, `repo`, `base_commit`, `patch`, `test_patch`, `problem_statement`, `hints_text`, and `created_at`.
**C. Data-leakage audit:** We successfully identified that `patch` and `test_patch` are GOLD references. They must never be injected into agent contexts.
**D. Sanitization implementation:** `evaluation/task_sanitizer.py` has been written and unit-tested to forcefully strip `patch`, `test_patch`, `base_commit`, and `created_at` from the runtime dictionary before the agent loop is invoked.
**E. Mock-vs-real evaluation distinction:** The orchestrator now injects an explicit `"is_mock": True` flag into all run results. Documented in `docs/EVALUATION_STATUS.md`.
**F. Verified harness schema:** Harness limits (`3GiB`, `32768` tokens, single model) are confirmed based on grep checks against `HARNESS_README.md`.
**G. Verified model/runtime configuration:** Configuration explicitly uses `gemma-4-31b-it-qat-w4a16-ct`.
**H. Baseline agent behavior:** Simple single-agent evidence-first flow.
**I. Evidence-first behavior:** Prompts have been verified to prioritize evidence retrieval before patch modification.
**J. Submission packaging path:** Implemented `scripts/build_submission.py` to correctly map an agent directory to a flat `agent.yaml` zip structure.
**K. Validation results:** Implemented `scripts/validate_submission.py` which validates maximum size, root agent config presence, file extensions, and path traversal vulnerabilities.
**L. Unit/integration test results:** Unit tests added for `test_task_sanitizer.py` explicitly passing.
**M. Genuine benchmark capability:** A genuine benchmark logic pipeline exists, but relies on MockBackend until vLLM is connected.
**N. Remaining blockers:** Actual inference environment for Kaggle dataset metrics.
**O. Exact next experiment:** E02 Semantic Localization.
