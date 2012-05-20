from setuptools import setup, find_packages

version = '1.0b1'

long_description = (
    open('README.rst').read()
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
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Buildout",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Software Development :: Code Generators",
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
          'templer.localcommands',
          'templer.plone',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [templer.templer_sub_template]
      contenttype = templer.plone.localcommands.archetype:ContentType
      schema_field = templer.plone.localcommands.archetype:ATSchemaField
      browserview = templer.plone.localcommands.plone:View
      browserlayer = templer.plone.localcommands.plone:BrowserLayer
      """,
      )
