from tests.utils import build_sphinx, assert_doc_equal, parse_doc

def test_versionadded(sphinx_src_dir, expected_sphinx_dir):
    out_dir = build_sphinx(sphinx_src_dir, ['versionmodified'])

    assert_doc_equal(
        parse_doc(out_dir, 'versionmodified'),
        parse_doc(expected_sphinx_dir, 'versionmodified'),
    )
