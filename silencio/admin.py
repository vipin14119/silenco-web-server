from django.contrib import admin
from silencio.models import Record, User


class UserClass(admin.ModelAdmin):

    class Meta:
        model = User
admin.site.register(User, UserClass)


class RecordClass(admin.ModelAdmin):
    list_display = ('user', 'name', 'db_level')

    class Meta:
        model = Record
admin.site.register(Record, RecordClass)
