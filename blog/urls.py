
from django.urls import path
from . import views
#from .views import PostListView


urlpatterns = [
	path('', views.home, name='blog-home'),
	path('about/', views.about, name='blog-about'),
	path('books/', views.books, name='blog-books')
]