from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing listings (optional)
        Listing.objects.all().delete()

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.paragraph(nb_sentences=5),
                location=fake.city(),
                price_per_night=round(random.uniform(50, 500), 2)
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings.'))
