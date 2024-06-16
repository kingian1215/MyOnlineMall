from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=True) 
    # 有效用户 預設為 False,若不想人工審核,可直接設為 True
    is_student = models.BooleanField(default=False) # 用戶別為學生
    is_teacher = models.BooleanField(default=False) # 用戶別為老師
