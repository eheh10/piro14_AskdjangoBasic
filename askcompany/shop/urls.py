from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

app_name = 'shop'

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/<yyyy:year>', views.year_archive, name='archives_year'),
    path('excel/', views.response_excel),
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('new/', views.item_new, name='item_new'),
    path('<int:pk>/edit/', views.item_edit, name='item_edit'),
]
