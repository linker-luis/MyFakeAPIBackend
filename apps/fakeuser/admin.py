from xml.parsers.expat import model
from django.contrib import admin
import nested_admin
from .models import (
    FakeUser,
    PersonalInformation,
    Location,
)

# class AddressInline(admin.StackedInline):
#     model = Address

# @admin.register(PersonalInformation)
# class PersonalInformationAdmin(admin.ModelAdmin):
#     inlines = [
#         AddressInline
#     ]

# class PersonalInformationInline(admin.TabularInline):
#     model = PersonalInformation

# @admin.register(FakeUser)
# class fakeuserAdmin(admin.ModelAdmin):
#     inlines = [
#         PersonalInformationInline,
#         # AddressInline,
#     ]

# # admin.site.register(FakeUser)
# # admin.site.register(PersonalInformation)
# admin.site.register(Address)
# admin.site.register(FakeToken)

class LocationInline(nested_admin.NestedStackedInline):
    model = Location

class PersonalInformationInline(nested_admin.NestedStackedInline):
    model = PersonalInformation
    inlines = [LocationInline]

@admin.register(FakeUser)
class FakeUserAdmin(nested_admin.NestedModelAdmin):
    inlines = [PersonalInformationInline]

# admin.site.register(FakeUser, FakeUserAdmin)