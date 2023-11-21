from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# pss/pssapp/urls.py
from . import views

urlpatterns = [
    path("", views.index, name="PssappIndex"),
    path("about/", views.about, name="AboutUs"),
    path("ourprocesses/", views.ourprocesses, name="OurProcesses"),
    path("valuedpartners/", views.valuedpartners, name="ValuedPartners"),
    path("contact/", views.contact, name="ContactUs"),
    path("getback/", views.getback, name="Getback"),
    path("careers/", views.careers, name="Careers"),
    path("jobapplication/", views.jobseeker, name="JobApplication"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)