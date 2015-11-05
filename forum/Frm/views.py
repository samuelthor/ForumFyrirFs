from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'frm/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'frm/detail.html', {'post': post})

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)

def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)
