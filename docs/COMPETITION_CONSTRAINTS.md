# Verified Competition Constraints

Based strictly on `HARNESS_README.md`:

1. **Submission Format**: A ZIP archive with `agent.yaml` at the root. The total unpacked size must be < 3 GiB.
2. **Model**: All agents in a submission must declare at most ONE unique base model, which must be `gemma-4-31b-it-qat-w4a16-ct`.
3. **Hardware Environment**: 4x NVIDIA L4 GPUs (24GB VRAM each).
4. **Context Window**: 32,768 tokens maximum combined prompt, reasoning, and output context length.
5. **Sandboxing**: Container A (Agent Sandbox) and Container B (Verification Sandbox) provide 4 GiB RAM / 2 vCPUs.
6. **Built-in Tools**: 9 official tools available via `swegemma.tools`:
   - Execution: `run_command`
   - Workspace: `read_file`, `edit_file`, `write_file`, `get_status`, `submit_patch`
   - Graph: `get_code_neighbors`, `search_similar_code`, `get_code_subgraph`
7. **Time Budget**: The total task-run budget across the evaluation is 12 hours.
