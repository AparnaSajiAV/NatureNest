from django.contrib import admin
from django.urls import path,include
from User import views

app_name="User"
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

    #View Products Plant
    path('ProductPlantView/',views.productplantSelect,name="productplantSelect"),
    #galleryplant view
    path('GalleryPlantView/<int:did>',views.galleryplantSelect,name="galleryplantSelect"),

    #pot view
    path('ProductPotView/',views.productpotSelect,name="productpotSelect"),
    #gallerypot view
    path('GalleryPotView/<int:did>',views.gallerypotSelect,name="gallerypotSelect"),

    #wishlist
    path('WishlisPot/<int:did>',views.wishlistpotInsert,name="wishlistpotInsert"),
    path('WishlistPotView/',views.wishlistpotSelect,name="wishlistpotSelect"),
    path('WishlistPotDelete/<int:tid>',views.wishlistpotDelete,name="wishlistpotDelete"),
    path('WishlistPlant/<int:tid>',views.wishlistplantInsert,name="wishlistplantInsert"),
    path('WishlistPlantView/',views.wishlistplantSelect,name="wishlistplantSelect"),
    path('WishlistPlantDelete/<int:tid>',views.wishlistplantDelete,name="wishlistplantDelete"),

    #order pots
    path('BuyProduct/<int:did>',views.productorderInsert,name="productorderInsert"), 
    path('BuyProductView/',views.productorderSelect,name="productorderSelect"), 
    path('DeliveryDetails/<int:did>',views.productdeliverySelect,name="productdeliverySelect"),
    path('Payments/',views.paymentpot,name="paymentpot"),
    path('Invoices/',views.Billingpot,name="Billingpot"),

    #order plant view
    path('ProductOrder/<int:did>',views.productbook,name="productbook"),
    path('MyPlantCart/',views.mycartSelect,name="mycartSelect"),
    path('DelCart/<int:did>',views.cartDelete,name="cartDelete"),
    path('CartQty/',views.cartqtySelect,name="cartqtySelect"),
    path('DeliveryDetails/',views.productplantdeliverySelect,name="productplantdeliverySelect"),
    path('Payment/',views.payment,name="payment"),
    path('Invoice/',views.Billing,name="Billing"),
    path('MyPlantOrders/',views.productplantorderSelect,name="productplantorderSelect"), 
    path('CancelOrders/<int:cid>',views.cancelplantorder,name="cancelplantorder"),
    
    #Complaint
    path('Complaint/',views.complaintInsert,name="complaintInsert"),
    path('ComplaintView/',views.complaintSelect,name="complaintSelect"),
    path('ComplaintDelete/<int:did>',views.complaintDelete,name="complaintDelete"),
    
    #Plants review
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    #Pots review
    path('PotsRating/<int:rid>',views.potsrating,name="potsrating"),  
    path('ajaxpotstar/',views.ajaxpotstar,name="ajaxpotstar"),
    path('Potsstarrating/',views.potsstarrating,name="potsstarrating"),

    #logout
    path('Logout/',views.logout_view,name="logout_view"),
]

#<a href="{% url 'User:complaintInsert' %}">Complaint</a><br>