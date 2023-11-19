from setuptools import setup, find_packages

from api import __version__, __app_name__

with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()


setup(
    name=__app_name__,
    version=__version__,
    author="alias",
    author_email="alias@fake_mail.com",
    description="Fake API",
    include_data_package=True,
    packages=find_packages(include=["api", "api.*"]),
    python_requires=">=3.10",
    install_requires=requirements
)
