from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
import random
import hashlib
from config import settings
from users.forms import CustomUserCreationForm, CustomAuthenticationForm, UserPassChangeForm, PasswordRestoreForm
from users.models import User


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.pug'
    form_class = CustomAuthenticationForm


class RestorePassword(TemplateView):
    def get(self, request):
        form = PasswordRestoreForm
        return render(request, 'password-restore.pug', {'form':form})

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user:
            rnd = random.randint(0, 1000000)
            user.set_password(f'{rnd}')
            user.save()
            subject = 'New password'
            message = f'{rnd}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)

        return redirect('login')


class ConfirmEmail(TemplateView):
    def get(self, request):
        code = request.GET.get('code')
        user = User.objects.get(confirm=code)
        if user:
            user.is_active = True
            user.save()
        return render(request, 'confirm.pug')


class RegisterView(CreateView):
    template_name = 'register.pug'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        md5_hash = hashlib.md5()
        rnd = random.randint(0, 1000000)
        md5_hash.update(rnd.to_bytes(4, byteorder='big'))
        form.instance.confirm = md5_hash.hexdigest()
        login(self.request, user)
        self.send_confirm_email(user.email, form.instance.confirm)
        return super().form_valid(form)

    def send_confirm_email(self, user_email, code):
        subject = 'Confirm email'
        message = f'http://{self.request.headers['Host']}/user/confirm?code={code}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class CabinetView(TemplateView):
    def get(self, request):
        return render(request, 'cabinet.pug' )

class PasswordChangeView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = UserPassChangeForm(request.user)
        return render(request, 'password-change.pug', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserPassChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('cabinet')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'password-change.pug', {'form': form})
