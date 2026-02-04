from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *
from datetime import date

# Create your views here.

#homepage
def homepage(request):
    data=tbl_deliverystaff.objects.get(id=request.session["did"])
    return render(request,"DeliveryStaff/HomePage.html",{'data':data})

#profile
def myprofile(request):
    data=tbl_deliverystaff.objects.get(id=request.session["did"])
    return render(request,"DeliveryStaff/MyProfile.html",{'data':data})

#edit profile
def editprofile(request):
    prodata=tbl_deliverystaff.objects.get(id=request.session["did"])
    if request.method=="POST":
        prodata.deliverystaff_name=request.POST.get('txtname')
        prodata.deliverystaff_contact=request.POST.get('txtcon')
        prodata.deliverystaff_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"DeliveryStaff/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"DeliveryStaff/EditProfile.html",{'prodata':prodata})

#change password
def changepassword(request):
    if request.method=="POST":
        ccount=tbl_deliverystaff.objects.filter(id=request.session["did"],deliverystaff_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                deliverystaffdata=tbl_deliverystaff.objects.get(id=request.session["did"],deliverystaff_password=request.POST.get('txtcurpass'))
                deliverystaffdata.deliverystaff_password=request.POST.get('txtnewpass')
                deliverystaffdata.save()
                return render(request,"DeliveryStaff/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"DeliveryStaff/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"DeliveryStaff/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"DeliveryStaff/ChangePassword.html")

#shipped orderviewPots
def shippedpotsorderSelect(request):
    deliverystaff=tbl_deliverystaff.objects.get(id=request.session["did"])
    data=tbl_order.objects.filter(order_status=2)
    return render(request,"DeliveryStaff/PotsOrdersConfirmed.html",{'data':data})

#DeliveredOrdersPots
def deliveredpotsorderSelect(request):
    deliverystaff=tbl_deliverystaff.objects.get(id=request.session["did"])
    data=tbl_order.objects.filter(order_status=3)
    return render(request,"DeliveryStaff/PotsOrdersDelivered.html",{'data':data})

#shipped Orders Plants
def shippedplantsorderSelect(request):
    deliverystaff=tbl_deliverystaff.objects.get(id=request.session["did"])
    #booking=tbl_productbooking.objects.filter(deliverystaff=deliverystaff)
    #data=tbl_cart.objects.filter(ship_status=2,cart_status=1,booking=booking)
    data=tbl_cart.objects.filter(ship_status=2,cart_status=1)
    return render(request,"DeliveryStaff/PlantsOrdersConfirmed.html",{'data':data})

#DeliveredOrdersPlants
def deliveredplantsorderSelect(request):
    data=tbl_cart.objects.filter(ship_status=3,cart_status=1)
    return render(request,"DeliveryStaff/PlantsOrdersDelivered.html",{'data':data})

def updateproductbooking(request,bid):
    item = tbl_cart.objects.get(id=bid)
    if item.ship_status == 2:
        item.ship_status = 3  
        item.save()  
        return redirect("DeliveryStaff:shippedplantsorderSelect")
    item.save()  
    return redirect("DeliveryStaff:newplantorderSelect")