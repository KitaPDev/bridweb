from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label=_("Name"))
    contact_email = forms.EmailField(required=True, label=_("Email"))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label=_("Message")
    )
