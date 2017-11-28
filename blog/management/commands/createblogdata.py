from blog.models import BlogIndexPage
from blog.tests.factories import BlogPageFactory, BlogIndexPageFactory
from home.models import HomePage

from django.core.management.base import BaseCommand
from django.db import transaction
from django.core import management


class Command(BaseCommand):
    help = 'Creates blog data appropriate for development.'

    def add_arguments(self, parser):
        parser.add_argument('number_of_posts', type=int)

    @transaction.atomic
    def handle(self, *args, **options):
        number_of_posts = options['number_of_posts']

        try:
            home_page = HomePage.objects.get(slug='home')
        except HomePage.DoesNotExist:
            management.call_command('createhomepage')
            home_page = HomePage.objects.get(slug='home')

        if BlogIndexPage.objects.all():
            blog_index_page = BlogIndexPage.objects.first()
        else:
            blog_index_page = BlogIndexPageFactory(parent=home_page)

        for x in range(number_of_posts):
            BlogPageFactory(parent=blog_index_page)
