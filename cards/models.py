from django.db import models
import uuid

# Create your models here.
class Card(models.Model):
    '''
    The elements of a card
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    introduction = models.TextField()
    author = models.CharField(max_length=64)
    url = models.URLField(max_length=512)
    create_data = models.DateTimeField(auto_now=True) # Time that the product added to this site
    rate = models.IntegerField() # The Cards will be sort by this
