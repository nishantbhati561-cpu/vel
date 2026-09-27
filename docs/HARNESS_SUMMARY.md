# Harness Analysis Summary

- Harness is `swegemma`.
- Extracts `agent.yaml` directly.
- Handles generation/context caching heavily for vLLM performance.
- Evaluates on 4x L4 GPUs (96GB total). Base model is 4-bit quantized taking ~16-18 GB.
- **Patch Flow:**
  - `submit_patch()` does `git add -N . && git diff HEAD`.
  - Automatic fallback patches working tree if agent hits limits without explicitly submitting.
  - Phase 2 validation runs in a fresh container. Uses multiple apply strategies (`git apply`, GNU `patch`).
  - Strict anti-tampering: tests and configurations are force-reset to baseline before evaluation.
- Local evaluations can use `swegemma eval`.
