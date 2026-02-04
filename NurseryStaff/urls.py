from django.contrib import admin
from django.urls import path,include
from NurseryStaff import views

app_name="NurseryStaff"
urlpatterns = [
    path('admin/', admin.site.urls),

    #homepage
    path('HomePage/',views.homepage,name="homepage"),

    #Profile
    path('MyProfile/',views.myprofile,name="myprofile"),
    
    #edit profile
    path('EditProfile/',views.editprofile,name="editprofile"),

    #change password
    path('ChangePassword/',views.changepassword,name="changepassword"),

    #Plant product
    path('ProductPlant/',views.productplantInsert,name="productplantInsert"),
    path('ProductPlantList/',views.productplantSelect,name="productplantSelect"),
    path('ProductPlantDelete/<int:did>',views.productplantDelete,name="productplantDelete"),
    path('ProductPlantUpdate/<int:eid>',views.productplantUpdate,name="productplantUpdate"),

    #Gallery Plant
    path('GalleryPlant/',views.galleryplantInsertSelect,name="galleryplantInsertSelect"),
    path('AjaxSubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
    path('AjaxProductPlant/',views.ajaxproductplant,name="ajaxproductplant"),
    path('GalleryPlantDelete/<int:did>',views.galleryplantDelete,name="galleryplantDelete"),

    #Pot product
    path('ProductPot/',views.productpotInsert,name="productpotInsert"),
    path('ProductPotList/',views.productpotSelect,name="productpotSelect"),
    path('ProductPotDelete/<int:did>',views.productpotDelete,name="productpotDelete"),
    path('ProductPotUpdate/<int:eid>',views.productpotUpdate,name="productpotUpdate"),
 
    #Gallery Pot
    path('GalleryPot/',views.gallerypotInsertSelect,name="gallerypotInsertSelect"),
    path('GalleryPotDelete/<int:did>',views.gallerypotDelete,name="gallerypotDelete"),

    #stock Plants
    path('AddPlantStock/<int:did>', views.addplantstock,name="addplantstock"),
    path('delPlantstock/<int:did>', views.delplantstock,name="delplantstock"),
    path('StockPlantView/', views.stockplantSelect,name="stockplantSelect"),

    #stock Pots
    path('Addstock/<int:did>', views.addpotstock,name="addpotstock"),
    path('delstock/<int:did>', views.delpotstock,name="delpotstock"),
    path('StockView/', views.stockpotSelect,name="stockpotSelect"),

    #orde pots
    path('NewPotOrders/',views.neworderSelect,name="neworderSelect"), 
    path('ConfirmAssignPotOrders/<int:did>',views.confirmassignorderInsert,name="confirmassignorderInsert"), 
    path('InprocessPotOrdersView/',views.inprocessorderSelect,name="inprocessorderSelect"), 
    path('ShippedPotOrdersView/',views.shippedorderSelect,name="shippedorderSelect"), 
    path('DeliveredPotOrdersView/',views.deliveredorderSelect,name="deliveredorderSelect"), 

    #Orders Plant
    path('NewPlantOrders/',views.newplantorderSelect,name="newplantorderSelect"), 
    path('InprocessPlantOrdersView/',views.inprocessplantorderSelect,name="inprocessplantorderSelect"), 
    path('ShippedPlantOrdersView/',views.shippedplantorderSelect,name="shippedplantorderSelect"), 
    path('DeliveredPlantOrdersView/',views.deliveredplantorderSelect,name="deliveredplantorderSelect"),
    path('UpdateStatus/<int:bid>',views.updateproductbooking,name="updateproductbooking"),
    

    #logout
    path('Logout/',views.logoutview,name="logoutview"),
]