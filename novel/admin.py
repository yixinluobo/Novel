from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from novel.models import Novel, Chapter, Brand, User


class MyUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'mobile', 'email')
        }),
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Brand)
