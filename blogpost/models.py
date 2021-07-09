from django.db import models
from django.contrib.auth.models import AbstractUser

# class Profile(models.Model):
#     my_user = models.OneToOneField(User, on_delete=models.CASCADE)
#     factoid = models.CharField(max_length=100)

    # def __str__(self):
    #     return f"{self.my_user.username}, {self.factoid}"

class Profile(AbstractUser):
    factoid = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}, {self.factoid}"


class BlogPosts(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.author}, {self.title}"