from django.views.generic import TemplateView
from communicode.gitlab_api import wrappers

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context_data = super(DashboardView, self).get_context_data(**kwargs)
        context_data['projects'] = wrappers.get_projects()
        # import ipdb; ipdb.set_trace()
        return context_data

dashboard_view = DashboardView.as_view()
