from tests.utils import run_parse_test


def test_ordered_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['ordered-list'])


def test_bullet_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['bullet-list'])


def test_nested_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['nested-list'])
