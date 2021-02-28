Thank you for contributing!
===========================

Thank you for considering a contribution to Sphinx reStructuredText
builder/writer, and for reading this document.

Use issues for bug reports, feature requests, or any sort of feedback
that you may have.

If you are able to spend the time to create a pull request, that is
most appreciated.


Testing your code
=================

* Run `pytest`_ to run all tests using your default Python version and
  Sphinx version.

* Run `pytest -k testName` to only run the test called testName.

* For testing, Sphinx is run for each test in the `tests/datasets`
  directory, and the output is written to the `output` directory.
  The result is then compared to the expected output in
  `tests/expected`.

* Rather than a byte-by-byte comparison, `output` and `tests/expected`
  are compared after reading the file with docutils (which contains a
  basic reStructuredText parser), to allow for slight variations in
  layout.

* If a test fails, the XML version of the parsed documents is written
  to the `output` directory. `test-file.expected.xml` for
  `test-file.rst` in `tests/expected`, and `test-file.output.xml` for
  `test-file.rst` in `output`.

* Optionally run `pytest -v -r A -W d` for a very verbose output,
  including stdout and stderr for all tests (note that some tests like
  nonexistent-target.rst are expected to give a warning), and including
  all Python warnings.

* To test with multiple Python version and Sphinx versions, run `tox`_.

* Run `tox -e python3.9-sphinx3.4` to run tox with a specific Python
  and Sphinx version.

* Each commit to master, and each pull request to the master branch is
  tested with a few different tests. See the actions tab for the
  results of each run, or click on the checkmark (✔ or ✘) listed with
  each commit.

.. _pytest: https://www.pytest.org/
.. _tox: https://tox.readthedocs.io/


Supported versions
==================

* See `.github/workflows/tests.yml` for a list of which version are
  tested for by GitHub after each pull request.

* See `tox.ini` for a list of which version are tested for by `tox`.
  These two files should be kept in sync.

* As a rule of thumb, this project supports all Sphinx versions
  starting from the one that came with the previous stable Debian
  distribution (`oldstable/sphinx-doc`_) till the most recent version.
  It supports all Python versions starting with the one that came with
  the previous stable Debian distribution (`oldstable/python3`_).

* Python 2 is no longer supported, and no test is run for it.
  We will consider small pull requests to add Python 2.7 support, if
  you really want to spend this effort.

.. _`oldstable/sphinx-doc`: https://packages.debian.org/oldstable/sphinx-doc
.. _`oldstable/python`: https://packages.debian.org/oldstable/python3


Publishing versions
===================

The code is available on the Python package index at
https://pypi.org/project/sphinxcontrib-restbuilder/.

This section is only relevant for administrators.

Creating a release
------------------

Change the following files::

    CHANGES.rst
    CONTRIBUTORS.txt   (Add new contributors, if any)
    setup.py           (Change version constant)

Commit the changes, add a tag, and upload the changes::

    git add CHANGES.rst CONTRIBUTORS.txt setup.py
    git commit -m "Bump version number to x.y.z"
    git tag -a version-x.y.z HEAD
    git push --tags

Publish a release at GitHub
---------------------------

* Go to https://github.com/sphinx-contrib/restbuilder/releases
* Click the "Draft a new release" button
* Select the tag, and add a Release title (e.g. Sphinx Restbuilder x.y)
  and release notes. I usually only list the most important changes,
  with optional link to CHANGES.rst for more details.

Publish a release at PyPI
-------------------------

Follow the process described at https://packaging.python.org/tutorials/distributing-packages/.

Install requirements::

    pip install --upgrade pip
    pip install setuptools wheel twine

Create both a source (.tar.gz) and wheel (.whl) distribution::

    python setup.py sdist
    python setup.py bdist_wheel --universal

Upload all that was created to PyPI::

    ls dist/
    twine upload dist/*
