from django.shortcuts import render
from django.views.generic import TemplateView

from mailing.models import MailingList
from users.models import User


# Create your views here.
class HomeView(TemplateView):
    """Home view"""
    def get(self, request):
        context = {
            'lists':MailingList.objects.count(),
            'active_lists':MailingList.objects.filter(status='Running').count(),
            'recipients': User.objects.filter(is_active=True).count()
        }
        return render(request,'home.pug', context)