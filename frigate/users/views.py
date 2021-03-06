from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView,
                                       PasswordChangeView,
                                       PasswordResetView)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

from .models import Parking_place
from .forms import LoginForm, RegisterForm, ChangeParkForm, CreateParkForm


from django.conf import settings
User = settings.AUTH_USER_MODEL


def home(request):
    parks = Parking_place.objects.all()
    parks_count = parks.count()
    return render(request,
                  'users/home.html',
                  {'parks': parks,
                   'count': parks_count,
                   'booking': True})


@login_required
def create_park(request):
    form = CreateParkForm(request.POST or None)
    if form.is_valid():
        park = form.save(commit=False)
        park.save()
        return redirect(to='/')
    return render(request, 'users/create_park.html',
                  {'form': form,
                   'is_edit': False})


@login_required
def change_park(request, park_id):
    if request.user.role == 'Employee':
        return redirect(to='/')
    park = get_object_or_404(Parking_place, id=park_id)
    form = CreateParkForm(request.POST or None)
    if form.is_valid():
        park.save()
        return redirect(to='/')
    return render(request, 'users/create_park.html',
                  {'form': form,
                   'is_edit': True})


@login_required
def delete_park(request, park_id):
    Parking_place.objects.filter(id=park_id).delete()
    return redirect(to='/')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions setting your password"
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        park_form = ChangeParkForm(request.POST, instance=request.user)
        if park_form.is_valid():
            park_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        park_form = ChangeParkForm(instance=request.user)
    return render(request, 'users/profile.html', {'park_form': park_form})
