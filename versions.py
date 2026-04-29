import sys
from importlib import metadata


def get_version(distribution_name):
    try:
        return metadata.version(distribution_name)
    except metadata.PackageNotFoundError:
        return "Not Installed"

packages = [
    "streamlit",
    "tensorflow",
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "librosa",
    "soundfile",
    "huggingface-hub",
]

print("\n📦 Installed Package Versions\n")
for pkg in packages:
    print(f"{pkg}: {get_version(pkg)}")

print("\nPython Version:", sys.version)
