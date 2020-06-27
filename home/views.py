# Create your views here.
from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from home.models import Contact,ProductView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from math import ceil


def index(request):

    return render(request,'index.html')
    messages.success(request,"this is a test message")
    #return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")
def contact(request):
    if request.method == "POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        phone= request.POST.get("phone")
        desc= request.POST.get("desc")
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is saved')
    
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
def login(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request,'userpage.html')
        else:
            return render(request,'login.html')
            
            # No backend authenticated the credentials
    

    return render(request,'login.html')
    # u: soham1, samir120802

def logout(request):
    logout(request)

    return render(request,'login.html')

def userpage(request):
    if request.user.isanonymous:
        return render(request,'login.html')
    else:
        return render(request,'userpage.html')

def shop(request):
    products=ProductView.objects.all()
    print(products)
    #n=len(products)
    #print(n)
    #nslides=n//4 + ceil(n/4 - n//4)
    #print(nslides)
    #params= {'no of slides': nslides, 'range':range(1,nslides),'product':products }
    #note through params we sent a single dictionery for creating just 1 slider

   #allprod=[[products,range(1,nslides),nslides],
    #         [products,range(1,nslides),nslides]]
    # note this was just to copy the same slider multiple times
    allprod=[]
    catprod=ProductView.objects.values('pcategory','id')
    cat={item['pcategory'] for item in catprod}
    for cat1 in cat:
        prod=ProductView.objects.filter( pcategory = cat1)
        n=len(prod)
        nslides=n//4 + ceil(n/4 - n//4)
        allprod.append([prod,range(1,nslides), nslides]) 
    params={'allprod':allprod}
    return render(request, 'shop_index2.html',params)

def prodview(request,id):
    #to fetch products using id
    product=ProductView.objects.filter(id=id)
    print(product)
    return render(request, 'shop_prodpage.html',{'product': product[0]})
    #note product is passing as a list and 1 item would be present for 1 product for sure
    #note it fetches all description of the particular icecream

