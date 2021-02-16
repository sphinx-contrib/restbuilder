from os.path import dirname, realpath, join
import shutil

import pytest


@pytest.fixture
def common_src_dir():
    return join(
        dirname(realpath(__file__)), 'datasets', 'common'
    )

@pytest.fixture
def expected_common_dir():
    return join(
        dirname(realpath(__file__)), 'expected', 'common'
    )

@pytest.fixture
def directives_src_dir():
    return join(
        dirname(realpath(__file__)), 'datasets', 'directives'
    )

@pytest.fixture
def expected_directives_dir():
    return join(
        dirname(realpath(__file__)), 'expected', 'directives'
    )

@pytest.fixture
def roles_src_dir():
    return join(
        dirname(realpath(__file__)), 'datasets', 'roles'
    )

@pytest.fixture
def expected_roles_dir():
    return join(
        dirname(realpath(__file__)), 'expected', 'roles'
    )

@pytest.fixture
def sphinx_directives_src_dir():
    return join(
        dirname(realpath(__file__)), 'datasets', 'sphinx-directives'
    )

@pytest.fixture
def expected_sphinx_directives_dir():
    return join(
        dirname(realpath(__file__)), 'expected', 'sphinx-directives'
    )

@pytest.fixture
def sphinx_roles_src_dir():
    return join(
        dirname(realpath(__file__)), 'datasets', 'sphinx-roles'
    )

@pytest.fixture
def expected_sphinx_roles_dir():
    return join(
        dirname(realpath(__file__)), 'expected', 'sphinx-roles'
    )

@pytest.fixture(scope="session")
def output_dir():
    out_dir = realpath(join(dirname(realpath(__file__)), '..', 'output'))
    shutil.rmtree(out_dir, ignore_errors=True)
    return out_dir
