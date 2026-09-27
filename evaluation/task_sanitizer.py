import json

def sanitize_task(raw_task: dict) -> dict:
    """
    Strips gold/reference fields from the raw tasks.jsonl entry to prevent data leakage.
    Allows only context needed for repair: instance_id, repo, problem_statement, hints_text, etc.
    """
    FORBIDDEN_FIELDS = {"patch", "test_patch", "base_commit", "created_at"}
    sanitized = {}

    for key, value in raw_task.items():
        if key in FORBIDDEN_FIELDS:
            # We explicitly drop these
            continue
        sanitized[key] = value

    return sanitized
