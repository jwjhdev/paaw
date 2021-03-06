"""paaw setup.py"""

import re
from codecs import open
from os import path

from setuptools import find_packages, setup

PACKAGE_NAME = "paaw"
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.rst"), encoding="utf-8") as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

extras = {
    "ci": ["coveralls"],
    "dev": ["pre-commit"],
    "lint": ["black", "flake8", "pydocstyle", "sphinx", "sphinx_rtd_theme"],
    "test": [
        "betamax >=0.8, <0.9",
        "betamax-matchers >=0.3.0, <0.5",
        "betamax-serializers >=0.2, <0.3",
        "mock >=0.8",
        "pytest >=2.7.3",
    ],
}
extras["dev"] += extras["lint"] + extras["test"]

setup(
    name=PACKAGE_NAME,
    author="James Hannah",
    author_email="jwjhdev@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    description=(
        "The Python AFL API Wrapper (PAAW) is a Python package "
        "that allows for simple access to the AFL.com.au API."
    ),
    extras_require=extras,
    install_requires=[
        "requests >=2.23.0",
    ],
    keywords="afl api wrapper",
    license="Simplified BSD License",
    long_description=README,
    package_data={
        "": ["LICENSE.txt"],
        PACKAGE_NAME: ["*.ini", "images/*.jpg"],
    },
    packages=find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    url="https://paaw.readthedocs.org/",
    version=VERSION,
)