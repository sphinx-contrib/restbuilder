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

* To test with multiple Python version and Sphinx versions, run `tox`_.

* Run ``tox -e python3.9-sphinx3.4`` to run tox with a specific Python
  and Sphinx version.

* Each commit to master, and each pull request to the master branch is
  tested with a few different tests. See the actions tab for the
  results of each run, or click on the checkmark (✔ or ✘) listed with
  each commit.

.. _pytest: https://www.pytest.org/
.. _tox: https://tox.readthedocs.io/


Adding and debugging tests
==========================

* For testing, Sphinx is run for each test in the ``tests/datasets``
  directory, and the output is written to the ``output`` directory.
  The result is then compared to the expected output in
  ``tests/expected``.

* Specific features should be accompanied by a test.

* Add a test file to one of the subdirectories in ``tests/datasets``,
  add the expected outcome to ``tests/expected``, and create a
  test runner in one of the ``test_*.py`` files in `tests`.

* Run ``pytest -k testName`` to only run the test called testName.

* Optionally run ``pytest -v -r A -W d`` for a very verbose output,
  including stdout and stderr for all tests (note that some tests like
  `nonexistent-target.rst` are expected to give a warning), and
  including all Python warnings.

* Rather than a byte-by-byte comparison, ``output`` and
  ``tests/expected`` are compared after reading the file with docutils
  (which contains a basic reStructuredText parser), to allow for slight
  variations in layout.

* If a test fails, the XML version of the parsed documents is written
  to the ``output`` directory. ``test-file.expected.xml`` for
  ``test-file.rst`` in ``tests/expected``, and ``test-file.output.xml``
  for ``test-file.rst`` in ``output``.

* If you want to see what to see how Sphinx parses a rst file, run e.g.
  ``sphinx-build -b xml -C tests/datasets output``. You can also
  specify ``-b html`` for HTML output. Beware that ``-b rst`` will use
  the restbuilder installed using pip, not the git checkout. This is
  most likely not what you intended. Run ``pytest`` instead.

* Sphinx will read all files in a directory. So multiple tests in the
  same directory are not standalone! This means that you should not use
  the same identifier for hyperlink targets in different tests, as they
  may inadvertedly point to a target in a different file.
  Either use unique target names, or use a separate subdirectory for
  your test.


Supported versions
==================

* See ``.github/workflows/tests.yml`` for a list of which version are
  tested for by GitHub after each pull request.

* See ``tox.ini`` for a list of which version are tested for by ``tox``.
  These two files should be kept in sync.
  (Note: at this moment, ``tox`` will still run Python 2.7 tests; 
  GitHub will not.)

* As a rule of thumb, this project supports all Sphinx versions
  starting from the one that came with the previous stable Debian
  distribution (`oldstable/sphinx-doc`_) till the most recent version.
  It supports all Python versions starting with the one that came with
  the previous stable Debian distribution (`oldstable/python3`_).
  This is currently Python 3.5 with Sphinx 1.4.

* Python 2.7 is partially supported: some basis tests will work, but
  other tests are known to fail are disabled. We consider pull requests
  to add Python 2.7 support for these features, but will not actively
  fix it ourselves.

* The same applies for Sphinx 1.4 - 1.8. Sphinx 1.x is partially
  supported: some basis tests will work, but other tests are known to
  fail, and are disabled. We consider pull requests to add Sphinx 1.x
  support for these features, but will not actively fix it ourselves.
  Look for ``@pytest.mark.skipif`` decorators in the test functions to
  see which features are currently not supported.

.. _`oldstable/sphinx-doc`: https://packages.debian.org/oldstable/sphinx-doc
.. _`oldstable/python3`: https://packages.debian.org/oldstable/python3


Publishing versions
===================

The code is available on the Python package index (PyPI) at
https://pypi.org/project/sphinxcontrib-restbuilder/.

*This following section is only relevant for maintainers.*

Creating a release
------------------

Change the following files::

    CHANGES.rst
    CONTRIBUTORS.txt                (Add new contributors, if any)
    sphinxcontrib/restbuilder.py    (Change version constant)

Commit the changes, add a tag, and upload the changes::

    git add CHANGES.rst CONTRIBUTORS.txt sphinxcontrib/restbuilder.py
    git commit -m "Bump version number to 0.1.2"
    git tag -a v0.1.2 HEAD
    git push --tags

Publish a release at GitHub
---------------------------

* Go to https://github.com/sphinx-contrib/restbuilder/releases
* Click the "Draft a new release" button
* Select the tag, and add a Release title (e.g. Sphinx Restbuilder 0.1.2)
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
