from setuptools import setup, find_packages

setup(
    name="krona-tools",
    version="2.8.1",
    packages=find_packages(include=["KronaTools", "KronaTools.*"]),
)

