#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="MechanicBuddy",
    author_email="dev@mechanicbuddy.co.za",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Use AWS Application load balancer authentication with Cognito and Django",
    install_requires=[
        'Django>=2.2.10,<2.3',
        'requests',
    ],
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"djangito": ["py.typed"]},
    include_package_data=True,
    keywords="djangito",
    name="djangito",
    package_dir={"": "src"},
    packages=find_packages(include=["src/djangito", "src/djangito.*"]),
    setup_requires=[],
    url="https://github.com/mechanicbuddy/djangito",
    version="0.1.0",
    zip_safe=False,
)
