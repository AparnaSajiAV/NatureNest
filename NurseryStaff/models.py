from django.db import models
from Admin.models import *
from User.models import *

# Create your models here.

#PRODUCT PLANT
class tbl_productplant(models.Model):
    productplant_name=models.CharField(max_length=50)
    productplant_description=models.CharField(max_length=50)
    productplant_rate=models.CharField(max_length=50)
    productplant_image=models.FileField(upload_to='Assets/ProductPlantPhoto/')
    subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)

#Galley Plant
class tbl_galleryplant(models.Model):
    product=models.ForeignKey(tbl_productplant, on_delete=models.CASCADE)
    galleryplant_file=models.FileField(upload_to='Assets/GalleryPlantPhoto/')
    subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)

#PRODUCT POT
class tbl_productpot(models.Model):
    productpot_name=models.CharField(max_length=50)
    productpot_description=models.CharField(max_length=50)
    productpot_rate=models.CharField(max_length=50)
    productpot_image=models.FileField(upload_to='Assets/ProductPotPhoto/')
    type = models.ForeignKey(tbl_typepot, on_delete=models.CASCADE)
    size = models.ForeignKey(tbl_sizepot, on_delete=models.CASCADE)
    shape = models.ForeignKey(tbl_shapepot, on_delete=models.CASCADE)
    material = models.ForeignKey(tbl_materialpot, on_delete=models.CASCADE)
    color = models.ForeignKey(tbl_colorpot, on_delete=models.CASCADE)

#Galley Pot
class tbl_gallerypot(models.Model):
    product=models.ForeignKey(tbl_productpot, on_delete=models.CASCADE)
    gallerypot_file=models.FileField(upload_to='Assets/GalleryPotPhoto/')

#stock plant
class tbl_stockplant(models.Model):
    stock_quantity=models.IntegerField()
    productplant = models.ForeignKey(tbl_productplant, on_delete=models.CASCADE,null=True)
    stock_date=models.DateField(null=True)

#stoclpot
class tbl_stockpot(models.Model):
    stock_quantity=models.IntegerField()
    productpot = models.ForeignKey(tbl_productpot, on_delete=models.CASCADE,null=True)
    stock_date=models.DateField(null=True)
    
    