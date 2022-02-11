#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:18:47 2022

@author: guyu
"""

from django.urls import path
from rango import views
from django.conf.urls import url
app_name = 'rango'
urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),

  path('category/<slug:category_name_slug>/', views.show_category,
       name='show_category'),
  path('add_category/', views.add_category, name='add_category'),
  path('add_page/', views.add_page, name='add_page'),
  path('category/<slug:category_name_slug>/add_page/',
       views.add_page, name='add_page'),
]