from django.core.mail import send_mail

from config import settings
from mailing.models import Sending, Result


class SendingService:
    @staticmethod
    def run_service(pk, user):
        sending = Sending.objects.get(pk=pk, owner=user)
        status = ''
        response = ''
        if sending:
            subject = sending.message.subject
            message = sending.message.body
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = list(map(lambda x: x.email, sending.recipients.all()))

            try:
                status = 'ok'
                response = send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                status = 'error'
                print(e)
                response = e
            Result.objects.create(status=status, response=response, sending=sending)

        else:
            status = 'error'
        return status
