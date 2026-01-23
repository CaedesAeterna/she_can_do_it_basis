import os
import subprocess
import sys

def run(cmd: str):
    print(f">>> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

image = os.environ["CI_REGISTRY_IMAGE"]
commit = os.environ["CI_COMMIT_SHORT_SHA"]

tag = f"{image}:{commit}"

run(f"docker run --rm {tag} pytest")

print("Tests passed")
