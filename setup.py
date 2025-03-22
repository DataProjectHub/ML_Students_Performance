# setup.py is used to build our application as a package
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # to automatically trigger requirements.txt 

def get_requirements(file_path:str)->List[str]: # to get the libraries in requirements.txt
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # reading the list of library in reuirements.txt
        requirements=[req.replace("\n","")for req in requirements] # replacing \n with blank while reading
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # while running the code, -e . is not required.
    
    return requirements


setup(
name="ML Project CI CD Automation",
version="0.0.1",
author="Pooja Anilkumar",
author_email="pujaa22@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt") # to install the dependencies
)