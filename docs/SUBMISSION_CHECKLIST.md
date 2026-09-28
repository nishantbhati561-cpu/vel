# Final Submission Checklist

- [ ] `agent.yaml` is at the ZIP root.
- [ ] YAML is valid and `!include` paths are correct.
- [ ] Base model is exactly `gemma-4-31b-it-qat-w4a16-ct`.
- [ ] No unapproved tools requested.
- [ ] No path traversal outside `/workspace`.
- [ ] Total uncompressed size < 3 GiB.
- [ ] No credentials included.
- [ ] No raw datasets included in the zip.
- [ ] Validated with `evaluation/validate_submission.py`.
