from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from rest_framework import viewsets, permissions

from mailing.forms import SendingForm, MessageForm, RecipientForm
from mailing.models import Sending, Message, Recipient, Result
from mailing.services import SendingService
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


class MessageListView(LoginRequiredMixin, ListView):
    """Message list view"""
    model = Message
    template_name = 'message.pug'
    context_object_name = 'list'

    def get_queryset(self):
        # Filter the queryset to include only objects owned by the current user
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Message create view"""
    form_class = MessageForm
    template_name = 'message-form.pug'
    success_url = reverse_lazy('message')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Message update view"""
    form_class = MessageForm
    model = Message
    template_name = 'message-form.pug'
    success_url = reverse_lazy('message')


class RecipientListView(LoginRequiredMixin, ListView):
    """Recipient list view"""
    model = Recipient
    template_name = 'recipient.pug'
    context_object_name = 'list'

    def get_queryset(self):
        # Filter the queryset to include only objects owned by the current user
        return Recipient.objects.filter(owner=self.request.user)


class RecipientCreateView(LoginRequiredMixin, CreateView):
    """Recipient create view"""
    form_class = RecipientForm
    template_name = 'recipient-form.pug'
    success_url = reverse_lazy('recipient')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    """Recipient update view"""
    model = Recipient
    form_class = RecipientForm
    template_name = 'recipient-form.pug'
    success_url = reverse_lazy('recipient')


class SendingListView(LoginRequiredMixin, ListView):
    """Sending list view"""
    model = Sending
    template_name = 'sending.pug'
    context_object_name = 'list'

    def get_queryset(self):
        return Sending.objects.filter(owner=self.request.user)


class SendingCreateView(LoginRequiredMixin, CreateView):
    """Sending create view"""
    form_class = SendingForm
    template_name = 'sending-form.pug'
    success_url = reverse_lazy('sending')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SendingUpdateView(LoginRequiredMixin, UpdateView):
    """Sending update view"""
    model = Sending
    form_class = SendingForm
    template_name = 'sending-form.pug'
    success_url = reverse_lazy('sending')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user
        return kwargs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Result.objects.filter(sending=1).order_by('-date')
        return context


def run_sending(request):
    status = 'error'
    if request.POST:
        sending_id = request.POST.get('sending')
        user = request.user
        status = SendingService.run_service(sending_id, user)
    return JsonResponse({'status':status})

def get_results(request, pk):
    data = []
    if request.GET:
        user = request.user
        sending = Sending.objects.get(pk=pk, owner=user)
        if sending:
            queryset = Result.objects.filter(sending=pk).order_by('-date')
            data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type="application/json")
