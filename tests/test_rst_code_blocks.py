from tests.utils import build_sphinx, assert_doc_equal, parse_doc


def test_code_block(sphinx_directives_src_dir, expected_sphinx_directives_dir, output_dir):
    build_sphinx(sphinx_directives_src_dir, output_dir, ['code-block'])

    assert_doc_equal(
        parse_doc(output_dir, 'code-block'),
        parse_doc(expected_sphinx_directives_dir, 'code-block'),
    )


def test_code_block_language(sphinx_directives_src_dir, expected_sphinx_directives_dir, output_dir):
    build_sphinx(sphinx_directives_src_dir, output_dir, ['code-block-language'])

    assert_doc_equal(
        parse_doc(output_dir, 'code-block-language'),
        parse_doc(expected_sphinx_directives_dir, 'code-block-language'),
    )


def test_code_block_linenos(sphinx_directives_src_dir, expected_sphinx_directives_dir, output_dir):
    build_sphinx(sphinx_directives_src_dir, output_dir, ['code-block-linenos'])

    assert_doc_equal(
        parse_doc(output_dir, 'code-block-linenos'),
        parse_doc(expected_sphinx_directives_dir, 'code-block-linenos'),
    )


def test_code(directives_src_dir, expected_directives_dir, output_dir):
    build_sphinx(directives_src_dir, output_dir, ['code'])

    assert_doc_equal(
        parse_doc(output_dir, 'code'),
        parse_doc(expected_directives_dir, 'code'),
    )


def test_code_language(directives_src_dir, expected_directives_dir, output_dir):
    build_sphinx(directives_src_dir, output_dir, ['code-language'])

    assert_doc_equal(
        parse_doc(output_dir, 'code-language'),
        parse_doc(expected_directives_dir, 'code-language'),
    )


def test_code_number_lines(directives_src_dir, expected_directives_dir, output_dir):
    build_sphinx(directives_src_dir, output_dir, ['code-number-lines'])

    assert_doc_equal(
        parse_doc(output_dir, 'code-number-lines'),
        parse_doc(expected_directives_dir, 'code-number-lines'),
    )
