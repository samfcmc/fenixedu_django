#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='fenixedu_django',
		version='1.0.1',
		description='FenixEdu Django utilities',
		author='Samuel Coelho',
		author_email='samuelfcmc@gmail.com',
		url='https://github.com/samfcmc/fenixedu_django',
		setup_requires=['fenixedu'],
		install_requires=['fenixedu'],
		packages=['fenixedu.authentication']
		)