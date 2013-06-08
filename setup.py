from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.simplesalesforce',
      version=version,
      description="Salesforce REST API via simple-salesforce",
      long_description=open("README.md"),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github/jlantz/collective.simplesalesforce',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'simple-salesforce',
          'five.grok',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
          'test': [
              'plone.app.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,

      )
