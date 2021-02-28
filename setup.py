# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
Sphinx_ extension to build reST (reStructuredText_) files.

This extension is in particular useful to use in combination with the autodoc
extension to automatically generate documentation for use by any rst parser
(such as the GitHub wiki).

In itself, the extension is fairly straightforward -- it takes the parsed reST 
file from Sphinx_ and outputs it as reST.

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
'''

requires = ['Sphinx>=1.4']

setup(
    name='sphinxcontrib-restbuilder',
    version='0.3',
    url='https://github.com/sphinx-contrib/restbuilder',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-restbuilder',
    license='BSD 2-Clause',
    author='Freek Dijkstra',
    author_email='freek@macfreek.nl',
    description='Sphinx extension to output reST files.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup :: reStructuredText',
    ],
    platforms='any',
    python_requires='>=2.7, !=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
