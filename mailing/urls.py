from django.urls import path

from mailing import views

urlpatterns = [
    path(r"mailing", views.MailingListView.as_view(), name="mailing"),
    path(r"mailing-create", views.MailingCreateView.as_view(), name="mailing-create"),
    path(
        r"mailing-update/<int:pk>",
        views.MailingUpdateView.as_view(),
        name="mailing-update",
    ),
    path(r"message", views.MessageListView.as_view(), name="message"),
    path(r"message-create", views.MessageCreateView.as_view(), name="message-create"),
    path(
        r"message-update/<int:pk>",
        views.MessageUpdateView.as_view(),
        name="message-update",
    ),
    path(r"recipient", views.RecipientListView.as_view(), name="recipient"),
    path(
        r"recipient-create",
        views.RecipientCreateView.as_view(),
        name="recipient-create",
    ),
    path(
        r"recipient-update/<int:pk>",
        views.RecipientUpdateView.as_view(),
        name="recipient-update",
    ),
    path("run", views.run_mailing, name="run"),
    path("results/<int:pk>", views.get_results, name="results"),
    path("users/", views.UsersListView.as_view(), name="users"),
    path("block-user/<int:pk>", views.block_user, name="block-user"),
    path("mailings-all/", views.MailingsAllListView.as_view(), name="mailings-all"),
    path("disable-mailing/<int:pk>", views.disable_mailing, name="disable-mailing"),
]
