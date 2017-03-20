from chats.models import Chat, Provider
from django.contrib import admin

# Register your models here.

@admin.register(Provider, Chat)
class ChatAdmin(admin.ModelAdmin):
    pass