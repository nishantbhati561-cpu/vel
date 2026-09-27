# Verified Competition Constraints

## Model Constraints
- **Required Model:** All agents MUST use `gemma-4-31b-it-qat-w4a16-ct` (W4A16 INT4 Quantized).
- **Context Window:** Max token limit is 32,768 (vLLM max_model_len). Total max_output_tokens + thinking_budget must respect this.

## Packaging Restrictions
- **Root:** `agent.yaml` must be at the root of the ZIP file.
- **Maximum Archive Size:** < 3 GiB (3,221,225,472 bytes) total unpacked size, including all `adapters/`.
- **File Extensions:** Only `.yaml`, `.yml`, `.md`, `.txt`, `.py`, `.json`, and `.safetensors` are allowed.
- **File Counts:** Max 10,000 files, Max 1,000 YAMLs, Max 1,000 skills. Max 500 agents. Max 50 sub_agent depth. Max YAML size 50 MiB.
- **Security:** No absolute paths, null bytes, `..` traversal, or symlinks escaping submission root.
- **LoRA:** Up to 8 LoRAs allowed. Max rank 128. `adapters/<name>/adapter_model.safetensors` format.

## Runtime & Tooling Constraints
- **Budget:** Total 12-hour task-run budget including sandbox setup.
- **Tools:** Use standard tools (`edit_file`, `write_file`, `run_command`, `submit_patch`, etc.). Tool output truncates if token limits are hit.
- **Patch Submission:**
  - Explicit `submit_patch` is free.
  - Temporary files in `/workspace` will be included in the patch. Use `/tmp` for scratch scripts.
  - Harness modifies test files (`pytest.ini`, `conftest.py`, `test_*.py`); agent must NOT alter them as harness resets them before validation.
- **Generation:** `temperature`, `top_p`, `top_k`, penalties, `thinking_config` are all configurable.
