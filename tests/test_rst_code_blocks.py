from tests.utils import run_parse_test


def test_code_block(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives', ['code-block'])


def test_code_block_language(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives', ['code-block-language'])


def test_code_block_linenos(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives', ['code-block-linenos'])


def test_code(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'directives', ['code'])


def test_code_language(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'directives', ['code-language'])


def test_code_number_lines(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'directives', ['code-number-lines'])
