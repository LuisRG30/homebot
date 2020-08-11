from django.core.management.base import BaseCommand
from homeworkcrafter.models import Delivery

class Command(BaseCommand):
    def handle(self, *args, **options):
        documents = Delivery.objects.filter(erase=True)
        for doc in documents:
            doc.delete()