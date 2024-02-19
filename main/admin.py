# from django.contrib import admin

from .models import Organization, Person, Role, Term
from django.contrib import admin


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)


class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)


class TermAdmin(admin.ModelAdmin):
    pass


admin.site.register(Term, TermAdmin)
