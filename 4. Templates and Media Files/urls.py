#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 05:13:31 2022

@author: guyu
"""

from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
        path('', views.index, name='index'),
        path('about/', views.about, name='about'),
]