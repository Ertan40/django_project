from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UsernameField

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {'username': auth_forms.UsernameField}



class UserCreateStaffForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all().order_by('name'))

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'groups')
        widgets = {
            'password': forms.PasswordInput(),
        }

        def save(self, commit=True):
            user = super().save(commit=False)
            password = self.cleaned_data['password']
            user.set_password(password)
            user.is_staff = True
            if commit:
                user.save()
                user.groups.set(self.cleaned_data['groups'])
                return user



class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        # fields = ('first_name',)
        fields = '__all__'
        field_classes = {"username": auth_forms.UsernameField}