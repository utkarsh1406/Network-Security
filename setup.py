from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    ''' This function reads the environment requirements 
    and return it in the form of list'''
    requirement_list = []
    try:
        with open('requirements.txt','r') as file:
            # Read the file line by line
            lines = file.readlines()
            # Ingore empty lines
            for line in lines:
                # removing the empty lines
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found!')
    
    return requirement_list


setup(
    name="Network-Security",
    version="0.0.1",
    author="Utkarsh",
    author_email="utkarsh.p1406@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A Python project for network security.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/utkarsh1406/Network-Security",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)