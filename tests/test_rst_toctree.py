import os

import pytest

from tests.utils import build_sphinx, assert_doc_equal, parse_doc


@pytest.fixture
def toctree_src_dir():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'datasets', 'toctree'
    )


@pytest.fixture
def expected_toctree_dir():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'expected', 'toctree'
    )


def test_toctree(toctree_src_dir, expected_toctree_dir):
    out_dir = build_sphinx(toctree_src_dir)

    assert_doc_equal(
        parse_doc(out_dir, 'index'),
        parse_doc(expected_toctree_dir, 'index'),
    )

    assert_doc_equal(
        parse_doc(out_dir, 'doc1'),
        parse_doc(expected_toctree_dir, 'doc1'),
    )

    assert_doc_equal(
        parse_doc(out_dir, 'doc2'),
        parse_doc(expected_toctree_dir, 'doc2'),
    )
