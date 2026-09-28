# Competition Data Inventory

## Downloaded Files
- `HARNESS_README.md`: Primary reference documentation for constraints and tools.
- `tasks.jsonl`: The official task dataset containing 129 SWE tasks.
- `docker/`: Contains the official Dockerfile configurations (`Dockerfile.public`, `Dockerfile.sandbox`) and helper scripts (`imp.py`, `telnetlib.py`).

## Task Dataset Breakdown (tasks.jsonl)
- **Total Tasks**: 129
- **Repositories**:
  - `fastapi/fastapi`: 67 tasks
  - `Textualize/rich`: 48 tasks
  - `psf/requests`: 13 tasks
  - `encode/httpx`: 1 tasks
- **Schema**: Each task provides:
  - `instance_id`
  - `repo`
  - `base_commit`
  - `patch` (The gold standard solution)
  - `test_patch` (The regression/verification test)
  - `problem_statement` (The issue description)

## Large Resources (Not Downloaded Yet)
- **Embeddings**: `.npz` files for semantic search (`search_similar_code`).
- **Graphs**: `.json` files for AST graph analysis (`get_code_neighbors`, `get_code_subgraph`).
- **Repos**: Base repository tarballs/snapshots.
