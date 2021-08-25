from django.urls import path, include
from . import views
app_name = 'shop'   # 重点是这一行
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    #  path(r'search/$', views.search, name='search')
    
]