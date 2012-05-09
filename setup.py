from setuptools import setup, find_packages
import os

version = '0.1a'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='templer.plone.localcommands',
      version=version,
      description="local commands for plone templates in the templer system",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='zope plone python',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='http://github.com/collective/templer.plone.localcommands',
      license='mit',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['templer', 'templer.plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
