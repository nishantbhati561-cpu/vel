# Gemma 4 Developer Agent - Research Repository

## Purpose
This repository is the dedicated research and development environment for building the strongest competition-compliant autonomous software-engineering agent for the Google DeepMind Gemma 4 Developer Agent Competition on Kaggle.

## Architecture
The agent system revolves around an evidence-first reasoning approach with targeted hybrid code localization. We prioritize test-aware repair, minimal patching, robust failure containment, and an adaptive time budget. Advanced components (multi-agent, LoRA) are introduced strictly based on experimental evidence.

## Source Layout
- `agents/`: Agent YAML configurations, sub-agent definitions, and ADK tool/skill code.
- `adapters/`: Safe tensors for optional LoRA adapters.
- `competition_data/`: Ignored directory containing raw competition tasks, graphs, and harnesses.
- `docs/`: Constraints, taxonomy, literature review, and architecture notes.

## Research Layout
- `experiments/`: Tracked versions of specific agent hypotheses.
- `evaluation/`: Scripts to run reproducible development splits.
- `results/`: Historical evaluation outcomes.
- `traces/`: Structured execution logs for debugging and offline learning.
- `prompts/`: Versioned instructions.

## Competition Constraints
- **Model:** All agents must use `gemma-4-31b-it-qat-w4a16-ct`.
- **Packaging:** ZIP file `< 3 GiB`, `agent.yaml` at root.
- **Tools:** Use harness tools (no path traversal).
- **Constraints:** Respect a 12-hour total task-run budget.

## Secrets
**Never commit or write `KAGGLE_API_TOKEN` or other credentials into any repository file.**
Use safe environment variable checks if accessing Kaggle APIs.

## Testing & Validation
Use the official `swegemma eval` CLI against the development splits.
Before building the final ZIP, we run our strict validator to ensure all competition packaging rules are met.
