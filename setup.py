# setup.py
from setuptools import setup, find_packages
NAME = "crt"
setup(
    name=NAME,
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'crt=crt.cli:main',
        ],
    },
)
