from setuptools import setup, find_packages

required_packages = [
    "annotated-types==0.7.0",
    "anyio==4.4.0",
    "certifi==2024.6.2",
    "distro==1.9.0",
    "h11==0.14.0",
    "httpcore==1.0.5",
    "httpx==0.27.0",
    "idna==3.7",
    "openai==1.33.0",
    "pydantic==2.7.3",
    "pydantic_core==2.18.4",
    "python-dotenv==1.0.1",
    "setuptools==70.0.0",
    "sniffio==1.3.1",
    "tqdm==4.66.4",
    "typing_extensions==4.12.2",
]

extra_reqs = {
    "dev": [
        "annotated-types==0.7.0",
        "anyio==4.4.0",
        "certifi==2024.6.2",
        "distro==1.9.0",
        "h11==0.14.0",
        "httpcore==1.0.5",
        "httpx==0.27.0",
        "idna==3.7",
        "openai==1.33.0",
        "pydantic==2.7.3",
        "pydantic_core==2.18.4",
        "python-dotenv==1.0.1",
        "setuptools==70.0.0",
        "sniffio==1.3.1",
        "tqdm==4.66.4",
        "typing_extensions==4.12.2",
    ]
}


setup(
    name="Code Agent",
    version="0.0.1",
    author="horheynm",
    author_email="george.scratch.dev@gmail.com",
    license="Apache 2.0",
    description="LLM agent for simple react component generation",
    package_dir={"": "src"},
    packages=find_packages("src", include=["api"]),
    install_requires=required_packages,
    extras_require=extra_reqs,
)
