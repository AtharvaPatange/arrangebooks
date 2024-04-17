from django.db import models
from django.contrib.auth.models import User


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     publication_date = models.DateField()

#     class Meta:
#         app_label='books'

#     def __str__(self):
#         return self.titl
class   Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    # participants =
    updated=models.TimeField(auto_now=True)
    created=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated=models.TimeField(auto_now=True)
    created=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]