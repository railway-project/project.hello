from django.db import models
from django.utils.text import slugify

class Poem(models.Model):
    CATEGORY_CHOICES = [
        ('love', 'Love'),
        ('motivational', 'Motivational'),
        ('sad', 'Sad'),
        # Add more categories as needed
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='uncategorized')
    image = models.ImageField(upload_to='poem_images/', default='rishi-image.jpg')
    is_new = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    views = models.IntegerField(default=0)
    publish_date= models.DateField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug:  # Check if the slug is empty
            self.slug = slugify(self.title)  # Generate the slug if it is empty
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Comment(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
