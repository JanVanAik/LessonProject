from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from mainapp.models import Order
from mainapp.forms import ProductForm
from django.utils.timezone import now, timedelta
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page Accesed')
    return HttpResponse('<h4> Основная страница</h4>')

def about(request):
    logger.info(request) # данные о странице
    return HttpResponse('<h4> Информация обо мне</h4>')

def image(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            print('Image succesfully changed')
            return HttpResponseRedirect(reverse("mainapp:image"))
    else:
        form = ProductForm()
    context = {
        'title': 'Image change page',
        'form': form,
    }
    return render(request, 'mainapp/image.html', context)

def orders(request):
    if request.method == 'POST':
        delta = {
            'year': 365,
            'month': 30,
            'week': 7,
        }
        choice = request.POST.get('choice')
        orders = Order.objects.filter(order_datetime__gt=now()-timedelta(days=delta[choice]))
        context = {
            'title': "ORDERS",
            'orders': orders
        }
    else:
        context = {
            'title': "ORDERS",
        }
    return render(request, 'mainapp/orders.html', context)
