import os
import shutil
from itertools import zip_longest

import docutils
from docutils.frontend import OptionParser
from docutils.nodes import Text, Element
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from sphinx.application import Sphinx
from sphinx.util.docutils import docutils_namespace


def build_sphinx(src_dir, files=None):
    out_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'output')
    shutil.rmtree(out_dir, ignore_errors=True)

    doctrees_dir = os.path.join(out_dir, '.doctrees')

    filenames = []
    force_all = True

    config = {'extensions': ['sphinxcontrib.restbuilder']}

    if files:
        force_all = False
        filenames = [os.path.join(src_dir, file + '.rst') for file in files]
        config['master_doc'] = files[0]

    with docutils_namespace():
        app = Sphinx(
            src_dir,
            None,
            out_dir,
            doctrees_dir,
            'rst',
            confoverrides=config,
            verbosity=0,
        )

        app.build(force_all=force_all, filenames=filenames)
    return out_dir


def assert_node_equal(n1, n2):
    assert type(n1) == type(n2)
    if isinstance(n1, Text):
        assert n1 == n2
    elif isinstance(n1, Element):
        assert len(n1.children) == len(n2.children)
        assert n1.attributes == n2.attributes
    else:
        raise AssertionError


def assert_doc_equal(doc1, doc2):
    """
    Can be used to compare two documents, ignoring any whitespace changes
    """
    for n1, n2 in zip_longest(
        doc1.traverse(include_self=False), doc2.traverse(include_self=False)
    ):
        assert_node_equal(n1, n2)


def parse_doc(dir, file):
    parser = Parser()
    with open(os.path.join(dir, file + '.rst')) as fh:
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
