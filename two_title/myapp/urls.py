from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]
