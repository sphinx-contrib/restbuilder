# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def get_restbuilder_version():
    # load sphinxcontrib.restbuilder from local path.
    from os.path import join, dirname
    import importlib.util
    restbuilder_path = join(dirname(__file__), 'sphinxcontrib', 'restbuilder.py')
    spec = importlib.util.spec_from_file_location('sphinxcontrib.restbuilder', restbuilder_path)
    restbuilder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(restbuilder)
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

requires = ['Sphinx>=5.0', 'docutils']

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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup :: reStructuredText',
    ],
    platforms='any',
    python_requires='>=3.10',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
