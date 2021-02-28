from tests.utils import run_parse_test

import pytest


def test_bullet_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['bullet-list'])


def test_ordered_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['ordered-list'])


def test_nested_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['nested-list'])


def test_multiline_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['multiline-list'])


@pytest.mark.skip(reason="work in progress")
def test_ordered_list_properties(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['ordered-list-properties'])


@pytest.mark.skip(reason="work in progress")
def test_bullet_list_consecutive(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['bullet-list-consecutive'])


def test_definition_list(src_dir, expected_dir, output_dir):
    run_parse_test(src_dir, expected_dir, output_dir, 'common', ['definition-list'])
