from setuptools import setup, find_packages

setup(
    name="py_dimensional",
    version="0.1.0",
    packages=find_packages(exclude=["tests*", "examples*"]),
    install_requires=[
        "httpx",
        "pydantic",
        "python-dotenv",
    ],  # Add your dependencies here
    url="https://github.com/hdresearch/py-dimensional",
    license="Apache License 2.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
