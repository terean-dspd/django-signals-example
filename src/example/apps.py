from django.apps import AppConfig
from django.db.models.signals import pre_save

class ExampleConfig(AppConfig):
    name = 'example'
    def ready(self):
        from .signals                 import example_receiver
        pre_save.connect(example_receiver, sender='example.TestModel')
