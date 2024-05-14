"""Docstring."""
from django import forms

from .models import Contest


class ContestForm(forms.ModelForm):
    """Docstring."""

    class Meta:
        """Docstring."""

        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': 22, 'rows': 5}),
            'comment': forms.Textarea(attrs={'cols': 22, 'rows': 5})
        }
