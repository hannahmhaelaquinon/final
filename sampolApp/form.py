from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('student_id', 'sName', 'plateNum','vType')