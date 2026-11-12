"""The namespace must coexist with other portions without setuptools imports."""
import os
import subprocess
import sys

import pytest


@pytest.mark.parametrize('other_first', [False, True])
def test_namespace_without_pkg_resources(tmpdir, other_first):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    other = tmpdir.mkdir('other')
    portion = other.mkdir('sphinxcontrib')
    portion.join('_restbuilder_namespace_probe.py').write('MARKER = 42\n')
    paths = [root, str(other)]
    if other_first:
        paths.reverse()
    subprocess.check_call([
        sys.executable, '-S', '-c',
        'import sys; sys.path[:0] = sys.argv[1:]; '
        'import sphinxcontrib; '
        'import sphinxcontrib._restbuilder_namespace_probe as probe; '
        'assert probe.MARKER == 42; '
        'assert "pkg_resources" not in sys.modules',
    ] + paths)
