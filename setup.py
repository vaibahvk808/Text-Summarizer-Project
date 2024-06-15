import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


__version__="0.0.0"

REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="vaibhavk808"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="vaibhavk808@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email="vaibhavk808@gmail.",
    description="A small python package for NLP s app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)


