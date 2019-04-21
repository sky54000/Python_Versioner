from setuptools import setup, find_packages

long_description=""
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pversioner",
    version="0.0.1",
    description="Python versioner (pversioner)",
    author="Le Baron Quentin, Nassoy Robin",
    author_email="quentin.lebaron@smile.fr, robin.nassoy@gmail.com",
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
                        "yamllint",
                        "argparse-graph",
                        "docker",
                        "beautifulsoup4",
                        "requests"],
    packages=find_packages(exclude=("tests",)),
    tests_require=["pytest"],
    # package_data={"pversioner": ["resources/scenarios.yml"]},
    scripts=["script/pversioner"],
    classifiers=[
    "Programming Language :: Python :: 3.5",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    ],)
