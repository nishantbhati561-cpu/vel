# Evaluation Framework

## Reproducible Testing
- Split tasks into Development / Holdout sets.
- Do not overfit on public leaderboards.
- Store results iteratively in `results/`.
- Validate submissions using local CLI (`swegemma eval`) before Kaggle submission.

## Experiment Tracking
All experiments must log:
- ID, Date, Commit
- Configuration and Strategy
- Task Pass/Fail Rate
- Execution Time
