from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out


def logged_in_message(sender, user, request, **kwargs):
    messages.success(request, "Logged in!")

user_logged_in.connect(logged_in_message)


def logged_out_message(sender, user, request, **kwargs):
    messages.success(request, "Logged out!")

user_logged_out.connect(logged_out_message)
