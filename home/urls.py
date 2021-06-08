from django.urls import path
from . import views
from .views import index,reservation,contact,blog,about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',index, name= 'index'),
    path ("Reservation/<choice_1>/<choice_2>/",views.reservation,name= 'reservation'),
    path ("Contact",contact,name= 'contact'),
    path ("Blog",blog,name= 'blog'),
    path ("About",about,name= 'about'),
    # path ("check",views.check, name="check"),
    path ("Reservation/Payment", views.payment, name= 'payment'),
    path ("Reservation/Payment/invoice", views.invoice, name='invoice'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]
urlpatterns += staticfiles_urlpatterns()
