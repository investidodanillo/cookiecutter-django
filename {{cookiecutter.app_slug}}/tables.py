{% if cookiecutter.use_tables == "yes" -%}
import django_tables2 as tables
from .models import {{ cookiecutter.app_slug|replace("_", "")|title }}Model

class {{ cookiecutter.app_slug|replace("_", "")|title }}Table(tables.Table):
    class Meta:
        model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model
        fields = ('titulo', 'criado_em')
{%- endif %}
