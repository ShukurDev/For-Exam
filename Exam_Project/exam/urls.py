
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
# router = DefaultRouter()
# # from views import ResultListView
# router.register('orders',views.ProductResultAPI,basename='orders')
# router.register('category',views.ProductAPI,basename='category')
# router.register('deliver',views.DeliveredAPI,basename='deliver')


urlpatterns = [

    path('ProductAPI',views.ProductAPI,name='ProductAPI'),

    path('createproductapi/',views.CreateProductAPI,name='createproductapi'),
    path('createdeliverapi/',views.CreateDeliverAPI,name='createdeliverapi'),
    path('createcategoryapi/',views.CreateCategoryAPI,name='createcategoryapi'),
    path('createorderapi/',views.CreateOrderAPI,name='createorderapi'),

    path('productresultapi/',views.ProductResultAPI,name='productresultapi'),

    path('manyincomeapi/',views.ManyIncomeAPI,name='manyincomeapi'),
    # path('nesting/<str:pk>/', views.productitemlist,name='productitemlist'),


]
