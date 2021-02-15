from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_paragraph(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['paragraph'])

    assert_doc_equal(
        parse_doc(out_dir, 'paragraph'),
        parse_doc(expected_common_dir, 'paragraph'),
    )


def test_indentation(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['indentation'])

    assert_doc_equal(
        parse_doc(out_dir, 'indentation'),
        parse_doc(expected_common_dir, 'indentation'),
    )


def test_literal_block(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['literal-block'])

    assert_doc_equal(
        parse_doc(out_dir, 'literal-block'),
        parse_doc(expected_common_dir, 'literal-block'),
    )

# TODO: add tests of indendation and bullet lists with different line lengths
