import zipfile
import os

def build_submission():
    print("Building flat monolithic agent submission (E12)...")
    with zipfile.ZipFile("submission.zip", "w") as zf:
        # Package the root agent (E12 Flat Architecture)
        if os.path.exists("agent.yaml"):
            zf.write("agent.yaml")
        else:
            print("ERROR: agent.yaml not found at root")
            return

        # Package evaluation config
        if os.path.exists("eval_config.yaml"):
            zf.write("eval_config.yaml")

        # Package generation/sampling configs
        if os.path.exists("configs"):
            for root, _, files in os.walk("configs"):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path, file_path)

        # Recursively package the prompts directory
        if os.path.exists("prompts"):
            for root, _, files in os.walk("prompts"):
                for file in files:
                    file_path = os.path.join(root, file)
                    zf.write(file_path, file_path)

    print("Submission built at submission.zip")

if __name__ == "__main__":
    build_submission()
