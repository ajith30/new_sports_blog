from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  #In blog, every post has title name
    author = models.ForeignKey(
                'auth.User',
                on_delete = models.CASCADE,
            )
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to = 'media/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """A string representation of title which is shown at admin site."""
        return self.title

    def summary(self):
        return self.body[:150]

#Let’s send a user to the detail page after successfully submit a new post form
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
