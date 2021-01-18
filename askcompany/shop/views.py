from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from urllib.parse import quote
import os
from .models import Item
from .forms import ItemForm
import re

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

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item' : item,  
    })

#def item_new(request, item=None):
#    if request.method == 'POST':
#        form = ItemForm(request.POST, request.FILES, instance=item)
#        if form.is_valid():
#            form.save()
#            redirect(item)
#    else:
#        form = ItemForm(instance=item)
#
#    return render(request, 'shop/item_form.html', {
#        'form':form,
#    })

#def item_edit(request, pk):
#    item = get_object_or_404(Item, pk=pk)
#    return item_new(request, item)
item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)
