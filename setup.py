import setuptools
import os

with open(os.path.dirname(os.path.realpath(__file__)) + '/requirements.txt') as fh:
    install_requires = fh.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jcalendar",
    version="0.1.0",
    author="Iman Kermani",
    author_email="imankermani97@outlook.com",
    description="Jalali calendar binding for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IKermani/jcalendar",
    project_urls={
        "Bug Tracker": "https://github.com/IKermani/jcalendar/issues",
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
