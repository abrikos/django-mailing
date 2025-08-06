from datetime import datetime

from django.core.mail import send_mail

from config import settings
from mailing.models import Mailing, Result


class MailingService:
    @staticmethod
    def send(subject, message, email):
        from_email = settings.DEFAULT_FROM_EMAIL
        try:
            status = "ok"
            response = send_mail(subject, message, from_email, [email])
        except Exception as e:
            status = "error"
            print(e)
            response = e
        return status, response

    @staticmethod
    def run_service(pk, user):
        mailing = Mailing.objects.get(pk=pk, owner=user)
        print("zzzzzzz", mailing)
        status = ""
        response = ""
        if mailing:
            subject = mailing.message.subject
            message = mailing.message.body
            for recipient in mailing.recipients.all():
                status, response = MailingService.send(subject, message, recipient.email)
                Result.objects.create(
                    status=status,
                    response=response,
                    mailing=mailing,
                    email=recipient.email,
                )
        else:
            status = "error"
        return status

    @staticmethod
    def run_all():
        mailings = Mailing.objects.filter(status="Running", start__lt=datetime.now(), end__gt=datetime.now())
        for mailing in mailings:
            status = MailingService.run_service(mailing.id, mailing.owner)
            print(status)
