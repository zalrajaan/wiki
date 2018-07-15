from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    
        return "/detail/%i/" % self.id
