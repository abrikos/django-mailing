from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from mailing.forms import MailingForm, MessageForm, RecipientForm
from mailing.models import Mailing, Message, Recipient, Result
from mailing.services import MailingService
from users.models import User


# Create your views here.
class HomeView(TemplateView):
    """Home view"""

    def get(self, request):
        context = {
            "lists": Mailing.objects.count(),
            "active_lists": Mailing.objects.filter(status="Running").count(),
            "recipients": User.objects.filter(is_active=True).count(),
        }
        return render(request, "home.pug", context)


class MessageListView(LoginRequiredMixin, ListView):
    """Message list view"""

    model = Message
    template_name = "message.pug"
    context_object_name = "list"

    def get_queryset(self):
        # Filter the queryset to include only objects owned by the current user
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Message create view"""

    form_class = MessageForm
    template_name = "message-form.pug"
    success_url = reverse_lazy("message")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Message update view"""

    form_class = MessageForm
    model = Message
    template_name = "message-form.pug"
    success_url = reverse_lazy("message")


class RecipientListView(LoginRequiredMixin, ListView):
    """Recipient list view"""

    model = Recipient
    template_name = "recipient.pug"
    context_object_name = "list"

    def get_queryset(self):
        # Filter the queryset to include only objects owned by the current user
        return Recipient.objects.filter(owner=self.request.user)


class RecipientCreateView(LoginRequiredMixin, CreateView):
    """Recipient create view"""

    form_class = RecipientForm
    template_name = "recipient-form.pug"
    success_url = reverse_lazy("recipient")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    """Recipient update view"""

    model = Recipient
    form_class = RecipientForm
    template_name = "recipient-form.pug"
    success_url = reverse_lazy("recipient")


class MailingListView(LoginRequiredMixin, ListView):
    """Mailing list view"""

    model = Mailing
    template_name = "mailing.pug"
    context_object_name = "list"

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Mailing create view"""

    form_class = MailingForm
    template_name = "mailing-form.pug"
    success_url = reverse_lazy("mailing")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # Pass the current user
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Mailing update view"""

    model = Mailing
    form_class = MailingForm
    template_name = "mailing-form.pug"
    success_url = reverse_lazy("mailing")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user  # Pass the current user
        return kwargs


def run_mailing(request):
    status = "error"
    if request.POST:
        mailing_id = request.POST.get("mailing")
        print("ffffff", mailing_id)
        user = request.user
        status = MailingService.run_service(mailing_id, user)
    return JsonResponse({"status": status})


def get_results(request, pk):
    data = []
    if request.GET:
        user = request.user
        mailing = Mailing.objects.get(pk=pk, owner=user)
        if mailing:
            queryset = Result.objects.filter(mailing=pk).order_by("-date")
            data = serializers.serialize("json", queryset)
    return HttpResponse(data, content_type="application/json")
