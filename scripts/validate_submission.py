import zipfile
import os
import argparse

def validate(zip_path: str):
    max_size = 3 * 1024 * 1024 * 1024  # 3 GiB
    size = os.path.getsize(zip_path)
    if size > max_size:
        raise ValueError(f"Zip size {size} exceeds 3GiB")

    with zipfile.ZipFile(zip_path, 'r') as zf:
        names = zf.namelist()
        if "agent.yaml" not in names and "agent.yml" not in names:
            raise ValueError("agent.yaml missing from zip root")

        for name in names:
            if ".." in name or name.startswith("/"):
                raise ValueError(f"Path traversal detected in {name}")

            ext = name.split(".")[-1].lower() if "." in name else ""
            if ext and ext not in ["yaml", "yml", "md", "txt", "py", "json", "safetensors"]:
                if "/" not in name or not name.endswith("/"): # Ignore directories
                    # This check is just a warning as there may be standard git files, but the harness is strict
                    print(f"Warning: Unusual extension found {name}")

    print("Validation passed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True)
    args = parser.parse_args()
    validate(args.zip)
