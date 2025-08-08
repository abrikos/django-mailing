from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.forms import ModelForm

from mailing.models import Mailing, Message, Recipient


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ["start", "end", "enabled", "message", "recipients"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields["message"].queryset = Message.objects.filter(owner=user)
        self.fields["recipients"].queryset = Recipient.objects.filter(owner=user)
        self.fields["start"].widget = DateTimePickerInput()
        self.fields["end"].widget = DateTimePickerInput()
        self.fields["start"].widget.attrs.update({"class": "form-control"})
        self.fields["end"].widget.attrs.update({"class": "form-control"})
        self.fields["message"].widget.attrs.update({"class": "form-control"})
        self.fields["recipients"].widget.attrs.update({"class": "form-control"})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["subject", "body"]


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ["email", "fio", "comment"]
