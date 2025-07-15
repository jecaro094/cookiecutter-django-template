from django.urls import path
from . import views

app_name = 'qr_generator'
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