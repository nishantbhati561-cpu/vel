import pytest
from evaluation.task_sanitizer import sanitize_task

def test_task_sanitizer_removes_gold_fields():
    raw = {
        "instance_id": "fastapi_1",
        "repo": "fastapi/fastapi",
        "patch": "--- a/file\n+++ b/file",
        "test_patch": "--- a/test\n+++ b/test",
        "problem_statement": "Fix the bug",
        "hints_text": "Look at line 5",
        "base_commit": "abcdef12345",
        "created_at": "2026-05-31"
    }

    sanitized = sanitize_task(raw)

    assert "patch" not in sanitized
    assert "test_patch" not in sanitized
    assert "base_commit" not in sanitized
    assert "created_at" not in sanitized
    assert "instance_id" in sanitized
    assert sanitized["problem_statement"] == "Fix the bug"
