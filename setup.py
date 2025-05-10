from setuptools import find_packages, setup
from typing import List

hypn = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [re.replace("\n", "") for re in requirements]

        if hypn in requirements:
            requirements.remove(hypn)

    return requirements

setup(
    name='miniproject',
    version='0.0.1',
    author='Adarsh',
    author_email='salunkheadarsh8@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
