from tests.utils import build_sphinx, assert_doc_equal, parse_doc

def test_versionadded(sphinx_directives_src_dir, expected_sphinx_directives_dir, output_dir):
    build_sphinx(sphinx_directives_src_dir, output_dir, ['versionadded'])

    assert_doc_equal(
        parse_doc(output_dir, 'versionadded'),
        parse_doc(expected_sphinx_directives_dir, 'versionadded'),
    )

def test_versionchanged(sphinx_directives_src_dir, expected_sphinx_directives_dir, output_dir):
    build_sphinx(sphinx_directives_src_dir, output_dir, ['versionchanged'])

    assert_doc_equal(
        parse_doc(output_dir, 'versionchanged'),
        parse_doc(expected_sphinx_directives_dir, 'versionchanged'),
    )

def test_deprecated(sphinx_directives_src_dir, expected_sphinx_directives_dir, output_dir):
    build_sphinx(sphinx_directives_src_dir, output_dir, ['deprecated'])

    assert_doc_equal(
        parse_doc(output_dir, 'deprecated'),
        parse_doc(expected_sphinx_directives_dir, 'deprecated'),
    )
