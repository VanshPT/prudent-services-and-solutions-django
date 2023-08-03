
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index,name="PssappIndex"),
    path("about/", views.about,name="AboutUs"),
    path("training/", views.training,name="Training"),
    path("ourstrength/", views.ourstrength,name="Ourstrength"),
    path("welfare/", views.welfare,name="Welfare"),
    path("contact/", views.contact,name="ContactUs"),
    path("emplogin/", views.emplogin,name="Emplogin"),
    # path("thankyou/", views.thankyou,name="thankyou")
]