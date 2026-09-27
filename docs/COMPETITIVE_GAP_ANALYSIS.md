# Competitive Gap Analysis

## Public Solutions Context
The Kaggle Gemma 4 Developer Agent competition has seen a variety of public baselines. These generally fall into two camps:
1. **Agentless / Heuristic Dense Retrievers:** Use the provided `embeddings/` directly to filter codebase context, then pipe a massively dense prompt into a 32K context window to generate a patch.
2. **Vanilla React Loops:** Standard zero-shot LLM loops wrapping `edit_file` and `read_file`, heavily susceptible to hallucination or getting stuck.

## Our Approach vs Public Approaches

### 1. Hybrid Localization vs Pure Semantic
- **Public:** Often rely entirely on `search_similar_code` (semantic) retrieving the top-K files. If the error spans a long inheritance chain, pure semantic search misses the base classes.
- **Our Gap / Advantage:** The `semantic_localization` (E02) and `graph_guided` (E03) agents combine semantic retrieval as the *entry point*, but explicitly use `get_code_neighbors` (graph) to walk the caller/callee trees. This covers the semantic blindspots (e.g. abstract interfaces not containing the error text).

### 2. Evidence-First Patching
- **Public:** Jump straight to `edit_file` upon guessing the error, repeatedly failing syntax errors.
- **Our Gap / Advantage:** Our explicit `evidence_first` instruction (E01) mandates reading tests and gathering structured hypothesis evidence *before* patching. We evaluate patching success locally via tests before finalizing `submit_patch`.

### 3. Cost / Token Exhaustion
- **Public:** Dump entire 30K graph subgraphs into context.
- **Our Gap / Advantage:** Our tools and instructions heavily prioritize minimal, targeted file reads and limiting context saturation.

## Conclusion
The explicit staging of E00 (baseline) -> E01 (evidence) -> E02 (semantic) -> E03 (graph) allows us to measure precisely *which* heuristic outperforms the public agentless baselines without just guessing.
