from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from rest_framework import viewsets, permissions

from mailing.forms import SendingForm, MessageForm, RecipientForm
from mailing.models import Sending, Message, Recipient
from users.models import User


# Create your views here.
class HomeView(TemplateView):
    """Home view"""

    def get(self, request):
        context = {
            'lists': Sending.objects.count(),
            'active_lists': Sending.objects.filter(status='Running').count(),
            'recipients': User.objects.filter(is_active=True).count()
        }
        return render(request, 'home.pug', context)

class MessageListView(ListView):
    """Message list view"""
    model = Message
    template_name = 'message.pug'
    context_object_name = 'list'
    #def get(self, request):
    #    return render(request, 'home.pug')

class MessageCreateView(CreateView):
    """Message create view"""
    form_class = MessageForm
    template_name = 'message-form.pug'
    success_url = reverse_lazy('message')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MessageUpdateView(UpdateView):
    """Message update view"""
    form_class = MessageForm
    model = Message
    template_name = 'message-form.pug'
    success_url = reverse_lazy('message')

class RecipientListView(ListView):
    """Recipient list view"""
    model = Recipient
    template_name = 'recipient.pug'
    context_object_name = 'list'
    #def get(self, request):
    #    return render(request, 'home.pug')

class RecipientCreateView(CreateView):
    """Recipient create view"""
    form_class = RecipientForm
    template_name = 'recipient-form.pug'
    success_url = reverse_lazy('recipient')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class RecipientUpdateView(UpdateView):
    """Recipient update view"""
    model = Recipient
    form_class = RecipientForm
    template_name = 'recipient-form.pug'
    success_url = reverse_lazy('recipient')

class SendingListView(ListView):
    """Sending list view"""
    model = Sending
    template_name = 'sending.pug'
    context_object_name = 'list'
    #def get(self, request):
    #    return render(request, 'home.pug')

class SendingCreateView(CreateView):
    """Sending create view"""
    form_class = SendingForm
    template_name = 'sending-form.pug'
    success_url = reverse_lazy('sending')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SendingUpdateView(UpdateView):
    """Sending update view"""
    model = Sending
    form_class = SendingForm
    fields = ['subject','body']
    template_name = 'sending-form.pug'
    success_url = reverse_lazy('sending')

