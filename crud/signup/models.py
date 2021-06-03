from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pubdate = models.DateTimeField()
    email = models.EmailField(max_length=100)
    introduce = models.TextField()

    def info_summary (self):
        return self.introduce[:100]