from distutils.core import setup
import setuptools


setup(
    name='ludumcli',
    version='1.2',
    install_requires=[
        'requests',
        'bs4'
    ],
    packages=[
        'ludumcli',
    ],
    entry_points={
        "console_scripts": [
            "ludumcli = ludumcli.program:run"
        ]
    }
)
