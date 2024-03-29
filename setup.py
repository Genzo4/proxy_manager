from setuptools import setup
from os import path


top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
   name='proxy_manager_g4',
   version='1.1.0',
   description='Proxy Manager',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Genzo',
   author_email='genzo@bk.ru',
   url='https://github.com/Genzo4/proxy_manager',
   project_urls={
           'Bug Tracker': 'https://github.com/Genzo4/proxy_manager/issues',
       },
   classifiers=[
      'Development Status :: 4 - Beta',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Topic :: Internet :: Proxy Servers'
   ],
   keywords=['proxy', 'proxy_manager', 'manager', 'proxy-manager', 'proxymanager', 'g4'],
   license='MIT',
   packages=['proxy_manager_g4'],
   install_requires=['requests'],
   python_requires='>=3.6'
)