from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

app_name = 'shop'

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/<yyyy:year>', views.year_archive),
    path('excel/', views.response_excel),
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),
]
