from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm

from mailing.models import Sending, Message, Recipient


class SendingForm(ModelForm):
    class Meta:
        model = Sending
        fields = ['start', 'end', 'status', 'message', 'recipients']

    def __init__(self, *args, **kwargs):
        super(SendingForm, self).__init__(*args, **kwargs)
        #self.fields['start'].widget = widgets.AdminSplitDateTime()
        self.fields['start'].widget.attrs.update({'class': 'form-control'})
        self.fields['end'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'fio', 'comment']
