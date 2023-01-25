from django import forms
from board.models import Care


class CareForm(forms.ModelForm):
    class Meta:
        model = Care
        fields = ["title", "place", "content", "image"]
