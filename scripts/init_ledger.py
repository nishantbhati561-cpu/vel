import csv
from pathlib import Path

def init_ledger():
    ledger_path = Path("results/official_submissions.csv")
    if not ledger_path.exists():
        with open(ledger_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                "submission_id",
                "timestamp",
                "agent_version",
                "commit",
                "architecture",
                "prompt_version",
                "adapter_version",
                "notes",
                "public_score",
                "status"
            ])
        print("Ledger initialized.")
    else:
        print("Ledger already exists.")

if __name__ == "__main__":
    init_ledger()
