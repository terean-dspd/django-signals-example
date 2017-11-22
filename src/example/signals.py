from django.utils import timezone

def example_receiver(sender, instance, **kwargs):
    now = timezone.now()
    instance.fieldsignal = str(now) 
