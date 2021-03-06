# Create your views here.
from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from home.models import Contact,ProductView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

def comingnext(request):
    return render(request,'comingnext.html')
def ulogin(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            #this creates the user"s id
            #return render(request,'userpage.html')
            return redirect("/userpage")
        else:
            return render(request,'login.html')


            # No backend authenticated the credentials


    return render(request,'login.html')
    # u: soham1, samir120802

def checkout(request):
    return render(request,'shop_checkout.html')



def logout(request):
    logout(request)

    return render(request,'login.html')

def userpage(request):
    if request.user.is_anonymous:
        #return render(request,'login.html')
        return redirect("/login")

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
        # dont know why harry kept it range(1, nslides)
    params={'allprod':allprod}
    return render(request, 'shop_index2.html',params)

def prodview(request,id):
    #to fetch products using id
    product=ProductView.objects.filter(id=id)
    print(product)
    return render(request, 'shop_prodpage.html',{'product': product[0]})
    #note product is passing as a list and 1 item would be present for 1 product for sure
    #note it fetches all description of the particular icecream


def searchmatch(query, item):
        if str(query).lower() in str(item.pdesc).lower() or str(query).lower() in str(item.pname).lower() or str(query).lower() in str(item.pcategory).lower() or str(query).lower() in str(item.psubcategory).lower():
            return True
        else:
            return False


def search(request):
    query = request.GET.get('search')
    #products=ProductView.objects.all()
    allprod=[]
    catprod=ProductView.objects.values('pcategory','id')
    cat={item['pcategory'] for item in catprod}
    for cat1 in cat:
        prodall=ProductView.objects.filter( pcategory = cat1)
        prod = [item for item in prodall if searchmatch(query, item)]
        n=len(prod)
        print(n)
        nslides=n//4 + ceil(n/4 - n//4)
        if len(prod) != 0:
            allprod.append([prod,range(1,nslides), nslides])
    params={'allprod':allprod,"msg" : ""}

    if len(allprod)==0:
        params = {'msg':"Your Item is not available"}
    print(allprod)


    return render(request, 'shop_searchpage.html',params)
