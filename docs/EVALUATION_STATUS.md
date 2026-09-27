# Evaluation Status Tracking

All metrics currently stored in `results/` are from our orchestration mock. They evaluate the framework piping and not the real model reasoning.

## Categories

- **INFRASTRUCTURE VERIFIED:** Local evaluator orchestrates properly, parses YAML correctly, processes tools correctly. (Currently active via MockBackend).
- **MOCK VERIFIED:** The mocked backend executes full end-to-end loops successfully on the sanitizer boundary.
- **REAL MODEL VERIFIED:** Not yet achieved (pending actual deployment of vLLM or 4x L4 hardware).
- **OFFICIAL HARNESS VERIFIED:** Not yet achieved (pending Kaggle submission).

*Do NOT report mock scores as true competition baseline metrics.*
