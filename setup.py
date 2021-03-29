# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def get_restbuilder_version():
    # load sphinxcontrib.restbuilder from local path.
    # (Lots of work, just to get the version info)
    from os.path import join, dirname
    import sys
    restbuilder_path = join(dirname(__file__), 'sphinxcontrib', 'restbuilder.py')
    if sys.version_info >= (3, 5):
        # requires Python 3.5 or up.
        import importlib.util
        spec = importlib.util.spec_from_file_location('sphinxcontrib.restbuilder', restbuilder_path)
        restbuilder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(restbuilder)
    else:
        # Python 2.7 support
        import imp
        restbuilder = imp.load_source('sphinxcontrib.restbuilder', restbuilder_path)
    return restbuilder.__version__

long_desc = '''
Sphinx_ extension to build and write reStructuredText_ (reST / rst) files.

This extension is in particular useful to use in combination with the autodoc
extension to automatically generate documentation for use by any rst parser
(such as the GitHub wiki, which does not support the advanced Sphinx directives).

In itself, the extension is fairly straightforward -- it takes the parsed
reStructuredText file from Sphinx_ and outputs it as reStructuredText.

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
'''

requires = ['Sphinx>=1.4', 'docutils']

setup(
    name='sphinxcontrib-restbuilder',
    version=get_restbuilder_version(),
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
