from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Doctor)
class ProductAdmin(TranslationAdmin):
    list_display = ("specialty",)
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# Register your models here.

admin.site.register(UserProfile)
# admin.site.register(Doctor)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(FitnessProgram)
admin.site.register(Notification)
