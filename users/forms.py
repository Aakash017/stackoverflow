from users.models import User
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        # exclude = ["user_isactive", "user_username", "user_roleid", "user_password", "user_gender", "user_dob",
        #            "user_image", "user_email", "user_mobile"]
