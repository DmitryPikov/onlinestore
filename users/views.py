import os

from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


def custom_logout(request):
    logout(request)
    return redirect('/')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.save()
        send_mail(
            subject="Регистрация на Skystore",
            message="Спасибо за регистрацию!",
            from_email=os.getenv('EMAIL_HOST_USER'),
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
