from django.db import models
from django.contrib.auth.models import User

class Thought(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    # NEPIEVIENOT user_id DJANGO automatiski izdara
    # japarmaina pēc no null true uz null false


class Profile(models.Model):
    #blank = True allows blank or null value in the form
    profile_pic =models.ImageField(blank=True, default='Default.png')
    user = models.OneToOneField(User,max_length=10, on_delete=models.CASCADE)
