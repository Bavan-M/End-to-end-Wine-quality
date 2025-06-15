from setuptools import setup, find_packages
from pathlib import Path


with open ("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="End-to-end-Wine-quality"
AUTHOR_USER_NAME="Bavan-M"
SRC_REPO="mlProject"
AUTHOR_EMAIL="bavanreddy1999@gmail.com"

README = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),

)