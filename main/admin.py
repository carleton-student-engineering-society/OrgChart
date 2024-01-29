# from django.contrib import admin

from main.models import Person, Organization, Role, Term
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)


class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)


class TermAdmin(admin.ModelAdmin):
    pass


admin.site.register(Term, TermAdmin)
