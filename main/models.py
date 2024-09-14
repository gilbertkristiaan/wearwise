from django.db import models
import uuid
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField(default=1)

    @property
    def __str__(self):
        return self.name