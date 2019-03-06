from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="testing_pubsub",
    version="0.0.1",
    author="Steven Harlow",
    author_email="stharlow  gmail",
    description="Run a temporary instance of Cloud PubSub emulator for Python tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peachfinance/testing_pubsub",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: APACHE SOFTWARE LICENSE",
    ],
)
