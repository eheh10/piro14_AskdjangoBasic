from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def year_archive(request, year):
    return HttpResponse('{}에 대한 내용'.format(year))