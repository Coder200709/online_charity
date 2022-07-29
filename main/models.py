from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
