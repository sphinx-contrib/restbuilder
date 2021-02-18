from tests.utils import run_parse_test

import sphinx


def test_bold(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['bold'])


def test_italic(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['italic'])


def test_literal(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['literal'])


def test_subscript(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['subscript'])


def test_superscript(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['superscript'])


def test_smart_quotes(src_dir, expected_dir, output_dir):
    # Smart quotes were only introduces in Sphinx 1.6
    if sphinx.version_info >= (1, 6):
        run_parse_test(src_dir, expected_dir, output_dir, 'common', ['smart-quotes'])
    else:
        # Support for Sphinx < 1.6
        # no modification, test against src_dir instead of expected_dir
        run_parse_test(src_dir, src_dir, output_dir, 'common', ['smart-quotes'])

