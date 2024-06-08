from setuptools import setup, find_packages
from typing import List

setup(
    name="Simple component generator",
    version="0.0.1",
    author="horheynm",
    author_email="george.scratch.dev@gmail.com",
    license="Apache 2.0",
    description="LLM agent for simple react component generation",
    package_dir={"": "src"},
    packages=find_packages("src", include=["api"]),
)
