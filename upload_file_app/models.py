from django.db import models

# Create your models here.

class Upload(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    file = models.FileField(upload_to="files/")

    class Meta:
        verbose_name = "Upload"
        verbose_name_plural = verbose_name + "s"
        ordering = ['-id']
    
    def __str__(self):
        return self.title