from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify

from cachexample.models import *
import populate


class Command(BaseCommand):
    args = ''
    help = 'generate random authors'

    def handle(self, *args, **options):
        how_many = 30
        if len(args) > 0:
            how_many = int(args[0])

        for i in range(0,how_many):
            author, created = Author.objects.get_or_create(name=populate.random_name())
            if created:
                author.bio = populate.random_paragraphs()
                author.save()
            print author
