# from django.contrib import admin

from main.models import Person, Organization, Role, Term
from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")


admin.site.register(Person, PersonAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Organization, OrganizationAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ("org", "name", "email", "manager")
    search_fields = ("org", "name", "desc", "email", "manager")


admin.site.register(Role, RoleAdmin)


class TermAdmin(admin.ModelAdmin):
    list_display = ("get_org", "get_role", "start", "end", "get_name", "get_email")
    search_fields = ("role__org__name", "role__name", "start", "end", "person__name", "person__email")

    def get_org(self, obj):
        return obj.role.org

    get_org.admin_order_field = "org"
    get_org.short_description = "Organization"

    def get_role(self, obj):
        return obj.role.name

    get_role.admin_order_field = "role"
    get_role.short_description = "Role Name"

    def get_name(self, obj):
        return obj.person.name

    get_name.admin_order_field = "person_name"
    get_name.short_description = "Person's Name"

    def get_email(self, obj):
        return obj.person.email

    get_email.admin_order_field = "person_email"
    get_email.short_description = "Person's Email"


admin.site.register(Term, TermAdmin)
