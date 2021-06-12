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
    path ("Hotels", views.hotel, name= 'hotel'),
    path ("plan_payment", views.plan_payment, name="plan_payment"),
    path ("plan_payment/plan_invoice", views.plan_invoice, name="plan_invoice"),
]
urlpatterns += staticfiles_urlpatterns()
