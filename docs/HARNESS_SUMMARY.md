# Harness Summary

This document summarizes the `swegemma` evaluation harness based on `HARNESS_README.md`.

## System Architecture
- **adk-submission**: Compiles the submission `agent.yaml` declaratively without executing untrusted python code.
- **adk-eval-core**: Manages task models, sandbox execution (Subprocess/Docker), file editing (`apply_replacement` resilient matcher), and cost tracking.
- **swegemma**: Orchestrates the evaluation lifecycle, binds the 9 sandboxed workspace/graph tools, and runs hermetic pytest + JUnit extraction.

## Built-In Tools
1. `run_command(command: str)`: Executes bash commands with a timeout limit.
2. `get_status()`: Retrieves git diffs and active uncommitted files.
3. `submit_patch()`: Finalizes the session, generating the patch for validation.
4. `read_file(filepath, start_line, end_line)`: Reads files with a 150-line / 10,000-character truncation limit.
5. `edit_file(filepath, old_string, new_string)`: Edits using exact, flexible (indentation-aware), or regex-based replacement.
6. `write_file(filepath, content)`: Creates or overwrites a file completely.
7. `get_code_neighbors(node, edge_type, max_neighbors)`: Navigates AST dependencies.
8. `search_similar_code(query, k)`: Performs offline cosine similarity against codebase vectors.
9. `get_code_subgraph(nodes)`: Extracts interconnecting graphs for specified nodes.

## Rules
- Single model: `gemma-4-31b-it-qat-w4a16-ct`.
- Context window: 32,768 max tokens.
- Budget warnings trigger when `tool_calls` is low.
