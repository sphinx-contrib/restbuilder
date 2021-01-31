from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_bold(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['bold'])

    assert_doc_equal(
        parse_doc(out_dir, 'bold'),
        parse_doc(expected_common_dir, 'bold'),
    )


def test_italic(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['italic'])

    assert_doc_equal(
        parse_doc(out_dir, 'italic'),
        parse_doc(expected_common_dir, 'italic'),
    )


def test_literal(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['literal'])

    assert_doc_equal(
        parse_doc(out_dir, 'literal'),
        parse_doc(expected_common_dir, 'literal'),
    )


def test_subscript(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['subscript'])

    assert_doc_equal(
        parse_doc(out_dir, 'subscript'),
        parse_doc(expected_common_dir, 'subscript'),
    )


def test_superscript(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['superscript'])

    assert_doc_equal(
        parse_doc(out_dir, 'superscript'),
        parse_doc(expected_common_dir, 'superscript'),
    )
