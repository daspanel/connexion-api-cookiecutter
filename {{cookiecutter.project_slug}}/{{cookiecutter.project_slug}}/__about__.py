#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""{{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

 :copyright: (c) {{ cookiecutter.year }}, {{ cookiecutter.full_name }}.
             All rights reserved.
 :license:   {{ cookiecutter.open_source_license}}, see LICENSE for more details.
"""
{% import 'include.jinja' as myctx with context %}
from __future__ import absolute_import, division, print_function
import re
from collections import namedtuple

version_info_t = namedtuple('version_info_t', (
    'major', 'minor', 'micro', 'releaselevel', 'serial',
))

__all__ = (
    '__title__',
    '__summary__',
    '__description__',
    '__author__',
    '__author_email__',
    '__email__',
    '__maintainer__',
    '__version_info__',
    '__version__',
    '__keywords__',
    '__license__',
    '__copyright__',
    '__url__',
    '__uri__',
    '__notifier__',
    '__status__',
    '__credits__',
    '__contact__',
    '__homepage__',
    '__docformat__',
    '__banner__',
    'VERSION',
    'version_info'
)

__title__ = '{{ cookiecutter.project_name }}'
__summary__ = '{{ cookiecutter.project_short_description }}'
__description__ = __summary__
__author__ = '{{ cookiecutter.full_name }}'
__author_email__ = '{{ cookiecutter.email }}'
__email__ = __author_email__
__maintainer__ = __author__
__version__ = '{{ cookiecutter.version }}'

_temp = re.match(
    r'(\d+)\.(\d+).(\d+)(.+)?', __version__).groups()
VERSION = version_info = __version_info__ = version_info_t(
    int(_temp[0]), int(_temp[1]), int(_temp[2]), _temp[3] or '', '')

del(_temp)
del(re)

#__version_info__ = ('0', '0', '1')

__keywords__ = ['daspanel', 'docker']
__license__ = '{{ cookiecutter.open_source_license}}'
__copyright__ = (
    "(c) {{ cookiecutter.year }}, {0}. All rights reserved.".format(__author__)
)
__url__ = '{{ cookiecutter.author_site }}'
__uri__ = '{{ myctx.repo_url }}'
__notifier__ = {
    'name': 'daspanel-uuid',
    'version': __version__,
    'url': __url__,
}
__status__ = "Development"
__credits__ = []
__contact__ = '{{ cookiecutter.email }}'
__homepage__ = '{{ cookiecutter.author_site }}'
__docformat__ = 'restructuredtext'
# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t=Daspanel API
__banner__ = r"""
╔╦╗┌─┐┌─┐┌─┐┌─┐┌┐┌┌─┐┬    ╔═╗╔═╗╦
 ║║├─┤└─┐├─┘├─┤│││├┤ │    ╠═╣╠═╝║
═╩╝┴ ┴└─┘┴  ┴ ┴┘└┘└─┘┴─┘  ╩ ╩╩  ╩  by Abner G Jacobsen
"""
# -eof meta-
