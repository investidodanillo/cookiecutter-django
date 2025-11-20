from django.contrib import admin
from .models import {{ cookiecutter.app_slug|replace("_", "")|title }}Model

@admin.register({{ cookiecutter.app_slug|replace("_", "")|title }}Model)
class {{ cookiecutter.app_slug|replace("_", "")|title }}ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'criado_em')
