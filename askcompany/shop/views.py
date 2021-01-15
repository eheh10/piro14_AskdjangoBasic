from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import quote
import os

# Create your views here.
def year_archive(request, year):
    return HttpResponse('{}에 대한 내용'.format(year))

def response_excel(request):
    filepath = 'C:\\Users\\enhh\\Desktop\\excel_test.xlsx'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')

        encoded_filename = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)

        return response