from django.shortcuts import render, get_object_or_404
from .models import Blogpost


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    blogpost = Blogpost.objects.order_by('-pub_date')
    return render(request, 'blog/blog.html', {'blogpost': blogpost})

def post(request, blog_id):
    blogpost = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'blog/post.html', {'blogpost': blogpost})