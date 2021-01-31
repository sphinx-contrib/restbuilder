import os

import pytest


@pytest.fixture
def common_src_dir():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'datasets', 'common'
    )


@pytest.fixture
def expected_common_dir():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'expected', 'common'
    )
