from django.shortcuts import render
from django.utils import timezone
from .models import Post # dot in the begining means the current directory.
from django.shortcuts import render, get_object_or_404

# Create your views here.
#Post.objects.get(pk=pk)  
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lakh/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lakh/post_detail.html', {'post':post})