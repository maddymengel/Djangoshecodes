from django.urls import path
from .views import CreateAccountView
from .views import account_details
# from .views import profile

from .views import account_details

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account/', account_details, name='account_details'),
    # path('profile/', profile, name='profile'),
]