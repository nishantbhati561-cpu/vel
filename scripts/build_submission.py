import zipfile
import os

def build_submission():
    print("Building advanced submission...")
    with zipfile.ZipFile("submission.zip", "w") as zf:
        # Package the root agent
        if os.path.exists("agents/advanced_agent/agent.yaml"):
            zf.write("agents/advanced_agent/agent.yaml", "agent.yaml")
        else:
            print("ERROR: advanced agent not found")
            return

        # Package eval config
        if os.path.exists("eval_config.yaml"):
            zf.write("eval_config.yaml")

        # Recursively package the prompts directory
        if os.path.exists("prompts"):
            for root, _, files in os.walk("prompts"):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Write retaining the 'prompts/...' folder structure
                    zf.write(file_path, file_path)

    print("Submission built at submission.zip")

if __name__ == "__main__":
    build_submission()
