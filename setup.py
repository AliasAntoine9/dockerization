from setuptools import setup, find_packages

with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()


setup(
    name="dockerization",
    version="1.0.0",
    author="alias",
    author_email="alias@fake_mail.com",
    description="Fake API",
    include_data_package=True,
    packages=find_packages(include=["api", "api.*"]),
    python_requires=">=3.10",
    install_requires=requirements
)
