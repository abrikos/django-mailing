from django.urls import path


from mailing import views

urlpatterns = [
    path(r'sending', views.SendingListView.as_view(), name="sending"),
    path(r'sending-create', views.SendingCreateView.as_view(), name="sending-create"),
    path(r'sending-update/<int:pk>', views.SendingUpdateView.as_view(), name="sending-update"),
    path(r'message', views.MessageListView.as_view(), name="message"),
    path(r'message-create', views.MessageCreateView.as_view(), name="message-create"),
    path(r'message-update/<int:pk>', views.MessageUpdateView.as_view(), name="message-update"),
    path(r'recipient', views.RecipientListView.as_view(), name="recipient"),
    path(r'recipient-create', views.RecipientCreateView.as_view(), name="recipient-create"),
    path(r'recipient-update/<int:pk>', views.RecipientUpdateView.as_view(), name="recipient-update"),
]