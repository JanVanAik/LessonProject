from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page Accesed')
    return HttpResponse('<h4> Основная страница</h4>')

def about(request):
    logger.info(request) # данные о странице
    return HttpResponse('<h4> Информация обо мне</h4>')
