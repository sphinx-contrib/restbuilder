from tests.utils import run_parse_test


def test_toctree(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'sphinx-directives/toctree', ['index', 'doc1', 'doc2'])
