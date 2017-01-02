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
import os
import connexion
import datetime
import logging

import config as CONFIG

logger = logging.getLogger(__name__)

# Create Connexion app
app = connexion.App(__name__)

# Trick: app.app is the Flask app object
flask_app = app.app
flask_app.logger_name = "{{ cookiecutter.project_slug }}"

# Add api blueprints
app.add_api(
    'swagger/pets.yaml', base_path='/v1.0/pets'
)


