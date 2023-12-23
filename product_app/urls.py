from django.urls import path 
from .views import *





urlpatterns = [
    path('', products, name='products'),
    path('air-compressor/', air_Compressor, name='aircompressor'),
    path('water-investement/', water_Investement, name='waterinvestement'),
    path('jet-ink/', jet_Ink, name='jetink'),
    path('steel-stanless/', steel_Stanless, name='steelstanless'),
    #path('<int:id>/', product_detail, name='product-detail')
]
