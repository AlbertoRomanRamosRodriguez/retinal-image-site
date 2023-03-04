from django.db import models

# Create your models here.
class OFundus(models.Model):
    class_name = models.CharField(max_length=60,null=True)
    image = models.ImageField()

    def __str__(self) -> str:
        return f'{self.class_name}'