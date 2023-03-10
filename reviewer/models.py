from django.db import models

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Course(models.Model):

    Course_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=34)
    Tag =  models.CharField(max_length=34)
    Description = models.CharField(max_length=2000)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Name)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Courses'

        
    def __str__(self):
        return self.Name
    
class Review(models.Model):

    
    Review_ID = models.AutoField(primary_key=True)
    
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    Rating = models.IntegerField(default=0)

    Comment = models.CharField(max_length=2000)

