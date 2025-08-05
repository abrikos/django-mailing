from django.contrib import admin

from mailing.models import Message, Sending, Result,Recipient

# Register your models here.
admin.site.register(Message)
admin.site.register(Sending)
admin.site.register(Result)
admin.site.register(Recipient)