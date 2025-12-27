# setup.py is used to package and distribute the Python project.
from setuptools import setup, find_packages
from typing import List

HYPHON_E_DOT = "-e ."


def get_requirements(file_path: str) -> list[str]:
    """Read the requirements from a file and return as a list."""


    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

    return requirements

setup(    name='my_ml_project',
    version='0.0.1',
    author='Abdul Rehman Shakeel',
    author_email="abdulrehmanshakeel@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    description="A machine learning project setup example",
)
