import os
from setuptools import setup, find_packages


def readme(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="ua_stache_api",
    version="1.0.0",
    packages=find_packages(),
    author="Stephen Stern, Rafael Lopez",
    author_email="sterns1@email.arizona.edu",
    long_description=readme('README.md'),
    license="MIT"
)
