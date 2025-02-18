from setuptools import setup, find_packages

long_description = open("README.rst").read()

setup(
    name="us-aidentified",
    version="3.0.2",
    author="Jeremy Carbaugh",
    author_email="jeremy@jcarbaugh.com",
    url="https://github.com/dgilmanAIDENTIFIED/python-us",
    description="US state meta information and other fun stuff",
    long_description=long_description,
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["jellyfish<1.0"],
    entry_points={"console_scripts": ["states = us.cli.states:main"]},
    platforms=["any"],
    classifiers=[
        # N.B. 3.6 is untested and should be dropped
        # in coming releases.
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
