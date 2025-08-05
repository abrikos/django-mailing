from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm

from mailing.models import Sending, Message, Recipient
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class SendingForm(ModelForm):
    class Meta:
        model = Sending
        fields = ['start', 'end', 'status', 'message', 'recipients']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(SendingForm, self).__init__(*args, **kwargs)
        self.fields['message'].queryset = Message.objects.filter(owner=user)
        self.fields['recipients'].queryset = Recipient.objects.filter(owner=user)
        self.fields['start'].widget = DateTimePickerInput()
        self.fields['end'].widget = DateTimePickerInput()
        self.fields['start'].widget.attrs.update({'class': 'form-control'})
        self.fields['end'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
        self.fields['recipients'].widget.attrs.update({'class': 'form-control'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'fio', 'comment']
