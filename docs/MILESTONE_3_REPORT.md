# Milestone 3 Report: End-to-End Baseline & Harness Validation

**A. Tests executed and results:** Unit tests run (`test_task_sanitizer.py`). 1 passed, 0 failed. Submission validation tests also successfully passed against `baseline_test.zip` asserting 3GiB size limits, root `agent.yaml`, and path safety.
**B. Task schema findings:** The `tasks.jsonl` schema explicitly exposes `patch` and `test_patch` arrays alongside meta-information like `base_commit`. These are officially forbidden from agent execution contexts to prevent dataset memorization.
**C. Leakage-sanitizer findings:** Explicit assertions were added ensuring ONLY `instance_id`, `repo`, `problem_statement`, and `hints_text` make it into the runtime context object.
**D. Official harness validation:** Validated that our YAML syntax properly complies with ADK requirements regarding model specification, limits, tool bindings, and agent instruction syntax via the manual checks implemented in `validate_submission.py`.
**E. Submission ZIP validation:** Verified that a flat zip archive of `agents/baseline/*` packages properly and passes basic schema compliance.
**F. Actual model availability:** Verified missing. Execution `pip list` confirmed vLLM is missing, and `nvidia-smi` confirmed zero L4 GPUs. Therefore, real Gemma 4 execution is blocked in this environment.
**G. Actual task execution availability:** Since the LLM is blocked, execution defaults to the `MockModelBackend` simulating a successful repair.
**H. Exact task IDs used:** `fastapi_15661`, `fastapi_15588`, `fastapi_15589`, `fastapi_15030`, `fastapi_14962`.
**I. E00 results:** 5 passes (MOCK ONLY). Logged to `results/mock/e00_baseline/`.
**J. E01 results:** 5 passes (MOCK ONLY). Logged to `results/mock/e01_evidence_first/`.
**K. Failure taxonomy:** (N/A for mock passes).
**L. Infrastructure limitations:** Hard limits on downloading the 9GB task graph datasets directly prevent immediate graph semantic analysis in code; execution bound by MOCK infrastructure.
**M. Remaining risks:** Prompt tuning relies entirely on zero-shot inference without real-world feedback loops from vLLM evaluation scoring.
**N. Exact next experiment:** E02 = Semantic Localization (Integrating existing dense retrievers properly for codebase mapping).
