from django.apps import AppConfig

class {{ cookiecutter.app_slug|replace("_", "")|title }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "{{ cookiecutter.app_slug }}"
