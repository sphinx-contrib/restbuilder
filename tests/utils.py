from os.path import join
try:
    from itertools import zip_longest
except ImportError:
    # Python 2.7 support.
    from itertools import izip_longest as zip_longest
import io

import docutils
from docutils.frontend import OptionParser
from docutils.nodes import Text, Element, system_message
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from docutils.core import publish_from_doctree
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
        output_text = output.replace('\r\n', ' ')
        output_text = output_text.replace('\n', ' ')
        expected_text = expected.replace('\r\n', ' ')
        expected_text = expected_text.replace('\n', ' ')
        assert output_text == expected_text
    elif isinstance(output, system_message):
        assert len(output.children) == len(expected.children)
        # Don't check specifics of system_messages (warnings)
        # E.g. the line number may be off
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
    with io.open(join(dir, file + '.rst'), encoding='utf-8') as fh:
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
        output_doc = parse_doc(output_dir, file)
        expected_doc = parse_doc(expected_dir, file)
        try:
            assert_doc_equal(output_doc, expected_doc)
        except AssertionError:
            # output XML version of doctree for easier debugging
            with open(join(output_dir, file + '.output.xml'), 'wb') as fw:
                fw.write(publish_from_doctree(output_doc, writer_name='xml'))
            with open(join(output_dir, file + '.expected.xml'), 'wb') as fw:
                fw.write(publish_from_doctree(expected_doc, writer_name='xml'))
            raise



if __name__ == '__main__':
    pass
