from django.db import models

# Create your models here.
class OFundus(models.Model):
    class_name = models.CharField(max_length=60,null=True)
    image = models.ImageField(upload_to='Images/', default='Images/None/No0img.jpg')

    def __str__(self) -> str:
        return f'{self.class_name}'