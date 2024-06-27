from .models import Doctor
from modeltranslation.translator import TranslationOptions, register


@register(Doctor)
class HotelTranslationOptions(TranslationOptions):
    fields = ('user', 'education')