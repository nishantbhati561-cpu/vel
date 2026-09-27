# Submission Checklist

- [ ] `agent.yaml` is at the root of the archive.
- [ ] Base model is exclusively `gemma-4-31b-it-qat-w4a16-ct`.
- [ ] Total archive size is strictly under 3 GiB.
- [ ] No credential leaks.
- [ ] No path traversal (all files resolve inside the root).
- [ ] No raw datasets or experiment logs included.
- [ ] Temporary files during execution use `/tmp` or are cleaned up.
- [ ] Uses valid `!include` structures (max depth 10).
