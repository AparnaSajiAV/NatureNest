from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
import random
from django.core.mail import send_mail,settings
# Create your views here.

#New User Reg
def userInsert(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
        UserName=request.POST.get("txtname")
        UserAddress=request.POST.get("txtaddress")
        UserGender=request.POST.get("txtgender")
        UserContact=request.POST.get("txtcont")
        UserEmail=request.POST.get("txtemail")
        UserPassword=request.POST.get("txtpass")
        UserPhoto=request.FILES.get("fileimg")
        Place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=UserName,user_address=UserAddress,user_gender=UserGender,user_contact=UserContact,place=Place,user_email=UserEmail,user_password=UserPassword,user_photo=UserPhoto)
        return redirect("WebGuest:Login")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

#Ajax place
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})

#Login
def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        admincount=tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        deliverycount=tbl_deliverystaff.objects.filter(deliverystaff_email=request.POST.get("txt_email"),deliverystaff_password=request.POST.get("txt_password")).count()
        nurserycount=tbl_nurserystaff.objects.filter(nurserystaff_email=request.POST.get("txt_email"),nurserystaff_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")
        elif admincount > 0:
            admin=tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"]=admin.id
            request.session["aname"]=admin.admin_name
            return redirect("WebAdmin:homepageLoarding")
        elif deliverycount>0:
            delivery=tbl_deliverystaff.objects.get(deliverystaff_email=request.POST.get("txt_email"),deliverystaff_password=request.POST.get("txt_password"))
            request.session['did']=delivery.id
            request.session["dname"]=delivery.deliverystaff_name
            return redirect("DeliveryStaff:homepage")
        elif nurserycount>0:
            nursery=tbl_nurserystaff.objects.get(nurserystaff_email=request.POST.get("txt_email"),nurserystaff_password=request.POST.get("txt_password"))
            request.session['nid']=nursery.id
            request.session["nname"]=nursery.nurserystaff_name
            return redirect("NurseryStaff:homepage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")

#Index  
def index(request):
    return render(request,"Guest/Index.html")

def about(request):
    admin=tbl_admin.objects.all()
    nursery=tbl_nurserystaff.objects.all()
    delivery=tbl_deliverystaff.objects.all()
    return render(request,"Guest/about.html",{"admin":admin,"nursery":nursery,"delivery":delivery})

def portfolio(request):
    return render(request,"Guest/portfolio.html")

def contact(request):
    return render(request,"Guest/contact.html")

def blog(request):
    return render(request,"Guest/blog.html")

def ForgotPass(request):
    if request.method=="POST":
        otp=(random.randint(100000,999999))
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txt_email')
        send_mail(
            'Respected Sir/Madam '+" ",#subject
            "Your Otp is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txt_email')],
        )
        return redirect('WebGuest:ValidateOTP')
    else:
        return render(request,"Guest/ForgotPassword.html")

def ValidateOTP(request):
    if request.method=="POST":
        otp=request.POST.get("txt_otp")
        ce=str(request.session["otp"])
        if otp==ce:
            return redirect("WebGuest:CreatePass")
    return render(request,"Guest/ValidateOTP.html")

def CreatePass(request):
    if request.method=="POST":
        if request.POST.get("txt_pass")==request.POST.get("txt_confirm"):
            usercount=tbl_user.objects.filter(user_email=request.session["femail"]).count()
            techniciancount=tbl_nurserystaff.objects.filter(nurserystaff_email=request.session["femail"]).count()
            deliverycount=tbl_deliverystaff.objects.filter(deliverystaff_email=request.session["femail"]).count()
            if usercount>0:
                user=tbl_user.objects.get(user_email=request.session["femail"])
                user.user_password=request.POST.get("txt_pass")
                user.save()
                return redirect("WebGuest:Login")
            elif techniciancount>0:
                  technician=tbl_nurserystaff.objects.get(nurserystaff_email=request.session["femail"])
                  technician.nurserystaf_password=request.POST.get("txt_pass")
                  technician.save()
                  return redirect("WebGuest:Login")
            elif deliverycount>0:
                  delivery=tbl_deliverystaff.objects.get(deliverystaff_email=request.session["femail"])
                  delivery.deliverystaff_password=request.POST.get("txt_pass")
                  delivery.save()
                  return redirect("WebGuest:Login")
        else:
            return render(request,"Guest/CreatePassword.html",{'msg':"Passwords not same"})
    else:
        return render(request,"Guest/CreatePassword.html")
