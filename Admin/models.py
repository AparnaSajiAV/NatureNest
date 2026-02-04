from django.db import models

# Create your models here.

#district
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

#place
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)

#admin reg
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50) 
    admin_password=models.CharField(max_length=50)
    admin_photo = models.FileField(upload_to='Assets/AdminPhoto/')

#category(plant)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

#subcategory
class tbl_subcategory(models.Model):
    category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=50)

#pot type
class tbl_typepot(models.Model):
    type_name=models.CharField(max_length=50)

#pot shape
class tbl_shapepot(models.Model):
    shape_name=models.CharField(max_length=50)

#pot material
class tbl_materialpot(models.Model):
    material_name=models.CharField(max_length=50)
    
#pot size
class tbl_sizepot(models.Model):
    size_name=models.CharField(max_length=50)

#pot color
class tbl_colorpot(models.Model):
    color_name=models.CharField(max_length=50)

#Nursery Staff
class tbl_nurserystaff(models.Model):
    nurserystaff_name=models.CharField(max_length=50)
    nurserystaff_gender=models.CharField(max_length=50)
    nurserystaff_contact=models.CharField(max_length=50)
    nurserystaff_email=models.CharField(max_length=50)
    nurserystaff_password=models.CharField(max_length=50)
    nurserystaff_photo = models.FileField(upload_to='Assets/NurseryPhoto/')

#Delivery Staff
class tbl_deliverystaff(models.Model):
    deliverystaff_name=models.CharField(max_length=50)
    deliverystaff_gender=models.CharField(max_length=50)
    deliverystaff_contact=models.CharField(max_length=50)
    deliverystaff_email=models.CharField(max_length=50)
    deliverystaff_password=models.CharField(max_length=50)
    deliverystaff_photo = models.FileField(upload_to='Assets/DeliveryPhoto/')

