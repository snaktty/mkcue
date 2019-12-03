from setuptools import setup, find_packages
import mkcue

setup(
    name='mkcue',
    version=mkcue.__version__,
    packages=find_packages(exclude=['tests']),
    entry_points='''
          [console_scripts]
          mkcue = mkcue.main:main
      ''',
    install_requires=[
        'click',
    ])
