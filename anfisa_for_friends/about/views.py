"""Docstring."""
from typing import Any
from django.views.generic.base import TemplateView
from contest.models import Contest


class DescriptionView(TemplateView):
    """Docstring."""

    template_name = 'about/description.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Docstring."""
        context = super().get_context_data(**kwargs)
        # contests = Contest.objects.all()
        context["contest_count"] = Contest.objects.all().count()
        # print(contests.count())
        return context
