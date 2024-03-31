from django.urls import path
from mainapp.views import about, index

app_name = "mainapp"


urlpatterns = [
    path('', index, name='main'),
    path("about", about, name='about'),
]
