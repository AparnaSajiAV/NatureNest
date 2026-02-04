from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from NurseryStaff.models import *
from Guest.views import *
from django.db.models import Sum
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse

# Create your views here.

#homepage
def homepage(request):
    return render(request,"User/HomePage.html")

#profile
def myprofile(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

#edit profile
def editprofile(request):
    district=tbl_district.objects.all()
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.user_address=request.POST.get('txtaddress')
        prodata.district= tbl_district.objects.get(id=request.POST.get('sel_district'))
        prodata.place= tbl_place.objects.get(id=request.POST.get('sel_place'))
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata,"districtdata":district})

#change password
def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")

#Plant Product View
def productplantSelect(request):
    data = tbl_productplant.objects.all()
    categorys = tbl_category.objects.all()
    subcategory = tbl_subcategory.objects.all()
    
    ar=[1,2,3,4,5]
    avg_list = []  
    reviewcount = 0

    for product in data:
        total_stock = tbl_stockplant.objects.filter(productplant=product).aggregate(total=Sum('stock_quantity'))['total']
        product.stock = total_stock if isinstance(total_stock, int) else 0
    for c in data:
        reviewcount = tbl_review.objects.filter(productplant=c.id).count()
        print(reviewcount)
        res = 0
        avg = 0
        review = tbl_review.objects.filter(productplant=c.id)
        for rev in review:
            res = res + rev.user_rating
            # print(res)
            avg = res//reviewcount
            # print(avg)
        avg_list.append(avg)
        print(avg_list)
        cdata = zip(data,avg_list)
        #return render(request, "User/ViewProductPlant.html", {"Data": cdata,"avg": avg_list,"ar":ar})
    if request.method == "POST":
        category_id = request.POST.get('sel_category')
        subcategory_id = request.POST.get('sel_subcategory')

        if subcategory_id:  # If a subcategory is selected
            subcategory = tbl_subcategory.objects.get(id=subcategory_id)
            data = tbl_productplant.objects.filter(subcategory=subcategory)
        elif category_id:  # If only category is selected
            category = tbl_category.objects.get(id=category_id)
            data = tbl_productplant.objects.filter(subcategory__category=category)
        for c in data:
            reviewcount = tbl_review.objects.filter(product=c.id).count()
        
        if data.exists():
            return render(request, "User/ViewProductPlant.html", {"data": data})
        else:
            messages.info(request, "Products not found!")
            return render(request, "User/ViewProductPlant.html", { "data": data,"categorydata": category})
        
    else:
        return render(request, "User/ViewProductPlant.html", {"data": cdata, "categorydata": categorys,"Data": cdata,"avg": avg_list,"ar":ar})
        
#galleryplant View
def galleryplantSelect(request,did):
    data=tbl_productplant.objects.filter(id=did)
    gallery=tbl_galleryplant.objects.filter(product=did)
    return render(request,"User/GalleryPlant.html",{"data":data,"gallery":gallery})

#complaint
def complaintInsert(request):
    if request.method=="POST":
        Title=request.POST.get('txttitle')
        Content=request.POST.get('txtdetails')
        User=tbl_user.objects.get(id=request.session["uid"])
        tbl_complaint.objects.create(complaint_title=Title,complaint_details=Content,user=User)
        return render(request,"User/ComplaintPost.html")
    else:
        return render(request,"User/ComplaintPost.html")

def complaintSelect(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    return render(request,"User/ComplaintView.html",{"data":data})

def complaintDelete(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:complaintSelect")
    
#Plant Product View
def productpotSelect(request):
    data=tbl_productpot.objects.all()
    type=tbl_typepot.objects.all()
    color=tbl_colorpot.objects.all()
    size=tbl_sizepot.objects.all()
    shape=tbl_shapepot.objects.all()
    material=tbl_materialpot.objects.all()
    ar=[1,2,3,4,5]
    avg_list = []  
    reviewcount = 0
    for c in data:
        reviewcount = tbl_review.objects.filter(productpot=c.id).count()
        # print(reviewcount)
        res = 0
        avg = 0
        review = tbl_review.objects.filter(productpot=c.id)
        for rev in review:
            res = res + rev.user_rating
            # print(res)
            avg = res//reviewcount
            # print("avg",avg)
        avg_list.append(avg)
        # print(avg_list)
        cdata = zip(data,avg_list)
    # print(avg_list)
    if request.method=="POST":
        if ((request.POST.get('sel_type')!="") and (request.POST.get('sel_color')!="") and (request.POST.get('sel_size')) and (request.POST.get('sel_shape'))) and (request.POST.get('sel_material')):
            Type = tbl_typepot.objects.get(id=request.POST.get('sel_type'))
            Color = tbl_colorpot.objects.get(id=request.POST.get('sel_color'))
            Size = tbl_sizepot.objects.get(id=request.POST.get('sel_size'))
            Shape = tbl_shapepot.objects.get(id=request.POST.get('sel_shape'))
            Material = tbl_materialpot.objects.get(id=request.POST.get('sel_material'))
            data=tbl_productpot.objects.filter(shape=Shape,size=Size,color=Color,material=Material,type=Type)
            for c in data:
                reviewcount = tbl_review.objects.filter(productpot=c.id).count()
                # print(reviewcount)
                res = 0
                avg = 0
                review = tbl_review.objects.filter(productpot=c.id)
                for rev in review:
                    res = res + rev.user_rating
                    # print(res)
                    avg = res//reviewcount
                    # print("avg",avg)
                avg_list.append(avg)
                # print(avg_list)
                cdata = zip(data,avg_list)
        return render(request,"User/ViewProductPot.html",{"data":cdata})
    else:
        return render(request,"User/ViewProductPot.html",{"data":cdata,"type":type,"color":color,"size":size,"shape":shape,"material":material,"avg": avg_list,"ar":ar})

#gallerypot View
def gallerypotSelect(request,did):
    data=tbl_productpot.objects.filter(id=did)
    gallery=tbl_gallerypot.objects.filter(product=did)
    return render(request,"User/GalleryPot.html",{"data":data,"gallery":gallery})

#wishlistpot
def wishlistpotInsert(request,did):
    User=tbl_user.objects.get(id=request.session["uid"])
    potid=tbl_productpot.objects.get(id=did)
    data=tbl_wishlistpot.objects.filter(productpot=potid,user=User).count()
    if data>0:
        return render(request,"User/ViewProductPot.html",{'msg':"Already Added"}) 
    else:
        tbl_wishlistpot.objects.create(productpot=potid,user=User)
        return render(request,"User/ViewProductPot.html",{'msg':"Product Added Successfully"}) 
    return redirect("User:productpotSelect")

#wishlistViewPot
def wishlistpotSelect(request):
    data=tbl_wishlistpot.objects.filter(user=request.session["uid"])
    return render(request,"User/WishlistPot.html",{'data':data})

def wishlistpotDelete(request,tid):
    tbl_wishlistpot.objects.get(id=tid).delete()
    #return redirect("User:wishlistpotSelect")
    return render(request,"User/WishlistPot.html",{'msg':"Product Removed Successfully"}) 

#wishlistplant
def wishlistplantInsert(request,tid):
    User=tbl_user.objects.get(id=request.session["uid"])
    plantid=tbl_productplant.objects.get(id=tid)
    data=tbl_wishlistplant.objects.filter(user=User,productplant=plantid).count()
    if data>0:
        return render(request,"User/ViewProductPlant.html",{'msg':"Already Added"}) 
    else:
        tbl_wishlistplant.objects.create(user=User,productplant=plantid)
        return render(request,"User/ViewProductPlant.html",{'msg':"Product Added Successfully"}) 
    return redirect("User:productplantSelect")

#wishlistViewPlant
def wishlistplantSelect(request):
    data=tbl_wishlistplant.objects.filter(user=request.session["uid"])
    return render(request,"User/WishlistPlant.html",{'data':data})

def wishlistplantDelete(request,tid):
    tbl_wishlistplant.objects.get(id=tid).delete()
    #return redirect("User:wishlistplantSelect")
    return render(request,"User/WishlistPlant.html",{'msg':"Product Removed Successfully"}) 

#orderplant
def productbook(request,did):
    product=tbl_productplant.objects.get(id=did)
    user=tbl_user.objects.get(id=request.session["uid"])
    count = tbl_productbooking.objects.filter(user=user,booking_status=0).count()
    if count > 0:
        bcount=tbl_productbooking.objects.get(user=user,booking_status=0)
        icount=tbl_cart.objects.filter(productplant=product,booking=bcount).count()
        if icount > 0:
           return render(request,"User/ViewProductPlant.html",{'msg':"Already Added"}) 
        else:
            tbl_cart.objects.create(booking=bcount,productplant=product,cart_qty=1)
            return render(request,"User/ViewProductPlant.html",{'msg':"Added to Cart"})
    else:
        tbl_productbooking.objects.create(user=user)
        count = tbl_productbooking.objects.filter(user=user,booking_status=0).count()
        if count > 0:
            bcount=tbl_productbooking.objects.get(user=user,booking_status=0)
            icount=tbl_cart.objects.filter(productplant=product,booking=bcount).count()
            if icount > 0:
                return render(request,"User/ViewProductPlant.html",{'msg':"Already Added"}) 
            else:
                tbl_cart.objects.create(booking=bcount,productplant=product,cart_qty=1)
                return render(request,"User/ViewProductPlant.html",{'msg':"Added to Cart"})

#cart plant order
def mycartSelect(request):
    if request.method=="POST":
        bookingdata=tbl_productbooking.objects.get(id=request.session["bookingid"])
        cart=tbl_cart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status=1
            i.save()
        bookingdata.price=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("User:payment")
    else:
        customerdata=tbl_user.objects.get(id=request.session["uid"])
        bcount=tbl_productbooking.objects.filter(user=customerdata,booking_status=0).count()
        if bcount>0:
            book=tbl_productbooking.objects.get(user=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_productbooking.objects.get(id=bid)
            cartdata=tbl_cart.objects.filter(booking=bkid)
            data=[]
            for product in cartdata:
                total_stock = tbl_stockplant.objects.filter(productplant=product.productplant_id).aggregate(total=Sum('stock_quantity'))['total']
                total_cart = tbl_cart.objects.filter(productplant=product.productplant_id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                if isinstance(total_stock, int):
                     total_stock = total_stock
                else:
                    total_stock = 0
                    
                if isinstance(total_cart, int):
                    total_cart = total_cart
                else:
                    total_cart = 0
                total=  total_stock-total_cart
                print (total)
                print("stock",total_stock)
                print("cart",total_cart)
                product.stock = total
                pro_data={
                    'id':product.id,
                    'cartproduct': product,
                    'stock':total,
                }
                data.append(pro_data)
            
            return render(request,"User/MyPlantCart.html",{'data':data})
        else:
            return render(request,"User/MyPlantCart.html")    

def cartDelete(request,did):
   tbl_cart.objects.get(id=did).delete()
   #return redirect("User:mycartSelect")
   return render(request,"User/MyPlantCart.html",{'msg':"Removed from Cart"})

def cartqtySelect(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:mycartSelect")

def productplantdeliverySelect(request):
    if request.method=="POST":
        return redirect("User:payment")
    else:
        return render(request,"User/PlantDeliveryDetails.html")

def payment(request):
    if request.method=="POST":
        bookingdata=tbl_productbooking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_status=2
        bookingdata.save()
        return redirect("User:Billing")
    else: 
        return render(request,"User/Payment.html")

def Billing(request):
    billno = random.randint(10000, 99999)
    today = datetime.now().strftime("%d-%m-%Y")
    newuser= tbl_user.objects.get(id=request.session["uid"])   
    latest_booking = tbl_productbooking.objects.filter(user=newuser, booking_status=2).latest('booking_date')    
    data = tbl_cart.objects.filter(booking=latest_booking)
    total=latest_booking.price
    return render(request,"User/Bill.html",{'billno':billno,'today':today,'userdata':newuser,'data':data,'total':total})

def productplantorderSelect(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    data1 = tbl_productbooking.objects.filter(user=user)
    data = tbl_cart.objects.filter(booking__in=data1)
    return render(request, "User\PlantOrdersView.html",{"data":data})

#order pot
def productorderInsert(request,did):
    district=tbl_district.objects.all()
    data=tbl_productpot.objects.filter(id=did)
    if request.method=="POST":
        potid=tbl_productpot.objects.get(id=did)
        qty=int(request.POST.get('qty'))
        pot_rate = int(potid.productpot_rate)
        amount = qty * pot_rate
        User=tbl_user.objects.get(id=request.session["uid"])
        order=tbl_order.objects.create(productpot=potid,order_qty=qty,user=User,order_amount=amount)
        return redirect("User:paymentpot")
    else:
        return render(request,"User/PotOrder.html",{'data':data,"districtdata":district})

def paymentpot(request):
    if request.method=="POST":
        return redirect("User:Billingpot")
    else: 
        return render(request,"User/Payment.html")

def Billingpot(request):
    billno = random.randint(10000, 99999)
    today = datetime.now().strftime("%d-%m-%Y")
    newuser= tbl_user.objects.get(id=request.session["uid"])   
    latest_booking = tbl_productbooking.objects.filter(user=newuser, booking_status=2).latest('booking_date')    
    data = tbl_cart.objects.filter(booking=latest_booking)
    total=latest_booking.price
    return render(request,"User/Bill.html",{'billno':billno,'today':today,'userdata':newuser,'data':data,'total':total})
    
def productorderSelect(request):
    data=tbl_order.objects.filter(user=request.session["uid"])

    return render(request,"User/PotOrderView.html",{'data':data})

def productdeliverySelect(request,did):
    data=tbl_order.objects.filter(user=request.session["uid"],id=did)
    return render(request,"User/PlantDeliveryDetails.html",{'data':data})

#logout
def logout_view(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('WebGuest:Login')
    else:
        return redirect('WebGuest:Login')

#cancel plant order
def cancelplantorder(request,cid):
    data=tbl_cart.objects.get(id=cid) 
    data.cart_status=2
    data.save()
    return render(request,"User/PlantOrdersView.html")

#Plants Review and rating
def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    wdata=tbl_cart.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_review.objects.filter(productplant=wdata.productplant_id).count()
    if counts>0:
        res=0
        stardata=tbl_review.objects.filter(productplant=wdata.productplant_id).order_by('-review_datetime')
        for i in stardata:
            res=res+i.user_rating
        avg=res//counts
        return render(request,"User/PlantsRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/PlantsRating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_cart.objects.get(id=workid)
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=rating_data,productplant=tbl_productplant.objects.get(id=wdata.productplant_id))
    stardata=tbl_review.objects.filter(productplant=wdata.productplant_id).order_by('-review_datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    cdata = tbl_cart.objects.get(id=request.GET.get("pdt"))
    rate = tbl_review.objects.filter(productplant=cdata.productplant_id)
    for i in rate:
        if int(i.user_rating) == 5:
            five = five + 1
        elif int(i.user_rating) == 4:
            four = four + 1
        elif int(i.user_rating) == 3:
            three = three + 1
        elif int(i.user_rating) == 2:
            two = two + 1
        elif int(i.user_rating) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + int(i.user_rating)
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)

#Pots Review and rating
def potsrating(request,rid):
    parray=[1,2,3,4,5]
    mid=rid
    wdata=tbl_order.objects.get(id=rid)
    
    counts=0
    counts=stardata=tbl_review.objects.filter(productpot=wdata.productpot_id).count()
    if counts>0:
        res=0
        stardata=tbl_review.objects.filter(productpot=wdata.productpot_id).order_by('-review_datetime')
        for i in stardata:
            res=res+i.user_rating
        avg=res//counts
        return render(request,"User/PotsRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/PotsRating.html",{'mid':mid})

def ajaxpotstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    workid=request.GET.get('workid')
    wdata=tbl_order.objects.get(id=workid)
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=rating_data,productpot=tbl_productpot.objects.get(id=wdata.productpot_id))
    stardata=tbl_review.objects.filter(productpot=wdata.productpot_id).order_by('-review_datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def potsstarrating(request):
    r_len = 0
    five = four = three = two = one = 0
    cdata = tbl_order.objects.get(id=request.GET.get("pdt"))
    rate = tbl_review.objects.filter(productpot=cdata.productpot_id)
    for i in rate:
        if int(i.user_rating) == 5:
            five = five + 1
        elif int(i.user_rating) == 4:
            four = four + 1
        elif int(i.user_rating) == 3:
            three = three + 1
        elif int(i.user_rating) == 2:
            two = two + 1
        elif int(i.user_rating) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        r_len = r_len + int(i.user_rating)
    rlen = r_len // 5
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":rlen}
    return JsonResponse(result)