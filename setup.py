from setuptools import setup, find_packages
from typing import List

def load_requirements(filename:str) -> List:
    requirements = []

    with open(filename) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements = [req.replace('-e .', '') for req in requirements]

    return requirements


setup(
    name = "Fraud Detection in Credit Cards",
    version = "0.0.1",
    author = "Debmalya (Deb)",
    author_email = "debmalya.mondal@outlook.com",
    description = "A ML implementation to detect fradulent credit card transctions",
    packages = find_packages(),
    install_requires = load_requirements("requirements.txt")
)