#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:36:09 2022

@author: guyu
"""

from django import template
from rango.models import Category
	
register = template.Library()

	
@register.inclusion_tag('rango/cats.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}