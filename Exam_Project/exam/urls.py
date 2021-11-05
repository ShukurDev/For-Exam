
from django.urls import path


# from views import ResultListView

from . import views

urlpatterns = [
    path('console/',views.console,name = 'console'),

    path('list/',views.Productapi,name='list'),
    path('createproductapi/',views.createproduct,name='createapi'),
    path('createproductitem/',views.createproduct,name='createproductitem'),
    path('createdeliver/',views.createproduct,name='createdeliver'),
    path('createcategory/',views.createproduct,name='createcategory'),
    path('result/',views.ResultListView.as_view(),name='result'),

    path('nesting/<str:pk>/', views.productitemlist,name='productitemlist'),
    

]
