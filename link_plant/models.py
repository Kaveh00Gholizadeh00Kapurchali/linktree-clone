from django.db import models

# Create your models here.


class Profile(models.Model):
    
    #first section is for database, second section will show up for admin for easy reading
    BG_CHOICES = (
        ("blue", "Blue"),
        ("green", "Green"),
        ("yellow", "Yellow"),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) 
    background_color = models.CharField(max_length=50, choices= BG_CHOICES)
    
    
    def __str__(self):
        return self.name
    
    
class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    #we have to use many to one relation ship for our profile management
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name= "links")
    
    
    def __str__(self):
        return f"{self.text} | {self.url}"
    