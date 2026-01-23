import os
import subprocess
import sys

def run(cmd: str):
    print(f">>> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

host = os.environ["DEPLOY_HOST"]
user = os.environ["DEPLOY_USER"]
image = os.environ["CI_REGISTRY_IMAGE"]

cmd = f"""
ssh {user}@{host} "
  docker pull {image}:latest &&
  docker stop backend || true &&
  docker rm backend || true &&
  docker run -d \
    --name backend \
    --restart always \
    -p 8000:8000 \
    {image}:latest
"
"""

run(cmd)

print(" Deployment successful")
