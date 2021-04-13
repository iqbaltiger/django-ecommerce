from django.db import models
from django.contrib.auth.models import AbstractUser


user_type_list = (
   (1, 'admin'),
   (2, 'shop-manager'),
   (3, 'sales-man'),
   (4,'store-keeper'),
   (5,'customer')
    
    )


class User(AbstractUser):
    ip_address = models. GenericIPAddressField()
    status = models.BooleanField(default=True)
    about = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(default="dummy-profile-pic-male1.webp", null=True)
    last_login = models.DateTimeField(auto_now=True)
    last_logout = models.DateTimeField(auto_now=True)
    user_type = models.CharField(max_length=2, choices=user_type_list, default='shop-manager') # multiple user type 