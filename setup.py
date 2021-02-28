from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ci_github_actions',
    version='0.0.1',
    url='https://github.com/j0hanj0han/ci-github-actions.git',
    author='j0hanj0han',
    author_email='author@gmail.com',
    description='sandbox for github actions',
    packages=find_packages(),    
    install_requires=requirements,
)