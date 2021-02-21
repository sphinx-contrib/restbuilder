from tests.utils import run_parse_test


def test_hyperlink_targets(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['hyperlink-targets'])


def test_external_hyperlinks(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['external-hyperlinks'])


def test_internal_hyperlinks(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['internal-hyperlinks'])


def test_ref(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-roles', ['ref'])


def test_cross_ref(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-roles/ref', ['index', 'doc1'])


def test_doc_role(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-roles/doc', ['index', 'doc1', 'doc2'])
