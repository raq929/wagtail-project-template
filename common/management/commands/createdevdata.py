from wagtail.core.models import Page

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.core import management


class Command(BaseCommand):
    help = 'Creates data appropriate for development'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete homepage and child pages before creating new data.',
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options['delete']:
            # Deletes home page and all of it's children.
            # Settings and snippets (including menus) need to be deleted seperately.
            Page.objects.filter(slug='home').delete()

        management.call_command('createhomepage')
        management.call_command('createblogdata', '10')

        # Create superuser
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                'test',
                'test@project_name.com',
                'test',
            )
            self.stdout.write(
                'Superuser created:\n'
                '\tname: test\n'
                '\temail: test@project_name.com\n'
                '\tpassword: test'
            )
