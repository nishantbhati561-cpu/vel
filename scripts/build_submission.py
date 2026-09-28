import zipfile
import os

def build_submission():
    print("Building submission...")
    with zipfile.ZipFile("submission.zip", "w") as zf:
        if os.path.exists("agents/baseline/agent.yaml"):
            zf.write("agents/baseline/agent.yaml", "agent.yaml")
        else:
            print("ERROR: baseline agent not found")
            return

    print("Submission built at submission.zip")

if __name__ == "__main__":
    build_submission()
