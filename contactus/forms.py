from django import forms
from .models import Contact
from django.db import models


class ContactImage(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

