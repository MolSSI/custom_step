#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Pmw', 'logging', 'seamm_util', 'seamm', 'pprint', 'PyYAML>=5.1'
]
# 'os',
# 'yaml',  is PyYAML

setup_requirements = [
    # tmp pws 'pytest-runner',
    # TODO(paulsaxe): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='custom_step',
    version='0.1.0',
    description="Custom stage for Python code",
    long_description=readme + '\n\n' + history,
    author="Paul Saxe",
    author_email='psaxe@molssi.org',
    url='https://github.com/molssi-seamm/custom_step',
    packages=find_packages(include=['custom_step']),
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='custom_step',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Materials Science',
        'Topic :: Scientific/Engineering :: Computational Materials Science',
        'Topic :: Scientific/Engineering :: Computational Molecular Science',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3  :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    entry_points={
        'org.molssi.seamm': ['Python = custom_step:CustomStep',],
        'org.molssi.seamm.tk': ['Python = custom_step:CustomStep',],
    }
)
