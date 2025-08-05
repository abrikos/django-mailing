from datetime import datetime

from django.utils import timezone

from django.core.mail import send_mail

from config import settings
from mailing.models import Sending, Result


class SendingService:
    @staticmethod
    def send(subject, message, email):
        from_email = settings.DEFAULT_FROM_EMAIL
        try:
            status = 'ok'
            response = send_mail(subject, message, from_email, [email])
        except Exception as e:
            status = 'error'
            print(e)
            response = e
        return status, response

    @staticmethod
    def run_service(pk, user):
        sending = Sending.objects.get(pk=pk, owner=user)
        status = ''
        response = ''
        if sending:
            subject = sending.message.subject
            message = sending.message.body
            for recipient in sending.recipients.all():
                status, response = SendingService.send(subject, message, recipient.email)
                Result.objects.create(status=status, response=response, sending=sending, email=recipient.email)
        else:
            status = 'error'
        return status

    @staticmethod
    def run_all():
        sendings = Sending.objects.filter(status='Running', start__lt=datetime.now(), end__gt=datetime.now())
        for sending in sendings:
            status = SendingService.run_service(sending.id, sending.owner)
            print(status)