from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)


class Organization(models.Model):
    name = models.CharField(max_length=255)


class Role(models.Model):
    org = models.ForeignKey("Organization", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    manager = models.ForeignKey("Role", on_delete=models.CASCADE, null=True, blank=True)


class Term(models.Model):
    start = models.DateField()
    end = models.DateField(null=True)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)
