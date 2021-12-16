from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def detail_view(request):
    return render(request, 'detail.html')


def page_view(request):
    return render(request, 'page.html')


def post_view(request):
    return render(request, 'post.html')
