# AGENTS.md

## Purpose
This repository serves as the research and development environment for the Gemma 4 Developer Agent competition. The goal is to build, benchmark, improve, harden, and package the strongest compliant autonomous software-engineering agent.

## Architecture
The system emphasizes a rigorous, evidence-first workflow:
1. **Localization**: Hybrid code localization combining lexical search, semantic embeddings, graph traversal, and targeted reads.
2. **Reasoning**: Test-aware root cause analysis.
3. **Patching**: Minimal patch generation prioritizing focused edits.
4. **Verification**: Automated regression testing and patch hygiene within an adaptive time/tool budget.

The competition base model is strictly `gemma-4-31b-it-qat-w4a16-ct`.

## Source Layout
- `agents/`: Agent YAML definitions (e.g., `baseline/`, `evidence_first/`).
- `competition_data/`: Downloaded competition materials (e.g., `HARNESS_README.md`, `tasks.jsonl`, `embeddings/`, `graphs/`). **DO NOT package large raw datasets in the final submission.**
- `docs/`: Competition summaries, taxonomies, state documents, and architecture design.
- `evaluation/` & `scripts/`: Tools for running reproducible evaluation pipelines.

## Competition Constraints
- **Model Rule**: Only the official quantized `gemma-4-31b-it-qat-w4a16-ct` model may be used.
- **Context Limit**: Maximum context length is 32,768 tokens.
- **Environment**: 4x NVIDIA L4 GPUs.
- **Budget**: 12 hours global evaluation time.
- **Tools**: Only the 9 built-in `swegemma` tools (e.g., `read_file`, `edit_file`, `run_command`, `get_code_neighbors`, `search_similar_code`) or compliant subagents/skills are allowed.
- **Path Traversal**: Traversal outside `/workspace` or the submission root is strictly prohibited.

## Workflow Rules
- **No Secrets**: NEVER log, print, or commit `KAGGLE_API_TOKEN` or any credentials.
- **Preserve Experiments**: Append results, never overwrite.
- **Safe Testing**: Fail clearly on errors and diagnose them before guessing fixes.

## Final Submission
- Must be a `.zip` archive.
- `agent.yaml` must reside at the root of the archive.
- The overall size must be under 3 GiB.
