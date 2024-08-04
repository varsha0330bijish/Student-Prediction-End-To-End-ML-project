from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # '-e.' means that python packages should be installed in editable function
def get_requirements(file_path:str)->List[str]: # this function will read the requirements.txt line by line
    
    
    requirements=[]
    with open(file_path) as file_obj:# The open function is used to open the file located at file_path. The with statement ensures that the file is properly closed after reading, even if an error occurs
        requirements=file_obj.readlines()# assigning requiere.tx as file object to be read problem ;creats '/n'
        requirements=[req.replace("\n","") for req in requirements] # /n gets added every time a line or element is read, so to remove it.

        if HYPEN_E_DOT in requirements: # in requiremnt.tx -e. like a tracker but it should be included in the list
            requirements.remove(HYPEN_E_DOT) # hence we are removing it
    
    return requirements


setup(
    name="Student-Prediction-End-To-End-ML-project",
    version='0.0.1',
    author='varsha',
    author_email='varshabijish@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') # a function is created in "def get_requirements" instead of [panda,seaborn]
    )




