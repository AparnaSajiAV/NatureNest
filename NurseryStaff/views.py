from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from NurseryStaff.models import *
from User.models import *
from datetime import date
from django.db.models import Sum

# Create your views here.

#homepage
def homepage(request):
    data=tbl_nurserystaff.objects.get(id=request.session["nid"])
    return render(request,"NurseryStaff/HomePage.html",{'data':data})

#profile
def myprofile(request):
    data=tbl_nurserystaff.objects.get(id=request.session["nid"])
    return render(request,"NurseryStaff/MyProfile.html",{'data':data})

#edit profile
def editprofile(request):
    prodata=tbl_nurserystaff.objects.get(id=request.session["nid"])
    if request.method=="POST":
        prodata.nurserystaff_name=request.POST.get('txtname')
        prodata.nurserystaff_contact=request.POST.get('txtcon')
        prodata.nurserystaff_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"NurseryStaff/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"NurseryStaff/EditProfile.html",{'prodata':prodata})

#change password
def changepassword(request):
    if request.method=="POST":
        ccount=tbl_nurserystaff.objects.filter(id=request.session["nid"],nurserystaff_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                nurserystaffdata=tbl_nurserystaff.objects.get(id=request.session["nid"],nurserystaff_password=request.POST.get('txtcurpass'))
                nurserystaffdata.nurserystaff_password=request.POST.get('txtnewpass')
                nurserystaffdata.save()
                return render(request,"NurseryStaff/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"NurseryStaff/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"NurseryStaff/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"NurseryStaff/ChangePassword.html")

#product plant
def productplantInsert(request):
    category=tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        Name=request.POST.get('txtname')
        Des=request.POST.get('txtdes')
        Rate=request.POST.get('txtrate')
        Image=request.FILES.get("fileimg")
        SubcategoryName = tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
        tbl_productplant.objects.create(productplant_name=Name,productplant_description=Des,productplant_rate=Rate,productplant_image=Image,subcategory=SubcategoryName)
        return render(request,"NurseryStaff/ProductPlant.html",{'msg':"Product Added Successfully"})
    else:
        return render(request,"NurseryStaff/ProductPlant.html",{"categorydata":category,"subcategorydata":data})
        
def productplantSelect(request):
    data=tbl_productplant.objects.all()
    for product in data:
        total_stock = tbl_stockplant.objects.filter(productplant=product).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_cart.objects.filter(productplant=product.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        print(total_stock,"stock")
        print(total_cart,"cart")
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        if isinstance(total_stock, int):
            total_stock = total_stock
        else:
            total_stock = 0     
            if isinstance(total_cart, int):
                total_cart = total_cart
            else:
                total_cart = 0
        total=  total_stock-total_cart
        print(total)
        product.total_stock = total
    return render(request,"NurseryStaff/ProductPlantView.html",{"data":data})

def productplantDelete(request,did):
    tbl_productplant.objects.get(id=did).delete()
    #return redirect("NurseryStaff:productplantSelect")
    return render(request,"NurseryStaff/ProductPlantView.html",{"msg":"Plant Removed Successfully"})

def productplantUpdate(request,eid):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    editdata=tbl_productplant.objects.get(id=eid)
    if request.method=="POST":
        editdata.productplant_name=request.POST.get('txtname')
        editdata.productplant_description=request.POST.get('txtdes')
        editdata.productplant_rate=request.POST.get('txtrate')
        editdata.category= tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.subcategory = tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
        editdata.productplant_image=request.FILES.get("fileimg")
        editdata.save()
        #return redirect("NurseryStaff:productplantSelect")
        return render(request,"NurseryStaff/ProductPlantView.html",{"msg":"Plant Updated Successfully"})
    else:
        return render(request,"NurseryStaff/ProductPlant.html",{'editdata':editdata,"categorydata":category,"subcategorydata":subcategory})

#Gallery Plant
def galleryplantInsertSelect(request):
    data=tbl_galleryplant.objects.all()
    category=tbl_category.objects.all()
    if request.method=="POST":
        Image=request.FILES.get("fileimg")
        SubcategoryName = tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
        ProductName = tbl_productplant.objects.get(id=request.POST.get('sel_product'))
        tbl_galleryplant.objects.create(galleryplant_file=Image,product=ProductName,subcategory=SubcategoryName)
        return render(request,"NurseryStaff/ProductPlantGallery.html",{"data":data,'msg':"Plants Gallery Added Successfully"})
    else:
        return render(request,"NurseryStaff/ProductPlantGallery.html",{"data":data,"categorydata":category})

def ajaxsubcategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcat=tbl_subcategory.objects.filter(category=cat)
    return render(request,"NurseryStaff/AjaxSubcategory.html",{"subcategorydata":subcat})

def ajaxproductplant(request):
    subcat = tbl_subcategory.objects.get(id=request.GET.get("did"))
    product=tbl_productplant.objects.filter(subcategory=subcat)
    return render(request,"NurseryStaff/AjaxProductPlant.html",{"productdata":product})

def galleryplantDelete(request,did):
    tbl_galleryplant.objects.get(id=did).delete()
    #return redirect("NurseryStaff:galleryplantInsertSelect")
    return render(request,"NurseryStaff/ProductPlantGallery.html",{'msg':"Plants Gallery Removed Successfully"})

#product pot
def productpotInsert(request):
    type=tbl_typepot.objects.all()
    color=tbl_colorpot.objects.all()
    size=tbl_sizepot.objects.all()
    shape=tbl_shapepot.objects.all()
    material=tbl_materialpot.objects.all()
    if request.method=="POST":
        Name=request.POST.get('txtname')
        Des=request.POST.get('txtdes')
        Rate=request.POST.get('txtrate')
        Image=request.FILES.get("fileimg")
        Type = tbl_typepot.objects.get(id=request.POST.get('sel_type'))
        Color = tbl_colorpot.objects.get(id=request.POST.get('sel_color'))
        Size = tbl_sizepot.objects.get(id=request.POST.get('sel_size'))
        Shape = tbl_shapepot.objects.get(id=request.POST.get('sel_shape'))
        Material = tbl_materialpot.objects.get(id=request.POST.get('sel_material'))
        tbl_productpot.objects.create(productpot_name=Name,productpot_description=Des,productpot_rate=Rate,productpot_image=Image,type=Type,color=Color,size=Size,shape=Shape,material=Material)
        return render(request,"NurseryStaff/ProductPot.html",{'msg':"Product Added Successfully"})
    else:
        return render(request,"NurseryStaff/ProductPot.html",{"type":type,"color":color,"size":size,"shape":shape,"material":material})
    
def productpotSelect(request):
    data=tbl_productpot.objects.all()
    for product in data:
        total_stock = tbl_stockpot.objects.filter(productpot=product).aggregate(total=Sum('stock_quantity'))['total']
        product.productpot_stock = total_stock
    return render(request,"NurseryStaff/ProductPotView.html",{"data":data})

def productpotDelete(request,did):
    tbl_productpot.objects.get(id=did).delete()
    #return redirect("NurseryStaff:productpotSelect")
    return render(request,"NurseryStaff/ProductPotView.html",{"msg":"Planters Removed Successfully"})

def productpotUpdate(request,eid):
    type=tbl_typepot.objects.all()
    color=tbl_colorpot.objects.all()
    size=tbl_sizepot.objects.all()
    shape=tbl_shapepot.objects.all()
    material=tbl_materialpot.objects.all()
    editdata=tbl_productpot.objects.get(id=eid)
    if request.method=="POST":
        editdata.productpot_name=request.POST.get('txtname')
        editdata.productpot_description=request.POST.get('txtdes')
        editdata.productpot_rate=request.POST.get('txtrate')
        editdata.type = tbl_typepot.objects.get(id=request.POST.get('sel_type'))
        editdata.color = tbl_colorpot.objects.get(id=request.POST.get('sel_color'))
        editdata.size = tbl_sizepot.objects.get(id=request.POST.get('sel_size'))
        editdata.shape = tbl_shapepot.objects.get(id=request.POST.get('sel_shape'))
        editdata.material = tbl_materialpot.objects.get(id=request.POST.get('sel_material'))
        editdata.productpot_image=request.FILES.get("fileimg")
        editdata.save()
        #return redirect("NurseryStaff:productpotSelect")
        return render(request,"NurseryStaff/ProductPotView.html",{"msg":"Planters Updated Successfully"})
    else:
        return render(request,"NurseryStaff/ProductPot.html",{'editdata':editdata,"type":type,"color":color,"size":size,"shape":shape,"material":material})

#gallery pot
def gallerypotInsertSelect(request):
    potdata=tbl_productpot.objects.all()
    data=tbl_gallerypot.objects.all()
    if request.method=="POST":
        Image=request.FILES.get("fileimg")
        ProductName = tbl_productpot.objects.get(id=request.POST.get('sel_product'))
        tbl_gallerypot.objects.create(gallerypot_file=Image,product=ProductName)
        return render(request,"NurseryStaff/ProductPotGallery.html",{"data":data,'msg':"Planters Gallery Added Successfully"})
    else:
        return render(request,"NurseryStaff/ProductPotGallery.html",{"data":data,"potdata":potdata})

def gallerypotDelete(request,did):
    tbl_gallerypot.objects.get(id=did).delete()
    #return redirect("NurseryStaff:gallerypotInsertSelect")
    return render(request,"NurseryStaff/ProductPotGallery.html",{"msg":"Planters Gallery Removed Successfully"})

#stock plant
def addplantstock(request,did):
    productplant =  tbl_productplant.objects.get(id=did)
    stock_entry = tbl_stockplant.objects.filter(productplant=productplant).first()
    data = tbl_stockplant.objects.all()
    data=tbl_productplant.objects.all()
    if request.method == "POST":
        date = request.POST.get('txtdate')
        stock_quantity = request.POST.get("txtstock")
        tbl_stockplant.objects.create(stock_date=date,stock_quantity=stock_quantity,productplant=productplant)
        return render(request, "NurseryStaff/PlantStockAdd.html", {'data': data,'msg':"Plants Stock Added"})
    else:
        return render(request, "NurseryStaff/PlantStockAdd.html", {'data': data})

def stockplantSelect(request):
    data1=tbl_stockplant.objects.all()
    return render(request, "NurseryStaff/PlantStockView.html", {'data': data1}) 

def delplantstock(request,did):
    tbl_stockplant.objects.get(id=did).delete()
    #return redirect("NurseryStaff:stockplantSelect")
    return render(request,"NurseryStaff/PlantStockView.html",{"msg":"Plants Stock Removed Successfully"})

#stock pot
def addpotstock(request,did):
    productpot =  tbl_productpot.objects.get(id=did)
    stock_entry = tbl_stockpot.objects.filter(productpot=productpot).first()
    data = tbl_stockpot.objects.all()
    if request.method == "POST":
        date = request.POST.get('txtdate')
        stock_quantity = request.POST.get("txtstock")
        tbl_stockpot.objects.create(stock_date=date,stock_quantity=stock_quantity,productpot=productpot)
        return render(request, "NurseryStaff/PotStockAdd.html", {'data': data,'msg':"Planters Stock Added"})
    else:
        return render(request, "NurseryStaff/PotStockAdd.html", {'data': data})

def stockpotSelect(request):
    data=tbl_stockpot.objects.all()
    return render(request, "NurseryStaff/PotStockView.html", {'data': data}) 

def delpotstock(request,did):
    tbl_stockpot.objects.get(id=did).delete()
    #return redirect("NurseryStaff:stockpotSelect")
    return render(request,"NurseryStaff/PotStockView.html",{"msg":"Planters Stock Removed Successfully"})

#Orders Plant new
def newplantorderSelect(request):
    data=tbl_cart.objects.filter(ship_status=0,cart_status=1)
    return render(request,"NurseryStaff/PlantOrdersNew.html",{'data':data})

#order plant confirm
def inprocessplantorderSelect(request):
    data=tbl_cart.objects.filter(ship_status=1,cart_status=1)
    return render(request,"NurseryStaff/PlantOrdersInprocess.html",{'data':data})

#order plant shipped
def shippedplantorderSelect(request):
    data=tbl_cart.objects.filter(ship_status=2,cart_status=1)
    return render(request,"NurseryStaff/PlantOrdersShipped.html",{'data':data})

#order plant delivered
def deliveredplantorderSelect(request):
    data=tbl_cart.objects.filter(ship_status=3,cart_status=1)
    return render(request,"NurseryStaff/PlantOrdersDelivered.html",{'data':data})

def updateproductbooking(request,bid):
    item = tbl_cart.objects.get(id=bid)
    if item.ship_status == 0:
        item.ship_status = 1  
        item.save()  
        return redirect("NurseryStaff:newplantorderSelect")
    elif item.ship_status == 1:
        item.ship_status = 2  
        item.save()  
        return redirect("NurseryStaff:inprocessplantorderSelect")
    item.save()  
    return redirect("NurseryStaff:newplantorderSelect")

#order pot new
def neworderSelect(request):
    data=tbl_order.objects.filter(order_status="Pending")
    return render(request,"NurseryStaff/PotOrdersNew.html",{'data':data})

#Confirm Assign Orders pot
def confirmassignorderInsert(request,did):
    staff=tbl_deliverystaff.objects.all()
    data=tbl_order.objects.filter(id=did)
    assign=tbl_assigndelivery.objects.get(order=did)
    datas=tbl_order.objects.get(id=did)
    if request.method=="POST":
        datas.order_status="Confirmed"
        datas.save()
        assign.deliverystaff=tbl_deliverystaff.objects.get(id=request.POST.get('sel_staff'))
        assign.assign_date=date.today()
        assign.assign_status=1
        assign.save()
        return redirect("NurseryStaff:neworderSelect")
    else:
        return render(request,"NurseryStaff/PotOrdersAssign.html",{'data':data,'staff':staff})

#confirmedorderview pot
def inprocessorderSelect(request):
    assign=tbl_assigndelivery.objects.filter(assign_status=1)
    return render(request,"NurseryStaff/PotOrdersConfirmed.html",{'assign':assign})

#order pot shipped
def shippedorderSelect(request):
    assign=tbl_assigndelivery.objects.all()
    return render(request,"NurseryStaff/PotOrdersShipped.html",{'assign':assign})

#DeliveredOrders
def deliveredorderSelect(request):
    assign=tbl_assigndelivery.objects.filter(order=tbl_order.objects.get(order_status="Delivered"))
    return render(request,"NurseryStaff/PotOrdersDelivered.html",{'assign':assign})

#logout
def logoutview(request):
    if 'nid' in request.session:
        del request.session['nid']
        return redirect('WebGuest:Login')
    else:
        return redirect('WebGuest:Login')


