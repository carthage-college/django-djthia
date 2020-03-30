# -*- coding: utf-8 -*-

"""URLs for all views."""

from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from djthia.gearup import views


urlpatterns = [
    path(
        'success/',
        TemplateView.as_view(template_name='gearup/success.html'),
        name='gearup_success',
    ),
    # donation form
    path('give/', views.donation, name='donation'),
    # notes form
    path('notes/', views.notes, name='notes'),
    # questionnaire form
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    # redirect
    path('', RedirectView.as_view(url=reverse_lazy('home'))),
]
