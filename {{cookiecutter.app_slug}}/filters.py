{% if cookiecutter.use_filters == "yes" -%}
import django_filters
from .models import {{ cookiecutter.app_slug|replace("_", "")|title }}Model

class {{ cookiecutter.app_slug|replace("_", "")|title }}Filter(django_filters.FilterSet):
    class Meta:
        model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model
        fields = ['titulo',]
{%- endif %}
