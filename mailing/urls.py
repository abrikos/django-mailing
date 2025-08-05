from django.urls import path

from mailing import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

]