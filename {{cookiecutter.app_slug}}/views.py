{% if cookiecutter.use_cbv == "yes" %}
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import {{ cookiecutter.app_slug|replace("_", "")|title }}Model

class {{ cookiecutter.app_slug }}_list_view(ListView):
    model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model

class {{ cookiecutter.app_slug }}_create_view(CreateView):
    model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model
    fields = '__all__'

class {{ cookiecutter.app_slug }}_update_view(UpdateView):
    model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model
    fields = '__all__'

class {{ cookiecutter.app_slug }}_detail_view(DetailView):
    model = {{ cookiecutter.app_slug|replace("_", "")|title }}Model
{% else %}
from django.shortcuts import render

def {{ cookiecutter.app_slug }}_list_view(request):
    return render(request, "{{ cookiecutter.app_slug }}/list.html")
{% endif %}
