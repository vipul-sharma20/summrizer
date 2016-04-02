from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='summrizer',

    version='1.0.0.dev1',

    description='A text summarizing script',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/vipul-sharma20/summrizer',

    # Author details
    author='Vipul Sharma',
    author_email='vipul.sharma20@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='nlp summary',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['nltk>=3.1'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
