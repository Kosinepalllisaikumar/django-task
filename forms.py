from django import forms

from .models import Register, SignUp

class RegisterForm(forms.ModelForm):

    class Meta():
        model = Register
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)


class SignUpForm(forms.ModelForm):

    class Meta():
        model = SignUp
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
