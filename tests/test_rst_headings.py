from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_headings(common_src_dir, expected_common_dir, output_dir):
    build_sphinx(common_src_dir, output_dir, ['headings'])

    assert_doc_equal(
        parse_doc(output_dir, 'headings'),
        parse_doc(expected_common_dir, 'headings'),
    )
