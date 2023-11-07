from  setuptools import find_packages,setup
from typing import List


variable='-e .'
def get_requirements(file_path:str)->List[str]:
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requiremnts]
        if variable in requiremnts:
            requiremnts.remove(variable)
        return requiremnts

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Utkarsh Jhariya',
    author_email='jutkarsh027@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)