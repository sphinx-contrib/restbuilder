# -*- coding: utf-8 -*-
"""
    sphinxcontrib.restbuilder
    =========================

    Sphinx extension to output reST files.

    .. moduleauthor:: Freek Dijkstra <freek@macfreek.nl>

    :copyright: Copyright 2012-2021 by Freek Dijkstra and contributors.
    :license: BSD, see LICENSE.txt for details.
"""

from __future__ import (print_function, unicode_literals, absolute_import)

__version__ = '0.3.0'
__author__ = 'Freek Dijkstra <freek@macfreek.nl> and contributors'

def setup(app):
    # imports defined inside setup function, so that the __version__ can be loaded,
    # even if Sphinx is not yet installed.
    from sphinx.writers.text import STDINDENT
    from .builders.rst import RstBuilder  # loads RstWriter as well.

    app.require_sphinx('1.4')
    app.add_builder(RstBuilder)
    app.add_config_value('rst_file_suffix', ".rst", False)
    """This is the file name suffix for reST files"""
    app.add_config_value('rst_link_suffix', None, False)
    """The is the suffix used in internal links. By default, takes the same value as rst_file_suffix"""
    app.add_config_value('rst_file_transform', None, False)
    """Function to translate a docname to a filename. By default, returns docname + rst_file_suffix."""
    app.add_config_value('rst_link_transform', None, False)
    """Function to translate a docname to a (partial) URI. By default, returns docname + rst_link_suffix."""
    app.add_config_value('rst_indent', STDINDENT, False)

    return {
        'version': __version__,
        # 'env_version': 1,  # not needed; restbuilder does not store data in the environment
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
