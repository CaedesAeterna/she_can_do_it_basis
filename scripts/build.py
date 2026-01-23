import os
import subprocess
import sys

def run(cmd: str):
    print(f">>> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

registry = os.environ["CI_REGISTRY"]
user = os.environ["CI_REGISTRY_USER"]
password = os.environ["CI_REGISTRY_PASSWORD"]
image = os.environ["CI_REGISTRY_IMAGE"]
commit = os.environ["CI_COMMIT_SHORT_SHA"]

tag_commit = f"{image}:{commit}"
tag_latest = f"{image}:latest"

run(f"docker login -u {user} -p {password} {registry}")
run(f"docker build -t {tag_commit} -t {tag_latest} .")
run(f"docker push {tag_commit}")
run(f"docker push {tag_latest}")

print("Build & push completed")
