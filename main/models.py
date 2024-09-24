from django.db import models
from django.contrib.auth.models import User

import uuid
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField(default=0)

    @property
    def __str__(self):
        return self.name