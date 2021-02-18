from tests.utils import run_parse_test

import pytest
import sphinx

@pytest.mark.skipif(sphinx.version_info < (2, 0), reason="Sphinx 1.x does not support code blocks without language")
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


@pytest.mark.skipif(sphinx.version_info < (2, 0), reason="Sphinx 1.x renders line numbers inline.")
def test_code_number_lines(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'directives', ['code-number-lines'])
