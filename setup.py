from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT="-e ."
def get_requirements(file_path:str) -> List[str]:
    try:
        requirements = []
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements= [req.replace("\n", "") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
        return requirements"""
    

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Masasa H A',
    author_email='hamanasa20@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)