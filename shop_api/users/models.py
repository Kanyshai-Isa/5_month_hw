from django.db import models
from django.contrib.auth.models import User
import secrets

class ConfirmCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirm_code = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.confirm_code:
            self.confirm_code = f"{secrets.randbelow(900000) + 100000}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.confirm_code