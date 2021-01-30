from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_ordered_list(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['ordered-list'])

    assert_doc_equal(
        parse_doc(out_dir, 'ordered-list'),
        parse_doc(expected_common_dir, 'ordered-list'),
    )


def test_bullet_list(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['bullet-list'])

    assert_doc_equal(
        parse_doc(out_dir, 'bullet-list'),
        parse_doc(expected_common_dir, 'bullet-list'),
    )


def test_nested_list(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['nested-list'])

    assert_doc_equal(
        parse_doc(out_dir, 'nested-list'),
        parse_doc(expected_common_dir, 'nested-list'),
    )
