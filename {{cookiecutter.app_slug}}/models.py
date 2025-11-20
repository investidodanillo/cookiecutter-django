from django.db import models

class {{ cookiecutter.app_slug|replace("_", "")|title }}Model(models.Model):
    titulo = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "{{ cookiecutter.app_title }}"
        verbose_name_plural = "{{ cookiecutter.app_title }}"

    def __str__(self):
        return self.titulo
