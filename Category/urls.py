from django.urls import path
from . import views

app_name = 'Category'

urlpatterns = [
    path('', views.MainList.as_view(), name='sex_toys'),
    path('<slug:slugname>/', views.CategoryList.as_view(), name='sex_toys_slug'),
]