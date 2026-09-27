# Official Kaggle Execution Path

Based strictly on `HARNESS_README.md`, the actual execution of an agent works as follows:

## Stage 1: ADK Compilation & Inference
1. **Receive Submission**: Kaggle extracts `submission.zip` into `/kaggle/working/submission`. Total unpacked size must be < 3 GiB.
2. **Compile Agent**: `adk-submission` compiles `agent.yaml` directly from the zip root. It strictly enforces the single-model rule (`gemma-4-31b-it-qat-w4a16-ct`) and discovers any LoRA directories mapped in `adapters/`.
3. **Workspace Setup**: `swegemma` spawns Container A (Sandboxed workspace) matching the task repository at its `base_commit`.
4. **Agent Invocation**: The agent receives `{problem_description}` and `{hints}` interpolated into its instructions.
5. **Tool Execution**: The agent calls any of the 9 official tools. These tools are strictly gated by budget checks (`max_tool_calls=100`, `timeout=300s`, total run limits).
6. **Patch Capture**: The agent explicitly calls `submit_patch()`, or, if it exhausts limits without calling it, the harness automatically runs `git add -N . && git diff HEAD` inside Container A as a fallback.

## Stage 2: Phase 2 Verification (Metric Scoring)
7. **Clean Container B**: A fresh Container B is spawned. Target test files and runner configs (`pytest.ini`, etc.) are reset to `HEAD` (eval_baseline) to strictly prevent tampering.
8. **Patch Application**: The captured `agent_patch` is applied using a resilient 4-pass sequence (git apply vs patch).
9. **Test Execution**: The official `task.test_patch` is applied, and hermetic `pytest` is executed.
10. **Resolution**: `score = 1.0` if `pytest` exits `0` AND the JUnit XML explicitly validates the required nodes without skipped/failed tests.
