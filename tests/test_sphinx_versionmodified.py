from tests.utils import run_parse_test


def test_versionadded(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives', ['code-block'])


def test_versionchanged(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives', ['versionchanged'])


def test_deprecated(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives', ['deprecated'])
