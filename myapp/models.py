from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Number(models.Model):
    description = models.TextField(blank=True)  # Description field
    number = models.IntegerField(null=True, blank=True)  # Number field

    def __str__(self):
        return f"Todo {self.number}"  # Optional: Returns number as the title


class SavedPicture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_pictures')
    image = models.ImageField(upload_to='saved_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Picture by {self.user.username}"

