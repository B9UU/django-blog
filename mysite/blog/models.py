from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# tables for database
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)

    # on_delete to delete the data if user was deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-details', kwargs={'pk':self.pk})
