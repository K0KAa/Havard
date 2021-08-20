from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=64)
    start_bid = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    image_url = models.CharField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date_created =models.DateTimeField(default=timezone.now)
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)

class Bid(models.Model):
        user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
        listing = models.ForeignKey(Listing,on_delete=models.CASCADE)
        bid_amount = models.DecimalField(max_digits=7,decimal_places=2)