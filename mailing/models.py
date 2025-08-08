from django.db import models

from users.models import User


# Create your models here.
class Recipient(models.Model):
    """Recipient model"""

    email = models.CharField(max_length=250, verbose_name="Email", unique=True)
    fio = models.CharField(max_length=250, verbose_name="Fio")
    comment = models.TextField(verbose_name="Comment")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="RecipientOwner")

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'
        permissions = [
            ("can_view_recipient", "Can view recipient"),
        ]


class Message(models.Model):
    """Message model"""

    subject = models.CharField(max_length=250, verbose_name="Subject")
    body = models.TextField(verbose_name="Body")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageOwner")

    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        permissions = [
            ("can_view_message", "Can view messages"),
        ]


class Mailing(models.Model):
    """Mailing List model"""

    enabled = models.BooleanField(verbose_name="Enable Mailing", default=True)
    start = models.DateTimeField(verbose_name="Start Mailing")
    end = models.DateTimeField(verbose_name="End Mailing")
    status = models.CharField(
        max_length=50,
        verbose_name="Status",
        default="created",
        choices=[("created", "Created"), ("ended", "Ended"), ("running", "Running")],
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="Message")
    recipients = models.ManyToManyField(Recipient, related_name="Recipients")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MailingOwner")

    def __str__(self):
        return f"{self.message.subject} {self.start} - {self.end} :: {self.status}"

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'
        permissions = [
            ("can_view_mailing", "Can view mailing"),
        ]


class Result(models.Model):
    """Result model"""

    date = models.DateTimeField(verbose_name="Mailing date", auto_now_add=True)
    status = models.CharField(max_length=50, verbose_name="Status", blank=True, null=True)
    email = models.CharField(max_length=50, verbose_name="Email", blank=True, null=True)
    response = models.TextField(max_length=50, verbose_name="ServerResponse", blank=True, null=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="Mailing")
    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'
        permissions = [
            ("can_view_result", "Can view result"),
        ]
