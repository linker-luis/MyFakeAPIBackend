from django.contrib import admin
from .models import ApiDoc, ApiDocSection

class ApiDocSectionInline(admin.TabularInline):
    model = ApiDocSection

@admin.register(ApiDoc)
class ApiDocAdmin(admin.ModelAdmin):
    inlines = [
        ApiDocSectionInline
    ]

admin.site.register(ApiDocSection)