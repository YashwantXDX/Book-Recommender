from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Book Recommender"
AUTHER_USER_NAME = "Yashwant"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHER_USER_NAME,
    description="Package for Book Recommender",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    author_email="yashwantxdx@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.12.5",
    install_requires=LIST_OF_REQUIREMENTS
)