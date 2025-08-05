from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    """Home view"""
    template_name = 'home.pug'
