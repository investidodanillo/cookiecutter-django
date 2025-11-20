import sys, re
slug = '{{ cookiecutter.app_slug }}'
if not re.match(r'^[a-z0-9_]+$', slug):
    print('ERROR: app_slug must be snake_case (lowercase, numbers and underscores only).')
    sys.exit(1)
