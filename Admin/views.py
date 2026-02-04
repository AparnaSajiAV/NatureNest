from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import date

# Create your views here.

#Homepage
def homepageLoarding(request):
    admin=tbl_admin.objects.get(id=request.session["aid"])
    return render(request,"Admin/HomePage.html",{'admin':admin})

#profile
def myprofile(request):
    data=tbl_admin.objects.get(id=request.session["aid"])
    return render(request,"Admin/MyProfile.html",{'data':data})

#edit profile
def editprofile(request):
    prodata=tbl_admin.objects.get(id=request.session["aid"])
    if request.method=="POST":
        prodata.admin_name=request.POST.get('txtname')
        prodata.admin_contact=request.POST.get('txtcon')
        prodata.admin_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Admin/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Admin/EditProfile.html",{'prodata':prodata})

#change password
def changepassword(request):
    if request.method=="POST":
        ccount=tbl_admin.objects.filter(id=request.session["aid"],admin_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                admindata=tbl_admin.objects.get(id=request.session["aid"],admin_password=request.POST.get('txtcurpass'))
                admindata.admin_password=request.POST.get('txtnewpass')
                admindata.save()
                return render(request,"Admin/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Admin/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Admin/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Admin/ChangePassword.html")

#District
def districtInsertSelect(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtdistrict')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Admin/District.html",{'data':data,'msg':"District Added Successfully"})
    else:
        return render(request,"Admin/District.html",{'data':data})

def districtDelete(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,"Admin/District.html",{'msg':"District Removed Successfully"})
    #return redirect("WebAdmin:districtInsertSelect")

def districtUpdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtdistrict")
        editdata.save()
        return render(request,"Admin/District.html",{'msg':"District Updated Successfully"})
       # return redirect("WebAdmin:districtInsertSelect")
    else:
        return render(request,"Admin/District.html",{"editdata":editdata})

#Place
def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Admin/Place.html",{'data':data,'msg':"Place Added Successfully"})
    else:
        return render(request,"Admin/Place.html",{'data':data,"districtdata":district})

def placeDelete(request,did):
    tbl_place.objects.get(id=did).delete()
    return render(request,"Admin/Place.html",{'msg':"Place Removed Successfully"})
    #return redirect("WebAdmin:placeInsertSelect")

def placeUpdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return render(request,"Admin/Place.html",{'msg':"Place Updated Successfully"})
        #return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"Admin/Place.html",{"editdata":editdata,"districtdata":district})

#Category Plant 
def categoryInsertSelect(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        cateName=request.POST.get('txtcategory')
        tbl_category.objects.create(category_name=cateName)
        return render(request,"Admin/Category.html",{'data':data,'msg':"Category Added Successfully"})
    else:
        return render(request,"Admin/Category.html",{'data':data})

def categoryDelete(request,did):
    tbl_category.objects.get(id=did).delete()
    #return redirect("WebAdmin:categoryInsertSelect")
    return render(request,"Admin/Category.html",{'msg':"Category Removed Successfully"})

def categoryUpdate(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtcategory")
        editdata.save()
        #return redirect("WebAdmin:categoryInsertSelect")
        return render(request,"Admin/Category.html",{'msg':"Category Updated Successfully"})
    else:
        return render(request,"Admin/Category.html",{"editdata":editdata})

#Subcategory
def subcategoryInsertSelect(request):
    category=tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcat=request.POST.get('txtsubcategory')
        Category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=subcat,category=Category)
        return render(request,"Admin/Subcategory.html",{'data':data,'msg':"Subcategory Added Successfully"})
    else:
        return render(request,"Admin/Subcategory.html",{'data':data,"category":category})

def subcategoryDelete(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    #return redirect("WebAdmin:subcategoryInsertSelect")
    return render(request,"Admin/Subcategory.html",{'msg':"subcategory Removed Successfully"})

def subcategoryUpdate(request,eid):
    category=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.subcategory_name=request.POST.get("txtsubcategory")
        editdata.category = tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.save()
        #return redirect("WebAdmin:subcategoryInsertSelect")
        return render(request,"Admin/Subcategory.html",{'msg':"Subcategory Updated Successfully"})
    else:
        return render(request,"Admin/Subcategory.html",{"editdata":editdata,"category":category})

#Pot Type
def typepotInsertSelect(request):
    data=tbl_typepot.objects.all()
    if request.method=="POST":
        typeName=request.POST.get('txttype')
        tbl_typepot.objects.create(type_name=typeName)
        return render(request,"Admin/PotType.html",{'data':data,'msg':"Type Added Successfully"})
    else:
        return render(request,"Admin/PotType.html",{'data':data})

def typepotDelete(request,did):
    tbl_typepot.objects.get(id=did).delete()
    #return redirect("WebAdmin:typepotInsertSelect")
    return render(request,"Admin/PotType.html",{'msg':"Planters Type Removed Successfully"})

def typepotUpdate(request,eid):
    editdata=tbl_typepot.objects.get(id=eid)
    if request.method=="POST":
        editdata.type_name=request.POST.get("txttype")
        editdata.save()
        #return redirect("WebAdmin:typepotInsertSelect")
        return render(request,"Admin/PotType.html",{'msg':"Planters Type Updated Successfully"})
    else:
        return render(request,"Admin/PotType.html",{"editdata":editdata})

#Pot Shape
def shapepotInsertSelect(request):
    data=tbl_shapepot.objects.all()
    if request.method=="POST":
        ShapeName=request.POST.get('txtshape')
        tbl_shapepot.objects.create(shape_name=ShapeName)
        return render(request,"Admin/PotShape.html",{'data':data,'msg':"Shape Added Successfully"})
    else:
        return render(request,"Admin/PotShape.html",{'data':data})

def shapepotDelete(request,did):
    tbl_shapepot.objects.get(id=did).delete()
    #return redirect("WebAdmin:shapepotInsertSelect")
    return render(request,"Admin/PotShape.html",{'msg':"Planters Shape Removed Successfully"})

def shapepotUpdate(request,eid):
    editdata=tbl_shapepot.objects.get(id=eid)
    if request.method=="POST":
        editdata.shape_name=request.POST.get("txtshape")
        editdata.save()
        #return redirect("WebAdmin:shapepotInsertSelect")
        return render(request,"Admin/PotShape.html",{'msg':"Planters Shape Updated Successfully"})
    else:
        return render(request,"Admin/PotShape.html",{"editdata":editdata})

#pot material
def materialpotInsertSelect(request):
    data=tbl_materialpot.objects.all()
    if request.method=="POST":
        MaterialName=request.POST.get('txtmaterial')
        tbl_materialpot.objects.create(material_name=MaterialName)
        return render(request,"Admin/PotMaterial.html",{'data':data,'msg':"Material Added Successfully"})
    else:
        return render(request,"Admin/PotMaterial.html",{'data':data})

def materialpotDelete(request,did):
    tbl_materialpot.objects.get(id=did).delete()
    #return redirect("WebAdmin:materialpotInsertSelect")
    return render(request,"Admin/PotMaterial.html",{'msg':"Planters Material Removed Successfully"})

def materialpotUpdate(request,eid):
    editdata=tbl_materialpot.objects.get(id=eid)
    if request.method=="POST":
        editdata.material_name=request.POST.get("txtmaterial")
        editdata.save()
        #return redirect("WebAdmin:materialpotInsertSelect")
        return render(request,"Admin/PotMaterial.html",{'msg':"Planters Material Updated Successfully"})
    else:
        return render(request,"Admin/PotMaterial.html",{"editdata":editdata})

#pot size
def sizepotInsertSelect(request):
    data=tbl_sizepot.objects.all()
    if request.method=="POST":
        SizeName=request.POST.get('txtsize')
        tbl_sizepot.objects.create(size_name=SizeName)
        return render(request,"Admin/PotSize.html",{'data':data,'msg':"Size Added Successfully"})
    else:
        return render(request,"Admin/PotSize.html",{'data':data})

def sizepotDelete(request,did):
    tbl_sizepot.objects.get(id=did).delete()
    #return redirect("WebAdmin:sizepotInsertSelect")
    return render(request,"Admin/PotSize.html",{'msg':"Planters Size Removed Successfully"})

def sizepotUpdate(request,eid):
    editdata=tbl_sizepot.objects.get(id=eid)
    if request.method=="POST":
        editdata.size_name=request.POST.get("txtsize")
        editdata.save()
        #return redirect("WebAdmin:sizepotInsertSelect")
        return render(request,"Admin/PotSize.html",{'msg':"Planters Size Updated Successfully"})
    else:
        return render(request,"Admin/PotSize.html",{"editdata":editdata})

#pot color
def colorpotInsertSelect(request):
    data=tbl_colorpot.objects.all()
    if request.method=="POST":
        ColorName=request.POST.get('txtcolor')
        tbl_colorpot.objects.create(color_name=ColorName)
        return render(request,"Admin/PotColor.html",{'data':data,'msg':"Color Added Successfully"})
    else:
        return render(request,"Admin/PotColor.html",{'data':data})

def colorpotDelete(request,did):
    tbl_colorpot.objects.get(id=did).delete()
    #return redirect("WebAdmin:colorpotInsertSelect")
    return render(request,"Admin/PotColor.html",{'msg':"Planters Color Removed Successfully"})

def colorpotUpdate(request,eid):
    editdata=tbl_colorpot.objects.get(id=eid)
    if request.method=="POST":
        editdata.color_name=request.POST.get("txtcolor")
        editdata.save()
        #return redirect("WebAdmin:colorpotInsertSelect")
        return render(request,"Admin/PotColor.html",{'msg':"Planters Color Updated Successfully"})
    else:
        return render(request,"Admin/PotColor.html",{"editdata":editdata})

#userlist
def userlist(request):
    data=tbl_user.objects.all()
    return render(request,"Admin/UserList.html",{'data':data})

#Admin Reg
def adminInsert(request):
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        photo=request.FILES.get("fileimg")
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd,admin_photo=photo)
        return render(request,"Admin/AdminRegistration.html",{'msg':"Registered Successfully"})
    else:
        return render(request,"Admin/AdminRegistration.html")

def adminSelect(request):
    data=tbl_admin.objects.all()
    return render(request,"Admin/AdminList.html",{'data':data})

def adminDelete(request,did):
    tbl_admin.objects.get(id=did).delete()
    #return redirect(reverse("WebAdmin:adminSelect"))
    return render(request,"Admin/AdminList.html",{"msg":"Admin Removed Successfully"})

def adminUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.admin_photo=request.FILES.get("fileimg")
        editdata.save()
        #return redirect("WebAdmin:adminSelect")
        return render(request,"Admin/AdminList.html",{"msg":"Admin Updated Successfully"})
    else:
        return render(request,"Admin/AdminRegistration.html",{"editdata":editdata})

#Nursery Staff
def nurserystaffInsert(request):
    data=tbl_nurserystaff.objects.all()
    if request.method=="POST":
        Name=request.POST.get('txtname')
        Gender=request.POST.get('txtgender')
        Contact=request.POST.get('txtcontact')
        Email=request.POST.get('txtemail')
        Password=request.POST.get('txtpwd')
        Photo=request.FILES.get("fileimg")
        tbl_nurserystaff.objects.create(nurserystaff_name=Name,nurserystaff_gender=Gender,nurserystaff_contact=Contact,nurserystaff_email=Email,nurserystaff_password=Password,nurserystaff_photo=Photo)
        return render(request,"Admin/NurseryStaffReg.html",{'msg':"Registered Successfully"})
    else:
        return render(request,"Admin/NurseryStaffReg.html")
    
def nurserystaffSelect(request):
    data=tbl_nurserystaff.objects.all()
    return render(request,"Admin/NurseryStaffList.html",{'data':data})

def nurserystaffDelete(request,did):
    tbl_nurserystaff.objects.get(id=did).delete()
    #return redirect("WebAdmin:nurserystaffSelect")
    return render(request,"Admin/NurseryStaffList.html",{'msg':"Nursery Staff Removed Successfully"})

def nurserystaffUpdate(request,eid):
    editdata=tbl_nurserystaff.objects.get(id=eid)
    if request.method=="POST":
        editdata.nurserystaff_name=request.POST.get('txtname')
        editdata.nurserystaff_gender=request.POST.get('txtgender')
        editdata.nurserystaff_contact=request.POST.get('txtcontact')
        editdata.nurserystaff_email=request.POST.get('txtemail')
        editdata.nurserystaff_password=request.POST.get('txtpwd')
        editdata.nurserystaff_photo=request.FILES.get("fileimg")
        editdata.save()
        #return redirect("WebAdmin:nurserystaffSelect")
        return render(request,"Admin/NurseryStaffList.html",{'msg':"Nursery Staff Updated Successfully"})
    else:
        return render(request,"Admin/NurseryStaffReg.html",{'editdata':editdata})

#Delivery Staff
def deliverystaffInsert(request):
    data=tbl_deliverystaff.objects.all()
    if request.method=="POST":
        Name=request.POST.get('txtname')
        Gender=request.POST.get('txtgender')
        Contact=request.POST.get('txtcontact')
        Email=request.POST.get('txtemail')
        Password=request.POST.get('txtpwd')
        photo=request.FILES.get("fileimg")
        tbl_deliverystaff.objects.create(deliverystaff_name=Name,deliverystaff_gender=Gender,deliverystaff_contact=Contact,deliverystaff_email=Email,deliverystaff_password=Password,deliverystaff_photo=photo)
        return render(request,"Admin/DeliveryStaffReg.html",{'msg':"Registered Successfully"})
    else:
        return render(request,"Admin/DeliveryStaffReg.html")

def deliverystaffSelect(request):
    data=tbl_deliverystaff.objects.all()
    return render(request,"Admin/DeliveryStaffList.html",{'data':data})

def deliverystaffDelete(request,did):
    tbl_deliverystaff.objects.get(id=did).delete()
    #return redirect("WebAdmin:deliverystaffSelect")
    return render(request,"Admin/DeliveryStaffList.html",{'msg':"Delivery Staff Removed Successfully"})

def deliverystaffUpdate(request,eid):
    editdata=tbl_deliverystaff.objects.get(id=eid)
    if request.method=="POST":
        editdata.deliverystaff_name=request.POST.get('txtname')
        editdata.deliverystaff_gender=request.POST.get('txtgender')
        editdata.deliverystaff_contact=request.POST.get('txtcontact')
        editdata.deliverystaff_email=request.POST.get('txtemail')
        editdata.deliverystaff_password=request.POST.get('txtpwd')
        editdata.save()
        #return redirect("WebAdmin:deliverystaffSelect")
        return render(request,"Admin/DeliveryStaffList.html",{'msg':"Delivery Staff Updated Successfully"})
    else:
        return render(request,"Admin/DeliveryStaffReg.html",{'editdata':editdata})
    
#Complaint
def complaintSelect(request):
    userdata=tbl_user.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"Admin/ComplaintNew.html",{'data':data})
    

def complaintreplayInsert(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        #return redirect("WebAdmin:complaintSelect")
        return render(request,"Admin/ComplaintReply.html",{'msg':"Complaint Replied Successfully"})
    else:
        return render(request,"Admin/ComplaintReply.html",{'complaint':complaint})

def complaintsolvedSelect(request):
    userdata=tbl_user.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"Admin/ComplaintSolved.html",{'data':data})

#logout
def logoutview(request):
    if 'aid' in request.session:
        del request.session['aid']
        return redirect('WebGuest:Login')
    else:
        return redirect('WebGuest:Login')

#plant sales report
def plantsReportSelect(request):
    data=tbl_productbooking.objects.all()
    if request.method=="POST":
        fromdate=request.POST.get("txtfromdate")
        todate=request.POST.get("txttodate")
        data=tbl_productbooking.objects.filter(booking_date__gte=fromdate,booking_date__lte=todate)
        return render(request,"Admin/PlantsReport.html",{'data':data})
    else:
        return render(request,"Admin/PlantsReport.html",{'data':data}) 

def plantsdetails(request,cid):
    data=tbl_cart.objects.filter(booking_id=cid)
    return render(request,"Admin/PlantsDetails.html",{"data":data})   

#planters sales report
def plantersReportSelect(request):
    data=tbl_order.objects.all()
    if request.method=="POST":
        fromdate=request.POST.get("txtfromdate")
        todate=request.POST.get("txttodate")
        data=tbl_order.objects.filter(order_date__gte=fromdate,order_date__lte=todate)
        return render(request,"Admin/PlantersReport.html",{'data':data})
    else:
        return render(request,"Admin/PlantersReport.html",{'data':data})    

def plantersdetails(request,pid):
    data=tbl_order.objects.filter(id=pid)
    return render(request,"Admin/PlantsDetails.html",{"data":data})

#Review
def ReviewSelect(request):
    data=tbl_review.objects.all()
    return render(request,"Admin/ReviewView.html",{"data":data})

