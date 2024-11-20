from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    time = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=1)
    
    