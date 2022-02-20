from django.urls import path
from autodonate_bulma_theme import views


urlpatterns = [
    path('', views.index, name='index')
]
