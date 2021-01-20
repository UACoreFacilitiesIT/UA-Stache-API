import os
from setuptools import setup, find_packages


def readme(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    with open(full_path, 'r') as file:
        return file.read()


setup(
    name="ua_stache_api",
    version="2.0.1",
    packages=find_packages(),
    author="Stephen Stern, Rafael Lopez",
    author_email="sterns1@email.arizona.edu",
    description=(
        "Allows the caller to easily get 'secret' information from stache"
        " entries at [https://stache.arizona.edu]."),
    long_description=readme("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/UACoreFacilitiesIT/UA-Stache-API",
    license="MIT",
    install_requires=["requests"],
)
