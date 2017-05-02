# Create your views here.
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class AddDeal(TemplateView):
    template_name = "add-deal.html"


class SignIn(TemplateView):
    template_name = "sign-in.html"


class SignUp(TemplateView):
    template_name = "sign-up.html"


class DealsView(TemplateView):
    template_name = "deals.html"