from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from django.views import generic as views
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from kinomania.accounts.forms import UserCreateForm
from django.urls import reverse_lazy

UserModel = get_user_model()


def index(request):
    return HttpResponse('profile index')

# class IndexView(views.TemplateView):
#     template_name = 'common/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['permissions'] = self.request.user.has_perm('accounts.view_appuser')
#         return context
class SignUpView(views.CreateView):
    template_name = 'accounts/signup-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Your Registration is Successful! Welcome to our website!')
        return redirect(self.success_url)

class SignInView(LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')
