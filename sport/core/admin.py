from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at')
    list_filter = ('status',)


admin.site.register(Menu)
admin.site.register(SportProgramme)
admin.site.register(FitnessExpert)
admin.site.register(Gallary)
admin.site.register(Traings)
admin.site.register(ServiceCategory)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Gratitude)
admin.site.register(UserName, UserAdmin)


# Register your models here.
