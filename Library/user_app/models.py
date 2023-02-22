from django.db import models

# Create your models here.


class ApprovalForUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.username
