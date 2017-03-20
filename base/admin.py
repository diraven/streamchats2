from base.models import News
from django.contrib import admin

@admin.register(News)
class ChatAdmin(admin.ModelAdmin):
    pass

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profiles'
#
# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#
#     # Re-register UserAdmin
#     admin.site.unregister(User)
#     admin.site.register(User, UserAdmin)
#
#
