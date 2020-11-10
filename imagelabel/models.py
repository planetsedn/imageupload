from django.db import models
from imagelabel.visionfunc import detect_labels_url

# Create your models here.


class ImageUpload(models.Model):
    photo = models.ImageField(upload_to='Professionals_photo')
    print(photo)
    labels = models.TextField(default=False)

    def save(self, *args, **kwargs):

        self.labels =detect_labels_url(self.photo)
        super(ImageUpload, self).save(*args, **kwargs)

        def __str__(self):
            return str(self.labels)



