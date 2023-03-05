from django.db import models

# Create your models here.
class OFundus(models.Model):
    class_name = models.CharField(max_length=10,null=True)
    refer_to_hospital = models.BooleanField(null=True)
    check_for_macular_edema = models.BooleanField(null=True)
    image = models.ImageField(upload_to='Images/', default='Images/None/No0img.jpg')

    def __str__(self) -> str:
        return f'{self.class_name}'