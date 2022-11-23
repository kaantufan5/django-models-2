from django.db import models

class Creator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

'''

on_delete properties:

# CASCADE -> if primary deleted, delete foreing too.
# SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
# SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value")
# DO NOTHING -> if primary deleted, do nothing.
# PROTECT -> if foreign is exist, can not delete primary.

'''

# one2one relation:
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"