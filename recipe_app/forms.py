from django import forms
from recipe_app.models import LoginInfo

class NewUserForm(forms.ModelForm):

    verify_email = forms.EmailField(label='Please verify email')

    class Meta():
        model = LoginInfo
        fields = ['username', 'email', 'verify_email']

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")