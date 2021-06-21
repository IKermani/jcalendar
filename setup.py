import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jcalendar",
    version="0.1.1",
    author="Iman Kermani",
    author_email="imankermani97@outlook.com",
    description="Jalali calendar binding for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IKermani/jcalendar",
    project_urls={
        "Bug Tracker": "https://github.com/IKermani/jcalendar/issues",
    },
    install_requires=['jdatetime==3.6.2'],
    classifiers=[
        "Programming Language :: Python :: 3",
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
