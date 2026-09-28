# Evaluation Plan

## Matrix
- **E00 Baseline**: Minimal robust baseline without advanced logic.
- **E01 Evidence-First**: Introduces rigorous hypothesis testing.
- **E02 Semantic Localization**: Leverages `search_similar_code`.
- **E03 Hybrid Localization**: Semantic + Lexical search.
- **E04 Graph Neighbors**: Uses `get_code_neighbors`.
- **E05 Test-Aware Repair**: Analyzes `pytest` outputs.

## Schema
Results must be stored reliably per task with:
- Task Result (PASS/FAIL)
- Elapsed Time
- Tool Count
- Failure Category
- Patch Size
