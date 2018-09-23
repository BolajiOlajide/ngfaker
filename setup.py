"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ng-faker',
    version='1.0.0',
    description='A python library to generate fake nigerian data',
    long_description=long_description,
    url='https://github.com/BolajiOlajide/ngfaker',

    # Author details
    author='Bolaji Olajide',
    author_email='cooproton@gmail.com',

    license='MIT',

    keywords='ngfaker faker python fake generate names yoruba igbo hausa',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    extras_require={
        'test': ['coverage'],
    },
)
