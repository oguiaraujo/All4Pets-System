from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        if self.status==True:
            status = "Ativo"
        else:
            status = "Inativo"
        return f"{self.name} - {status}"
