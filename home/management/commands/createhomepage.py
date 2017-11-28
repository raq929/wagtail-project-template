from home.models import HomePage

from wagtail.wagtailcore.models import Page, Site
from django.contrib.sites.models import Site as DjangoSite

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.core import management



class Command(BaseCommand):
    help = 'Creates homepage, Wagtail Site, and modifies Django Site name.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete homepage and child pages before creating new homepage and site.',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options['delete']:
            Page.objects.filter(slug='home').delete()

        try:
            HomePage.objects.get(slug='home')
        except ObjectDoesNotExist:
            Page.objects.filter(slug='home').delete()
            home_page = HomePage(title='Home', slug='home')

            root_page = Page.objects.get(title='Root')
            root_page.add_child(instance=home_page)

            Site.objects.create(
                site_name='project_name (Dev)',
                hostname='localhost',
                port='8000',
                root_page=home_page,
                is_default_site=True
            )

            # Certain apps (allauth, for example) use the django rather than
            # Wagtail site name and are not overridable.
            django_site = DjangoSite.objects.first()
            django_site.domain = 'www.project_name.com'
            django_site.name = 'project_name'
            django_site.save()
