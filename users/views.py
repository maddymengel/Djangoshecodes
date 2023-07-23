from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm


# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def account_details(request):
    user = request.user
    return render(request, 'users/account_details.html', {'user':user})