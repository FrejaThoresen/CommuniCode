from django.contrib.auth.models import User
from django.views.generic import TemplateView, View

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

dashboard_view = DashboardView.as_view()

class CreateProject(View):
    pass
