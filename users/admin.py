from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'city', 'phone')
    search_fields = ('user__username', 'city', 'hobby')
    list_filter = ('city',)

#Malou!1997?