from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class ReportsView(TemplateView):
    template_name = 'reports.html'