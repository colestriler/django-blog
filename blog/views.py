from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post, BookReview

def home(request):
	posts = Post.objects.all()
	distinct_years = set()

	for post in posts:
		distinct_years.add(post.date.year)
	
	context = {
		'posts': posts.order_by('-date'),
		'years': sorted(distinct_years, reverse=True)
	}
	return render(request, 'blog/home.html', context)


def books(request):
	books = BookReview.objects.all()
	distinct_years = set()
	for book in books:
		distinct_years.add(book.date.year)
	
	context = {
		'books': books.order_by('-date'),
		'years': sorted(distinct_years, reverse=True)
	}
	return render(request, 'blog/books.html', context)

# class PostListView(ListView):
# 	model = Post
# 	template = 'blog/home.html'
# 	context_object_name = 'posts'
	
def about(request):
	
	return render(request, 'blog/about.html')
	