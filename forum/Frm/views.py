from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Comment, Post
from django.utils import timezone
from .tests import TestCase
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'Frm/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """
        Return the last five published posts (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'Frm/detail.html'
    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Post.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Post
    template_name = 'Frm/results.html'

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'frm/index.html', context)

def register(request):
    user_name = request.GET['username']
    emailReg = request.GET['email']
    password = request.GET['password']
    u = User.objects.create_user(user_name, emailReg, password)
    u.save()
    return HttpResponseRedirect("http://localhost/angular/#/Login")

def login(request):
    user_name = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=user_name, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'frm/detail.html', {'post': post})

def results(request, post_id):
    post = get_object_or_404(post, pk=post_id)
    return render(request, 'Frm/results.html', {'post': post})

def vote(request, post_id):
    p = get_object_or_404(post, pk=post_id)
    try:
        selected_comment = p.comment_set.get(pk=request.POST['comment'])
    except (KeyError, comment.DoesNotExist):
        # Redisplay the post voting form.
        return render(request, 'Frm/detail.html', {
            'post': p,
            'error_message': "You didn't select a comment.",
        })
    else:
        selected_comment.votes += 1
        selected_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('Frm:results', args=(p.id,)))

class PostIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_post(self):
        """
        The detail view of a post with a pub_date in the future should
        return a 404 not found.
        """
        future_post = create_post(post_text='Future post.',
                                          days=5)
        response = self.client.get(reverse('Frm:detail',
                                   args=(future_post.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_post(self):
        """
        The detail view of a post with a pub_date in the past should
        display the post's text.
        """
        past_post = create_post(post_text='Past Post.',
                                        days=-5)
        response = self.client.get(reverse('Frm:detail',
                                   args=(past_post.id,)))
        self.assertContains(response, past_post.post_text,
                            status_code=200)
