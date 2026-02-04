from django.db import models
from Guest.models import *
from NurseryStaff.models import *

# Create your models here.

#Complaint
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=150)
    complaint_details=models.CharField(max_length=500)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default="0")
    complaint_reply=models.CharField(max_length=500,null=True)
    complaint_replydate=models.DateField(null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

#rating & review
class tbl_review(models.Model):
    user_rating=models.IntegerField(max_length=50)
    user_review=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    review_datetime=models.DateTimeField(auto_now_add=True)
    productplant= models.ForeignKey(tbl_productplant,on_delete=models.CASCADE,null=True)
    productpot= models.ForeignKey(tbl_productpot,on_delete=models.CASCADE,null=True)

#plantorderbooking
class tbl_productbooking(models.Model):
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    booking_status = models.IntegerField(default="0")
    price = models.CharField(default="0",max_length=40)
    deliverystaff=models.ForeignKey(tbl_deliverystaff, on_delete=models.CASCADE,null=True)
    assign_status = models.IntegerField(default="0")

#plantmycart
class tbl_cart(models.Model):
    booking = models.ForeignKey(tbl_productbooking, on_delete=models.CASCADE)
    productplant=models.ForeignKey(tbl_productplant, on_delete=models.CASCADE)
    cart_qty= models.CharField(max_length=500)
    cart_status=models.IntegerField(default="0")
    ship_status=models.IntegerField(default="0")

#Wishlistpot
class tbl_wishlistpot(models.Model):
    productpot=models.ForeignKey(tbl_productpot, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    wishlist_date=models.DateField(auto_now_add=True)

#Wishlistplant
class tbl_wishlistplant(models.Model):
    productplant=models.ForeignKey(tbl_productplant, on_delete=models.CASCADE)  
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    wishlist_date=models.DateField(auto_now_add=True)

#order
class tbl_order(models.Model):
    productpot=models.ForeignKey(tbl_productpot, on_delete=models.CASCADE,null=True)
    order_date=models.DateField(auto_now_add=True)
    order_deliverydate=models.DateField(null=True)
    order_qty=models.CharField(max_length=50)
    order_amount=models.CharField(max_length=50)
    order_status = models.CharField(max_length=50,default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)


