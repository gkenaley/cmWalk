from setuptools import setup, find_packages
import os
# To use a consistent encoding
from codecs import open
from cmwalk import version


# Get the long description from the README file
def readme():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        return f.read().replace('\r', '')


setup(name='cmwalk',
      version=version.VERSION,
      description='Update of a python script which walks the directory tree of a C/C++ project and generates CMakeLists.txt ',
      long_description=readme(),
      long_description_content_type='text/x-rst; charset=UTF-8',
      keywords = ['cmake'],
      classifiers=[],
      url='https://github.com/gkenaley/cmWalk',
      author='Gary Kenaley',
      author_email='garykenaley@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['jinja2', 'walkdir'],
      entry_points={
          'console_scripts': [
              'cmwalk = cmwalk.cmwalk:main'
          ]
      },
      zip_safe=False)
