from django.contrib.auth import models


class User(models.User, models.PermissionsMixin):

    def __str__(self):
        return self.username
