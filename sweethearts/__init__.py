# -*-coding:utf-8-*-

from django.apps import AppConfig
import os

default_app_config = 'sweethearts.SweetheartsConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class SweetheartsConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = "我 们 的 纪 念"