"""Docstring."""
from django.shortcuts import render

from .forms import ContestForm
from .models import Contest


def proposal(request):
    """Docstring."""
    form = ContestForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    """Docstring."""
    list = Contest.objects.all().order_by('id')
    context = {'list': list}
    return render(request, 'contest/contest_list.html', context)
