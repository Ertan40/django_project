from kinomania.accounts.views import index, SignUpView, SignInView, SignOutView, CreateUpStaffView
from django.urls import path


urlpatterns = [
    path('', index, name='profile index'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('register/staff/', CreateUpStaffView.as_view(), name='register staff user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
]

