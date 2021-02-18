from os.path import join
from itertools import zip_longest

import docutils
from docutils.frontend import OptionParser
from docutils.nodes import Text, Element
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from sphinx.application import Sphinx

# sphinx.util.docutils requires Sphinx 1.5 and up.
try:
    from sphinx.util.docutils import docutils_namespace
except ImportError:
    # Attempt to support Sphinx 1.4 and thus the old Debian Stretch (oldstable)
    from copy import copy
    from contextlib import contextmanager
    from docutils.parsers.rst import directives, roles
    @contextmanager
    def docutils_namespace():
        """Create namespace for reST parsers."""
        try:
            _directives = copy(directives._directives)
            _roles = copy(roles._roles)
            yield
        finally:
            directives._directives = _directives
            roles._roles = _roles


def build_sphinx(src_dir, output_dir, files=None, config={}):
    doctrees_dir = join(output_dir, '.doctrees')

    filenames = []
    force_all = True

    default_config = {
        'extensions': ['sphinxcontrib.restbuilder'],
        'master_doc': 'index',
    }
    default_config.update(config)
    config = default_config

    if files:
        force_all = False
        filenames = [join(src_dir, file + '.rst') for file in files]
        config['master_doc'] = files[0]

    with docutils_namespace():
        app = Sphinx(
            src_dir,
            None,
            output_dir,
            doctrees_dir,
            'rst',
            confoverrides=config,
            verbosity=0,
        )

        app.build(force_all=force_all, filenames=filenames)


def assert_node_equal(output, expected):
    assert type(output) == type(expected)
    if isinstance(output, Text):
        assert output == expected
    elif isinstance(output, Element):
        assert len(output.children) == len(expected.children)
        assert output.attributes == expected.attributes
    else:
        raise AssertionError


def assert_doc_equal(output_doc, expected_doc):
    """
    Can be used to compare two documents, ignoring any whitespace changes
    """
    for output, expected in zip_longest(
        output_doc.traverse(include_self=False), expected_doc.traverse(include_self=False)
    ):
        assert_node_equal(output, expected)


def parse_doc(dir, file):
    parser = Parser()
    with open(join(dir, file + '.rst')) as fh:
        doc = new_document(
            file,
            OptionParser(
                components=(docutils.parsers.rst.Parser,)
            ).get_default_values(),
        )
        parser.parse(
            fh.read(),
            doc,
        )
        return doc


def run_parse_test(src_dir, expected_dir, output_dir, subdir, files):
    src_dir = join(src_dir, subdir)
    expected_dir = join(expected_dir, subdir)
    output_dir = join(output_dir, subdir)
    build_sphinx(src_dir, output_dir, files)

    for file in files:
        assert_doc_equal(
            parse_doc(output_dir, file),
            parse_doc(expected_dir, file),
        )



if __name__ == '__main__':
    pass
