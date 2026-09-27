# Competition Data Inventory

## Overview
The exact dataset structure was partially explored using the Kaggle API. Due to pagination limits in the CLI, a full programmatic list is unavailable, but the known structure consists of:

- `HARNESS_README.md`: Contains all details on the environment and evaluation loop.
- `docker/`: Contains images and stubs (e.g., `Dockerfile.public`, `Dockerfile.sandbox`, `imp.py`).
- `embeddings/`: `.npz` files of precomputed embeddings for code retrieval (e.g., `fastapi_*`).
- `graphs/`: Structural code graphs.
- `snapshots/`: Baseline commits for tests.
- `tasks.jsonl`: The evaluation dataset.

## Repositories Identified
- `fastapi` (observed in the first page of embeddings)
- Other repositories follow the standard SWE-bench-like format, customized for this competition.

## Data Sizes
- Total archive size is roughly 9GB.
- Embeddings are approx 4-6 MB per `.npz` file.
