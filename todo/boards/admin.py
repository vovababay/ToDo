from django.contrib import admin
from boards.models import *


class NoteAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'status', 'author']
    list_display = ('title', 'description', 'status', 'author')


admin.site.register(Note, NoteAdmin)
