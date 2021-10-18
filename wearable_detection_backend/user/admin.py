from django.contrib import admin

# Register your models here.
from user.models import User

admin.site.site_header = 'wearable-detection-backend'
admin.site.site_title = 'wearable-detection-backend'


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'phone', 'sex', 'birthday')
    list_per_page = 25
