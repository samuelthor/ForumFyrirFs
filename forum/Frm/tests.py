import datetime
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from .models import Post

def create_post(post_text, days):
    """
    Creates a post with the given `post_text` published the given
    number of `days` offset to now (negative for posts published
    in the past, positive for posts that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return post.objects.create(post_text=post_text,
                                   pub_date=time)


class postViewTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no posts exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('Frm:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Frm are available.")
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_index_view_with_a_past_post(self):
        """
        posts with a pub_date in the past should be displayed on the
        index page.
        """
        create_post(post_text="Past post.", days=-30)
        response = self.client.get(reverse('Frm:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<post: Past post.>']
        )

    def test_index_view_with_a_future_post(self):
        """
        posts with a pub_date in the future should not be displayed on
        the index page.
        """
        create_post(post_text="Future post.", days=30)
        response = self.client.get(reverse('Frm:index'))
        self.assertContains(response, "No Frm are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_index_view_with_future_post_and_past_post(self):
        """
        Even if both past and future posts exist, only past posts
        should be displayed.
        """
        create_post(post_text="Past post.", days=-30)
        create_post(post_text="Future post.", days=30)
        response = self.client.get(reverse('Frm:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<post: Past post.>']
        )

    def test_index_view_with_two_past_posts(self):
        """
        The posts index page may display multiple posts.
        """
        create_post(post_text="Past post 1.", days=-30)
        create_post(post_text="Past post 2.", days=-5)
        response = self.client.get(reverse('Frm:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<post: Past post 2.>', '<post: Past post 1.>']
        )

class PostMethodTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() should return False for posts whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertEqual(future_post.was_published_recently(), False)
    def test_was_published_recently_with_old_post(self):
        """
        was_published_recently() should return False for posts whose
        pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_post = post(pub_date=time)
        self.assertEqual(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
        was_published_recently() should return True for posts whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_post = post(pub_date=time)
        self.assertEqual(recent_post.was_published_recently(), True)
