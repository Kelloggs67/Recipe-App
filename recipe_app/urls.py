from django.urls import path
from recipe_app import views

app_name = 'recipe_app'

urlpatterns = [
    path('', views.create, name='create'),
]