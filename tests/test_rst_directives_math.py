from tests.utils import run_parse_test


def test_directive_math(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'directives', ['math'])
