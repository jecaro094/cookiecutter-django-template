from django.urls import path
from . import views

app_name = '{{ cookiecutter.project_slug }}'
urlpatterns = [
    path(
        'test/',
        views.TestViewSet.as_view(
            {
                'get': 'hello_world'
            }
        ),
        name='hello_world'
    ),
]