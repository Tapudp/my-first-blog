from django.shortcuts import render
from django.utils import timezone
from .models import Post # dot in the begining means the current directory.

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lakh/post_list.html', {'posts':posts})
