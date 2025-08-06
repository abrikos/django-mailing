# your_app/management/commands/my_script.py
from django.core.management.base import BaseCommand

from mailing.services import MailingService


class Command(BaseCommand):
    help = 'Runs all mailings.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting custom script...'))
        MailingService.run_all()
        self.stdout.write(self.style.SUCCESS('Custom script finished.'))