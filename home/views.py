from django.shortcuts import render
from .models import Chambre,Catalogue,Testimonial, Choice, Invoice
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

import random

# Create your views here.
choice_2_2 = ""
name = ""
phone = ""
email = ""
checkin_date = ""
checkout_date = ""
adults = ""
children = ""
street_1 = ""
street_2 = ""
city = ""
state = ""
zip = ""
country = ""

def index (request):
    chambres= Chambre.objects.all()
    catalogues= Catalogue.objects.all()
    testimonials = Testimonial.objects.all()
    render(request,'index.html',{'testimonial': testimonials})
    render (request,'index.html',{'catalogues': catalogues})
    return render(request,"index.html",{'chambres': chambres})

def reservation (request, choice_1, choice_2):
    choice_1
    choice_2
    print(choice_1)
    print(choice_2)
    global choice_2_2
    choice_2_2 = choice_2

    choice = Choice()
    choice.name = choice_1
    choice.price = choice_2
    choices = [choice]
    # return HttpResponse('<h1>This is {}</h1>'.format(choice_2))
    return render(request, "reservation.html", {'choices' : choices})

def contact(request):
    return  render (request, "contact.html")
def blog (request):
    chambres = Chambre.objects.all()
    return render (request, "blog.html",{'chambres': chambres})
def about(request):
    return render (request, "about.html")
def payment(request):
    if request.method == 'POST':
        global name
        name = request.POST.get('name')
        print(type(name))
        global phone
        phone = request.POST.get('phone')
        print(type(phone))
        global email 
        email = request.POST.get('email')
        print(type(email))
        global checkin_date
        checkin_date = request.POST.get('checkin_date')
        print(type(checkin_date))
        global checkout_date
        checkout_date = request.POST.get('checkout_date')
        print(type(checkout_date))
        global adults
        adults = request.POST.get('adults')
        print(type(adults))
        global children
        children = request.POST.get('children')
        print(type(children))
        global street_1
        street_1 = request.POST.get('street_1')
        print(type(street_1))
        global street_2
        street_2 = request.POST.get('street_2')
        print(type(street_2))
        global city
        city = request.POST.get('city')
        print(type(city))
        global state
        state = request.POST.get('state')
        print(type(state)) 
        global zip
        zip = request.POST.get('zip')
        print(type(zip))
        global country
        country = request.POST.get('country')
        print(type(country))
    return render(request, "payment.html")

def invoice(request):
    invoice = Invoice()
    print("In Invoices")
    invoice.t_id = random.randint(1000000000, 9999999999)
    print(random.randint(1000000000, 9999999999))
    invoice.price = choice_2_2 
    print(choice_2_2)
    invoice.name = name
    print(name)
    invoice.email = email
    print(email)
    invoice.phone = phone
    print(phone)
    invoice.address = street_1 + " " + street_2
    print(street_1 + " " + street_2)
    invoice.guests = str(int(adults) + int(children))
    print(str(int(adults) + int(children)))
    invoice.duration = str(int(checkout_date[:1]) - int(checkin_date[:1]))
    print(str(int(checkout_date[:1]) - int(checkin_date[:1])))
    invoices = [invoice]
    return render(request, "invoice.html", {"invoices" : invoices})
    # return HttpResponse("Output")

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

data = {
	"company": "Akaash Travels",
	"address": str(street_1 + " " + street_2),
	"city": str(city),
	"state": str(state),
	"zipcode": str(zip),


	"phone": str(phone),
	"email": str(email),
	"website": "akaashtravelshotels.com",
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response