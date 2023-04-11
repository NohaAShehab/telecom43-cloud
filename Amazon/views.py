from django.shortcuts import render, reverse , redirect
from django.http import  HttpResponse
# Create your views here.
from Amazon.models import Product
from Amazon.forms import  ProductModelForm

""" any view function must return with HTTP Response """
def helloworld(request):  # request --> hold information about your request
    return HttpResponse("Hello world from django ")


def homepage(request):
    return HttpResponse("<h1 style='color:red'>Welcome to Amazon page </h1>")


def homeuser(request, username):
    return HttpResponse(f"<h1> Welcome to your homepage {username}</h1>")


def returndatatypes(request):
    d = {"name":"Ahmed", 'track':"telecom" }
    # return HttpResponse(['Ahmed', 'Ali'])
    return HttpResponse(d)


def userid(request , id):
    return HttpResponse(f"Welcome user  {id}")


def profile(request):
    info={
        "name":"Salma",
        "track": 'Telecom'
    }

    students = ['Salma','Aisha', 'Israa', 'Basant', 'Samir', 'Basma', 'Zeyad']
    return render(request, 'profile.html', context={"myinfo": info, 'students':students})

###################################################
products= [
        {"id":1, 'name':'product1', 'price':1000, 'image':'pic1.png'},
        {"id": 2, 'name': 'product2', 'price': 2000, 'image':'pic2.png'},
        {"id": 3, 'name': 'product3', 'price': 3000, 'image':'pic3.png'},
        {"id": 4, 'name': 'product4', 'price': 4000, 'image':'pic4.png'},
    ]

def allproducts(request):
    return render(request, 'products.html', context={"products":products})

def showproduct(request, id):
    for product in products:
        if product["id"]==id:
            return render(request, 'amazon/showproduct.html',

                          context={'name':product['name'], 'price':product['price'],
                                   'image':product['image']})

    return HttpResponse("Product not found")


def productIndexDB(request):

    allproducts = Product.objects.all()
    # print(allproducts)
    # return HttpResponse("Connected to databases")
    return render(request, 'amazon/products/index.html', context={"products":allproducts})

def productShowDB(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'amazon/products/show.html', context={"product":product})

def productDeleteDB(request, id):
    product = Product.get_product(id)
    res= product.delete_product()
    # if res:
    #     return HttpResponse("Product deleted successfully")
    index_url = reverse('db.products.index')
    return redirect(index_url)


def create_product(request):

    ## get method
    if request.method=="GET":
        myform = ProductModelForm()
        return render(request, 'amazon/products/create.html', context={"form":myform})
    else:
        saveForm = ProductModelForm(request.POST, request.FILES)
        if saveForm.is_valid():
            saveForm.save()
        # return HttpResponse("Data received")
        url= reverse('db.products.index')
        return redirect(url)




def edit_product(request, id):
    product = Product.get_product(id)
    ## get method
    if request.method=="GET":
        myform = ProductModelForm(instance=product)
        return render(request, 'amazon/products/edit.html', context={"form":myform})
    else:
        saveForm = ProductModelForm(request.POST, request.FILES, instance=product)
        if saveForm.is_valid():
            saveForm.save()
        # return HttpResponse("Data received")
        url= reverse('db.products.index')
        return redirect(url)
