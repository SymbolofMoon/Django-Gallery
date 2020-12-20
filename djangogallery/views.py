from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Image, Category

def this_is_about(request): 
    print("This is about page request")
    return render(request, "about.html")


def show_home_page(request):

    images = Image.objects.all()
    cat = Category.objects.all()
    data = {'images': images, 'cat': cat} 
    print("This is Home page request")
    return render(request, "home.html",data)
    




def show_category_page(request,cid):
  
    print(cid)

    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)
    

    images = Image.objects.filter(cat=category)
    data= {'images':images, 'cats':cats}

    return render(request, "home.html",data)




def home(request):
    return redirect('/home')

    
    
    