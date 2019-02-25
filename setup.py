from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(name='reMCpMC',
      version='0.1',
      description='Statistical model checking of pMC',
      long_description=readme,
      author='',
      packages=find_packages(exclude=('tests')))
