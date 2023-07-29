from setuptools import setup, find_packages

import myapp

setup(
  name='myapp_package',
  version=myapp.__version__,
  author=myapp.__author__,
  url='https://test.pypi.org/user/nguyenanh/',
  author_email='susu4691@gmail.com',
  description='my test wheel',
  packages=find_packages(include=['myapp']),
  entry_points={
    'group_1': 'run=myapp.__main__:main'
  },
  install_requires=[
    'setuptools'
  ]
)