import os
from setuptools import setup, find_packages, Extension
from version import version

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='gtfs_canonical_validator',
    version=version,
    author='Sujata Misra',
    author_email='sujatam@gaussiansolutions.com',
    description='Package is used for validate the canonical data.',
    long_description=long_description,
    project_urls={
        'Documentation': 'https://github.com/TaskarCenterAtUW/TDEI-mobilitydata-canonical-validator/blob/main/README.md',
        'GitHub': 'https://github.com/TaskarCenterAtUW/TDEI-mobilitydata-canonical-validator',
        'Changelog': 'https://github.com/TaskarCenterAtUW/TDEI-mobilitydata-canonical-validator/blob/main/CHANGELOG.md'
    },
    long_description_content_type='text/markdown',
    url='https://github.com/TaskarCenterAtUW/TDEI-mobilitydata-canonical-validator',
    install_requires=[
        'requests'
    ],
    packages=find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    package_dir={'': 'src'},
)