from django import forms
from .models import {{ cookiecutter.app_slug|replace("_", "")|title }}Model

class {{ cookiecutter.app_slug|replace("_", "")|title }}Form(forms.ModelForm):
    class Meta:
        model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model
        fields = '__all__'
