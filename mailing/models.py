from django.db import models

from users.models import User


# Create your models here.
class Recipient(models.Model):
    """Recipient model"""
    email = models.CharField(max_length=250, verbose_name='Email', unique=True)
    fio = models.CharField(max_length=250, verbose_name='Fio')
    comment = models.TextField(verbose_name='Comment')

class Message(models.Model):
    """Message model"""
    subject = models.CharField(max_length=250, verbose_name='Subject')
    body = models.TextField(verbose_name='Body')

class MailingList(models.Model):
    """Mailing List model"""
    start = models.DateTimeField(verbose_name='StartSending')
    end = models.DateTimeField(verbose_name='EndSending')
    status = models.CharField(max_length=50, verbose_name='Status', default='Создана')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='Message')
    recipients = models.ManyToManyField(Recipient, related_name='Recipients')

class Sending(models.Model):
    """Try to send model """
    date = models.DateTimeField(verbose_name='Sending date')
    status = models.CharField(max_length=50, verbose_name='Status')
    response = models.TextField(max_length=50, verbose_name='ServerResponse')
    mailing_list = models.ForeignKey(MailingList, on_delete=models.CASCADE, related_name='MailingList')