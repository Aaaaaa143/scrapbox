from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profilepic",null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Scraps(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_scrap")
    name=models.CharField(max_length=200)
    condition=models.CharField(max_length=200,null=True)
    price=models.PositiveIntegerField()
    scrap_pic=models.ImageField(upload_to="scrap",null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="scrap_catogry")
    created_date=models.DateTimeField(auto_now_add=True)
    status_option=(
        ("Sold","sold"),
        ("Available","available")
    )
    status=models.CharField(max_length=200,choices=status_option,default="Available")

    def __str__(self):
        return self.name


class Bids(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="bid_holder")
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="bidded_scrap")
    amount=models.PositiveIntegerField()
    status=(
        ("reject","reject"),
        ("pending","pending"),
        ("accept","accept")
    )

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_wish")
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrap_wish")
    created_date=models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_review")
    scrap=models.ForeignKey(Scraps,on_delete=models.CASCADE,related_name="scrap_review")
    comment=models.CharField(max_length=200,null=True)
    rating=models.FloatField()

def create_profile(sender,created,instance,**kwargs):

    if created:
        Userprofile.objects.create(user=instance)

post_save.connect(create_profile,sender=User)