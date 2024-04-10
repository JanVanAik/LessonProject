from django.urls import path
from mainapp.views import about, index, orders, image

app_name = "mainapp"


urlpatterns = [
    path('', index, name='main'),
    path('about/', about, name='about'),
    path('orders/', orders, name='orders'),
    path('image/', image, name='image'),
]
