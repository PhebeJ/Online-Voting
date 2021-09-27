# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import home, about, docs, faq, privacy, website

urlpatterns = [
  url(r'^$', home),
  url(r'^about$', about),
  url(r'^docs$', docs),
  url(r'^faq$', faq),
  url(r'^privacy$', privacy),
  url(r'^website$', website),
]
