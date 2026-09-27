import zipfile
import os
from pathlib import Path
import argparse

def build_submission(agent_name: str, output_path: str):
    agent_dir = Path("agents") / agent_name
    if not agent_dir.exists():
        raise FileNotFoundError(f"Agent directory {agent_dir} not found")

    yaml_path = agent_dir / "agent.yaml"
    if not yaml_path.exists():
        raise FileNotFoundError(f"agent.yaml missing from {agent_dir}")

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Crucial constraint: agent.yaml must be at the root of the zip
        for root, dirs, files in os.walk(agent_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(agent_dir)
                zf.write(file_path, arcname)
    print(f"Submission packed successfully to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", required=True)
    parser.add_argument("--out", default="submission.zip")
    args = parser.parse_args()
    build_submission(args.agent, args.out)
