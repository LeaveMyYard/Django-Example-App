from django.core.exceptions import ValidationError
from django import forms
from datetime import date
from .models import BookInstance


class ReserveBookForm(forms.Form):
    return_date = forms.DateField(
        help_text="Enter a date, at least today.", required=True
    )

    def clean_return_date(self):
        data = self.cleaned_data["return_date"]

        if data < date.today():
            raise ValidationError("Invaid date - return in the past")

        return data


class BookInstanceEditForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ["status", "due_back"]

        help_texts = {
            "status": "Change current book instance status",
            "due_back": "Enter a date, at least today.",
        }

    def clean_due_back(self):
        data = self.cleaned_data["due_back"]

        if data < date.today():
            raise ValidationError("Invaid date - return in the past")

        return data
