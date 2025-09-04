from setuptools import setup, find_packages

setup(
    name="ViviEngine",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.5.0",
    ],
    python_requires=">=3.12",
    author="LeDarron",
    author_email="",
    description="A simple Python game engine",
    license="MIT",
)
