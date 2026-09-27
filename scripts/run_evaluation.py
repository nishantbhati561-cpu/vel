import argparse
import json
import os
import time
from pathlib import Path
from evaluation.task_sanitizer import sanitize_task

class ModelBackend:
    """Abstract interface for LLM inference."""
    def generate(self, prompt: str, system_instruction: str, tools: list) -> str:
        raise NotImplementedError

class MockModelBackend(ModelBackend):
    """A mock backend for testing orchestration without a real GPU."""
    def __init__(self, simulate_recovery=False):
        self.simulate_recovery = simulate_recovery

    def generate(self, prompt: str, system_instruction: str, tools: list) -> str:
        return '{"action": "submit_patch", "args": {}}'

def run_agent_loop(agent_config_path: Path, raw_task: dict, backend: ModelBackend) -> dict:
    """Simulates the ADK loop using the given agent config and task."""
    start_time = time.time()

    # 1. Enforce Sanitization Boundary
    task = sanitize_task(raw_task)
    assert "patch" not in task, "Data leakage detected: Gold patch exposed to agent loop!"

    # Simulate infrastructure interactions
    agent_name = str(agent_config_path).split("/")[-2]

    if "integrated_core" in agent_name:
        # Simulate a richer loop with recovery and more tool calls
        tool_calls = 12
        files_read = 4
        files_mod = 2
        tests_run = 2
        repair_iterations = 1 # Failed once, fixed on retry
        budget_status = "HEALTHY"
    else:
        tool_calls = 3
        files_read = 2
        files_mod = 1
        tests_run = 1
        repair_iterations = 0
        budget_status = "HEALTHY"

    backend.generate(task.get("problem_statement", ""), "", [])
    elapsed = time.time() - start_time

    return {
        "task_id": task.get("instance_id", "unknown"),
        "repo": task.get("repo", "unknown"),
        "result": "PASS",
        "time_seconds": elapsed,
        "tool_calls": tool_calls,
        "files_read": files_read,
        "files_modified": files_mod,
        "tests_run": tests_run,
        "repair_iterations": repair_iterations,
        "budget_status": budget_status,
        "failure_category": "NONE",
        "is_mock": True
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", required=True)
    parser.add_argument("--tasks", default="competition_data/tasks.jsonl")
    parser.add_argument("--output", default="results/mock")
    parser.add_argument("--experiment", required=True, help="Experiment identifier (e.g. e00_baseline)")
    args = parser.parse_args()

    agent_path = Path(f"agents/{args.agent}/agent.yaml")
    out_dir = Path(args.output) / args.experiment
    out_dir.mkdir(parents=True, exist_ok=True)

    backend = MockModelBackend()

    tasks = []
    with open(args.tasks, "r") as f:
        for i, line in enumerate(f):
            if i >= 5: break
            tasks.append(json.loads(line))

    results = []
    for task in tasks:
        res = run_agent_loop(agent_path, task, backend)
        results.append(res)

    with open(out_dir / f"{args.agent}_summary.json", "w") as f:
        json.dump(results, f, indent=2)

    # Write CSV
    import csv
    csv_path = out_dir / f"{args.agent}_tasks.csv"
    with open(csv_path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        for r in results:
            writer.writerow(r)

if __name__ == "__main__":
    main()
