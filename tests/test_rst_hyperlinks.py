from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_external_hyperlinks(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['external-hyperlinks'])

    assert_doc_equal(
        parse_doc(out_dir, 'external-hyperlinks'),
        parse_doc(expected_common_dir, 'external-hyperlinks'),
    )

def test_internal_hyperlinks(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['internal-hyperlinks'])

    assert_doc_equal(
        parse_doc(out_dir, 'internal-hyperlinks'),
        parse_doc(expected_common_dir, 'internal-hyperlinks'),
    )

def test_hyperlink_targets(common_src_dir, expected_common_dir):
    out_dir = build_sphinx(common_src_dir, ['hyperlink-targets'])

    assert_doc_equal(
        parse_doc(out_dir, 'hyperlink-targets'),
        parse_doc(expected_common_dir, 'hyperlink-targets'),
    )
