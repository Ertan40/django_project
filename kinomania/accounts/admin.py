from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from kinomania.accounts.forms import UserCreateForm

# password: password    ertan  (superuser)
UserModel = get_user_model()
@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    ...