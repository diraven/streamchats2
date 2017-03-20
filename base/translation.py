from modeltranslation.translator import translator, TranslationOptions
from base.models import News

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

translator.register(News, NewsTranslationOptions)