"""Deploy the example application to a local output directory."""

import argparse
import shutil
from pathlib import Path


def deploy(destination):
    target = Path(destination).resolve()
    target.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "app.py"
    shutil.copy2(source, target / "app.py")
    print(f"Deployed app.py to {target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Deploy the Python app locally"
    )
    parser.add_argument("--destination", default="deployment")
    args = parser.parse_args()
    deploy(args.destination)
