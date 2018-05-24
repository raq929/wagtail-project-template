from datetime import datetime
import pytz
from django.test import TestCase

from blog.models import BlogPage
from blog.tests.factories import BlogPageFactory, BlogIndexPageFactory


class BlogIndexPageTest(TestCase):
    def setUp(self):
        self.blog_index = BlogIndexPageFactory()
        self.live_post = BlogPageFactory(
            live=True,
            parent=self.blog_index,
            publication_datetime=datetime(2017, 1, 1, tzinfo=pytz.UTC)
        )
        self.unpublished_post = BlogPageFactory(live=False, parent=self.blog_index)

    def tearDown(self):
        BlogPage.objects.all().delete()

    def test_get_posts_should_return_live_posts(self):
        posts = self.blog_index.get_posts()
        self.assertIn(self.live_post, posts)

    def test_get_posts_should_not_return_unpublished_posts(self):
        posts = self.blog_index.get_posts()
        self.assertNotIn(self.unpublished_post, posts)

    def test_get_posts_returns_newest_post_first(self):
        BlogPageFactory(publication_datetime=datetime(2018, 1, 1, tzinfo=pytz.UTC), parent=self.blog_index)
        first = BlogPageFactory(publication_datetime=datetime(2018, 3, 31, tzinfo=pytz.UTC), parent=self.blog_index)
        BlogPageFactory(publication_datetime=datetime(2017, 3, 1, tzinfo=pytz.UTC), parent=self.blog_index)
        posts = self.blog_index.get_posts()
        self.assertEqual(first, posts.first())

    def test_get_posts_returns_oldest_post_last(self):
        BlogPageFactory(publication_datetime=datetime(2018, 1, 1, tzinfo=pytz.UTC), parent=self.blog_index)
        BlogPageFactory(publication_datetime=datetime(2018, 3, 31, tzinfo=pytz.UTC), parent=self.blog_index)
        last = BlogPageFactory(publication_datetime=datetime(2015, 3, 31, tzinfo=pytz.UTC), parent=self.blog_index)
        BlogPageFactory(publication_datetime=datetime(2018, 3, 1, tzinfo=pytz.UTC), parent=self.blog_index)
        posts = self.blog_index.get_posts()
        self.assertEqual(last, posts.last())
