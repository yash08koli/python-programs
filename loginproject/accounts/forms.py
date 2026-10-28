import re
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data["username"]

        if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
            raise forms.ValidationError(
                "Username must be 3-20 letters, numbers or underscores."
            )

        return username

    def clean_password(self):
        password = self.cleaned_data["password"]

        if not re.fullmatch(
            r"(?=.*[A-Za-z])(?=.*\d).{8,}", password
        ):
            raise forms.ValidationError(
                "Password must contain at least 8 characters, "
                "one letter and one number."
            )

        return password