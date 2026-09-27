import argparse
import json
import os
import time
from pathlib import Path

class ModelBackend:
    """Abstract interface for LLM inference."""
    def generate(self, prompt: str, system_instruction: str, tools: list) -> str:
        raise NotImplementedError

class MockModelBackend(ModelBackend):
    """A mock backend for testing orchestration without a real GPU."""
    def generate(self, prompt: str, system_instruction: str, tools: list) -> str:
        # Simulate thinking and returning a patch
        return '{"action": "submit_patch", "args": {}}'

def run_agent_loop(agent_config_path: Path, task: dict, backend: ModelBackend) -> dict:
    """Simulates the ADK loop using the given agent config and task."""
    start_time = time.time()

    # Load agent config
    # In a real environment, this parses YAML and configures ADK.
    # We will simulate a successful mock loop.

    tool_calls = 3 # Simulated tool usages
    files_read = 2
    files_mod = 1
    tests_run = 1

    # Simulate LLM call
    backend.generate(task.get("problem_statement", ""), "", [])

    elapsed = time.time() - start_time

    return {
        "task_id": task.get("instance_id", "unknown"),
        "repo": task.get("repo", "unknown"),
        "result": "PASS", # Mock success
        "time_seconds": elapsed,
        "tool_calls": tool_calls,
        "files_read": files_read,
        "files_modified": files_mod,
        "tests_run": tests_run,
        "failure_category": "NONE"
    }

def main():
    parser = argparse.ArgumentParser(description="Run local evaluation framework.")
    parser.add_argument("--agent", required=True, help="Agent configuration name (e.g. 'baseline')")
    parser.add_argument("--tasks", default="competition_data/tasks.jsonl", help="Tasks file")
    parser.add_argument("--output", default="results", help="Output directory")
    args = parser.parse_args()

    agent_path = Path(f"agents/{args.agent}/agent.yaml")
    if not agent_path.exists():
        print(f"Error: Agent config {agent_path} not found.")
        return

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    backend = MockModelBackend()

    # Load first 5 tasks as a sample
    tasks = []
    with open(args.tasks, "r") as f:
        for i, line in enumerate(f):
            if i >= 5:
                break
            tasks.append(json.loads(line))

    results = []
    for task in tasks:
        print(f"Running task {task['instance_id']}...")
        res = run_agent_loop(agent_path, task, backend)
        results.append(res)

    # Write summary json
    summary_path = out_dir / f"{args.agent}_summary.json"
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2)

    # Write CSV
    csv_path = out_dir / f"{args.agent}_tasks.csv"
    import csv
    with open(csv_path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print(f"Evaluation complete. Results saved to {args.output}/")

if __name__ == "__main__":
    main()
