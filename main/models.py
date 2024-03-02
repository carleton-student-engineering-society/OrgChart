from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Role(models.Model):
    org = models.ForeignKey("Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    email = models.CharField(max_length=255, null=True)
    manager = models.ForeignKey("Role", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Term(models.Model):
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start) + " - " + self.person.name + " - " + self.role.name
