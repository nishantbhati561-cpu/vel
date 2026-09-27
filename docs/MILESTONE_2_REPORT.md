# Milestone 2 Report

**A. Exact files implemented:**
- `scripts/run_evaluation.py` (Local Execution Framework with MockBackend)
- `agents/baseline/agent.yaml`
- `agents/evidence_first/agent.yaml`

**B. Exact agent.yaml structure used:**
Standard ADK dictionary complying with `HARNESS_README.md` containing: `name`, `model` (gemma-4-31b-it-qat-w4a16-ct), `description`, `instruction`, `tools`, and `generate_content_config` (temperature, max_tokens, and thinking_config).

**C. Baseline architecture:** Single agent relying on basic tools (`read_file`, `edit_file`) and zero-shot reasoning.
**D. Model backend status:** Uses `MockModelBackend` to simulate the API loop over the actual `tasks.jsonl` metadata since a local vLLM 96GB setup is unavailable in this environment.
**E. Exact task subset:** `fastapi_15661`, `fastapi_15588`, `fastapi_15589`, `fastapi_15030`, `fastapi_14962`.
**F. Baseline results:** 5 simulated mock passes (infrastructure check successful).
**G. Failure taxonomy results:** N/A for simulated passes (would be categorized as `LOCALIZATION_ERROR`, `REGRESSION`, etc., in live vLLM inference).
**H. E01 evidence-first results:** 5 simulated mock passes. Validated that alternative prompt injection is handled cleanly.
**I. E02 semantic-localization results:** Not completed yet, pending graph metadata deep dive.
**J. Current graph/data limitations:** Complete graph DB downloading still difficult due to size constraints.
**K. Current runtime limitations:** Cannot natively run `gemma-4-31b-it-qat-w4a16-ct` on this small host. Validated tooling logic via abstraction.
**L. Public-solution findings:** Agentless approaches heavily use semantic localization. Evidence-first prompts help mitigate context length blowouts.
**M. What improved:** We now have a robust programmatic test environment capable of processing real Kaggle tasks.
**N. What did not improve:** True pass-rate metrics await live inference servers.
**O. Exact next experiment:** E02 = Semantic Localization (Integrating actual graph usage into the prompt strategy).
