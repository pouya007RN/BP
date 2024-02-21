from django.contrib import admin
from .models import Content, ContentRate


admin.site.register(ContentRate)
admin.site.register(Content)