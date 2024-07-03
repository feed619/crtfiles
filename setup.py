# setup.py
from setuptools import setup, find_packages
NAME = "crtfiles"
setup(
    name=NAME,
    version='1.0',
    author="feed619",
    author_email="azimovpro@gmail.com",
    description="create files quickly and conveniently",
    url="https://github.com/feed619/crtfiles",
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'crt=crt.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        'crt': ['data/templates.json'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
