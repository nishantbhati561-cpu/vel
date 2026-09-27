import json

def sanitize_task(raw_task: dict) -> dict:
    """
    Strips gold/reference fields from the raw tasks.jsonl entry to prevent data leakage.
    Allows only context needed for repair: instance_id, repo, problem_statement, hints_text, etc.
    """
    ALLOWED_FIELDS = {"instance_id", "repo", "problem_statement", "hints_text"}
    sanitized = {}

    for key, value in raw_task.items():
        if key in ALLOWED_FIELDS:
            sanitized[key] = value

    # As an extra safety net, we ensure these definitely don't exist
    assert "patch" not in sanitized
    assert "test_patch" not in sanitized

    return sanitized
