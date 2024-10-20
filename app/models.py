from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class About(models.Model):
    name = models.CharField(max_length=200)
    descriptin = models.TextField()
    address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    gmail = models.EmailField()
    phone = models.CharField(max_length=200)
    cv = models.FileField(upload_to='cv')
    project_completed = models.IntegerField()

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    job = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    about = models.TextField()

    def __str__(self):
        return self.job


class Skill(models.Model):
    name = models.CharField(max_length=200,verbose_name='Name of Skill')
    percent = models.IntegerField()
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    url = models.URLField()
    image = models.ImageField(upload_to='projects/')
    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True, blank=True)
    text = RichTextField()
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/')
    tags = models.ManyToManyField(Tag)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    email = models.EmailField(null=True,blank=True)
   
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[0:50]

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.message[0:50]


