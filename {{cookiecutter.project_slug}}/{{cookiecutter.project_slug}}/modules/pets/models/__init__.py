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
from __about__ import *

__all__ = ('PETS_DB', 'PetsModel')

from .tinydb_json import PETS_DB, PetsModel


