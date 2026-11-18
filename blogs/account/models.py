from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Blog_editors(models.Model):
    id = models.IntegerField(),
    firstname = models.CharField(max_length=100),
    secondname = models.CharField(max_length=100),
    blog_text = models.TextField()
    def __str__(self) -> str:
        return f"{self.firstname}"
    def save(self,*args, **kwargs):
              super().save(*args,**kwargs)
    
class Category(models.Model):
    categories = models.CharField(max_length=100)
    slug =  models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    
    def save(self,*args, **kwargs):
          self.slug = slugify(self.categories)
          super().save(*args,**kwargs)
          
    def __str__(self):
       return f"{self.categories}"
    

class Blogs(models.Model):
  title = models.CharField(max_length=200)
  image = models.ImageField(upload_to="blogs")
  description = models.TextField()
  is_active = models.BooleanField(default=False)
  is_home = models.BooleanField(default=False) 
  slug = models.SlugField(blank=True,unique=True,db_index=True,editable=False)
  category = models.ManyToManyField(Category)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs", null=True, blank=True)
  
  def __str__(self):
     return   f"{self.title}"
  def save(self,*args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args,**kwargs)
      
