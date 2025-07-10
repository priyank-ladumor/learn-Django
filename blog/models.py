from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    BLOG_TYPE = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Draft', 'Draft'),
    ]
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    blog_type = models.CharField(max_length=7, choices=BLOG_TYPE, default='Public')
    
    def __str__(self):
        return self.title