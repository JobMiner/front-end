from django.db import models

# Create your models here.
class Creator(models.Model):
    first_name = models.CharField(max_length=31, verbose_name='First Name')
    last_name = models.CharField(max_length=31, verbose_name='Last Name')

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "Creator"
        verbose_name_plural = "Creators"
        ordering = ("id", "first_name")