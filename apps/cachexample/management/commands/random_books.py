

from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify

from cachexample.models import *
import populate
import random
import string

class Command(BaseCommand):
    args = ''
    help = 'generate random author/books'

    def handle(self, *args, **options):
        how_many = 30
        if len(args) > 0:
            how_many = int(args[0])

        all_authors = Author.objects.all()
        all_categories = Category.objects.all()

        for i in range(0,how_many):
            name = string.capwords(' '.join([populate.random_noun(), populate.random_adj_noun()]))
            slug = slugify(name)
            book = Book(slug=slug,
                name = name,
                author = random.sample(all_authors, 1)[0],
                is_active = True,
                category = random.sample(all_categories, 1)[0],
            )
            print book
