from django.urls import path
import engine.views as views

urlpatterns = [
    path('a', views.index, name='index'),
]
