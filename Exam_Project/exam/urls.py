
from django.urls import path


# from views import ResultListView

from . import views

urlpatterns = [

    path('ProductAPI',views.ProductAPI,name='ProductAPI'),

    path('createproductapi/',views.CreateProductAPI,name='createproductapi'),
    path('createdeliverapi/',views.CreateDeliverAPI,name='createdeliverapi'),
    path('createcategoryapi/',views.CreateCategoryAPI,name='createcategoryapi'),
    path('createorderapi/',views.CreateOrderAPI,name='createorderapi'),


    path('result/',views.ResultListView.as_view(),name='result'),

    # path('nesting/<str:pk>/', views.productitemlist,name='productitemlist'),
    

]
