from django.urls import path
from . import views

app_name = "{{ cookiecutter.app_slug }}"

urlpatterns = [
    path('', views.{{ cookiecutter.app_slug }}_list_view, name='{{ cookiecutter.app_slug }}_list'),
    path('criar/', views.{{ cookiecutter.app_slug }}_create_view, name='{{ cookiecutter.app_slug }}_create'),
    path('editar/<int:pk>/', views.{{ cookiecutter.app_slug }}_update_view, name='{{ cookiecutter.app_slug }}_update'),
]
