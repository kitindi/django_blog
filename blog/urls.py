from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
	path('', views.home, name='home'),
	path('article/<slug:slug>/', views.article, name='article_details'),

]
