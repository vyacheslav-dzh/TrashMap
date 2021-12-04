from django.db import models

class CamMarker(models.Model):
    c_name = models.CharField(max_length=255)
    c_cord = models.CharField(max_length=255)
    c_mode = models.IntegerField()
    c_date = models.DateTimeField()
    c_image = models.TextField()
    #с_img = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d',
                              #help_text='150x150px', verbose_name='Ссылка картинки')

    def __str__(self):
        return self.c_name