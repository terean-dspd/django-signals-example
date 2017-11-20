from django.contrib import admin

from .models        import TestModel

class TestModelAdmin(admin.ModelAdmin):
    list_display = [
                    'pk',
                    'fieldself',
                    'fieldsignal',
                    ]
    class Meta:
        model = TestModel

admin.site.register(TestModel, TestModelAdmin)
