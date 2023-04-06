from .models import Shoes
from modeltranslation.translator import register, TranslationOptions

@register(Shoes)
class ShoesTranslationOptions(TranslationOptions):
    fields = ('about',)