#!/usr/bin/env python
import os

# More examples: https://github.com/pydanny/cookiecutter-django/blob/master/hooks/post_gen_project.py
# and: https://github.com/pytest-dev/cookiecutter-pytest-plugin/blob/master/hooks/post_gen_project.py

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    remove_file('include.jinja')

