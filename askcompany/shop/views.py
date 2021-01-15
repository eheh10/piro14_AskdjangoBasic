from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import quote
import os
from .models import Item

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
    
def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {
        'item_list':qs,
        'q':q,
    }

    )