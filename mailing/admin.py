from django.contrib import admin

from mailing.models import Message, Mailing, Result,Recipient

# Register your models here.
admin.site.register(Message)
admin.site.register(Mailing)
admin.site.register(Result)
admin.site.register(Recipient)