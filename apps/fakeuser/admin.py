from django.contrib import admin
from .models import (
    FakeUser,
    PersonalInformation,
    Address,
    FakeToken
)

class PersonalInformationInline(admin.TabularInline):
    model = PersonalInformation

class AddressInline(admin.TabularInline):
    model = Address

@admin.register(FakeUser)
class fakeuserAdmin(admin.ModelAdmin):
    inlines = [
        PersonalInformationInline,
        AddressInline,
    ]

# admin.site.register(FakeUser)
admin.site.register(PersonalInformation)
admin.site.register(Address)
admin.site.register(FakeToken)