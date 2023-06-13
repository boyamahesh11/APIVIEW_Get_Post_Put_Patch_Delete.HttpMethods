from django.db import models

# Create your models here.

class Product_category(models.Model):
    Pcid=models.IntegerField()
    Pcname=models.CharField(max_length=100)

    def __str__(self):
        return self.Pcname

class Product(models.Model):
    Pcname=models.ForeignKey(Product_category, on_delete=models.CASCADE)
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdescription=models.TextField()
    Pdate=models.DateField()

    def __str__(self):
        return self.Pname


