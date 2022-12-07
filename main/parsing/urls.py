from django.urls import path
from . import views

app_name = 'parse'

urlpatterns = [
    path('', views.ParserFormView.as_view(), name='parse_func'),
    path('info/', views.ParserView.as_view(), name='parse_view'),
]