import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
    'bs4',
    'iterfzf',
    'requests'
]

setup(
    name = "doc-fzf",
    version = "0.0.6",
    author = "Guillermo Garcia",
    author_email = "memogarcia@protonmail.com",
    description = "Fuzzy Search documentation from the CLI",
    license = "WTFPL",
    keywords = "documentation fzf fuzzy search",
    url = "https://gitlab.com/memogarcia/doc-fzf",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'doc-fzf = doc_fzf.main:main',
        ],
    },
    install_requires=install_requires,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)