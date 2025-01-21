from django.shortcuts import render
from django.views.generic import ListView
from newspaper.models import Post


class HomePageView(ListView):  # Fixed `List View` to `ListView`
    model = Post
    template_name = 'aznews/home.html'
    context_object_name = "posts"
    queryset = Post.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-published_at")[:5]
