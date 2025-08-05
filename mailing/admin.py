from django.contrib import admin

from mailing.models import Message, Sending, MailingList,Recipient

# Register your models here.
admin.site.register(Message)
admin.site.register(Sending)
admin.site.register(MailingList)
admin.site.register(Recipient)