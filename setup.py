from setuptools import setup
from os import path


top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
   name='proxy_manager',
   version='1.0',
   description='Proxy Manager module',
   long_description=long_description,
   author='Genzo',
   author_email='genzo@bk.ru',
   packages=['proxy_manager'],
   install_requires=['requests'],
)