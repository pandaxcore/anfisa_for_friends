"""Docstring."""
from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    """Docstring."""
    form = ContestForm(request.POST or None)
    context = {'form': form}
    return render(request, 'contest/form.html', context)
