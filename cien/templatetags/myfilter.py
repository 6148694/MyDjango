#!/usr/bin/env python 
# coding:utf-8
from django import template

register = template.Library()
@register.filter(name="replace")
def myreplace(value,arg):
    return value.replace(arg,"@@")
