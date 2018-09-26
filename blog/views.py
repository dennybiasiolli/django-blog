from django.shortcuts import render

# Create your views here.

# This is for the homepage 
def post_list(request):
    return render(request, 'blog/post_list.html', {})
