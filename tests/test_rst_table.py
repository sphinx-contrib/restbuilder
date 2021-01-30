from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_simple_table(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['simple-table'])

    assert_doc_equal(
        parse_doc(out_dir, 'simple-table'),
        parse_doc(expected_common_dir, 'simple-table'),
    )


def test_grid_table(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['grid-table'])

    assert_doc_equal(
        parse_doc(out_dir, 'grid-table'),
        parse_doc(expected_common_dir, 'grid-table'),
    )


def test_list_table(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['list-table'])

    assert_doc_equal(
        parse_doc(out_dir, 'list-table'),
        parse_doc(expected_common_dir, 'list-table'),
    )
