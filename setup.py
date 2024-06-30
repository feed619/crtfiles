from setuptools import setup

setup(
    name='crt',
    version='0.2',
    py_modules=['repos'],
    entry_points={
        'console_scripts': [
            'repos=scripts.scripts:main',
        ],
    },
)
