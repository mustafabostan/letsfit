from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import Customer
from .forms import customerForm

# customer_list = [
#     {
#         "id":1,
#         "name":"Mustafa",
#         "surname":"Bostan",
#         "phonenumber":"5555"
#     },
#     {
#         "id":2,
#         "name":"Halil",
#         "surname":"Kılıç",
#         "phonenumber":"5555"
#     },
#     {
#         "id":3,
#         "name":"Test",
#         "surname":"Test",
#         "phonenumber":"5555"
#     },
# ]


def index(request):
    return render(request, "LetsfitAuto/index.html")

def customers(request):
    # database = {
    #     "uyeler":customer_list,
    # }
    context = {
        "customers" : Customer.objects.all()
    }
    if request.method == "POST":
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()            
    form = customerForm()            
    return render(request, "LetsfitAuto/customers.html",{"form" : form} | context)
    

    

def products(request):
    return render(request, "LetsfitAuto/products.html")


# def new_customer(request):
#     if request.method == "POST":
#         name = request.POST["name"]
#         surname = request.POST["surname"]
#         phonenumber = request.POST["phonenumber"]
#     return render(request,"LetsfitAuto/partials/_addcustomer.html",{
#         "name" : name,
#         "surname" : surname,
#         "phonenumber" : phonenumber
#     })


