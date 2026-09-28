# Task Taxonomy

Based on the 129 tasks observed in `tasks.jsonl` from the official dataset:

## Identified Repositories
1. **fastapi (67 tasks)**: Web framework issues, often involving routing, Pydantic validation, serialization, and typing.
2. **rich (48 tasks)**: Terminal rendering issues, usually concerning formatting, layout geometry, ANSI escape sequences, and console output.
3. **requests (13 tasks)**: HTTP library issues, likely covering session management, headers, connection pooling, and SSL/TLS.
4. **httpx (1 task)**: Async HTTP library, similar footprint to requests.

## Expected Failure Patterns (Hypothesis)
- **Localization Failures**: Agents failing to find the correct deep nested module in `fastapi/routing.py` or `rich/console.py` due to generic problem statements.
- **Over-Editing**: Modifying core classes where only a localized edge-case patch is required, causing widespread test regressions.
- **Budget Exhaustion**: Infinite looping in `edit_file` when the `old_string` mismatch prevents the patch from applying.
- **Graph Misuse**: Dumping large subgraphs into the context window, blowing the 32k token limit.
