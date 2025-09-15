from django.views.generic import TemplateView
from django.urls import path

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any context data here, like the current date
        # context['today'] = datetime.date.today()
        return context   