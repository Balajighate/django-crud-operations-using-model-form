from django.shortcuts import render, redirect
from .models import Employees


# Create your views here.

def index(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp
    }
    return render(request, 'home.html',context)

def Add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

    emp = Employees(
        name = name,
        email = email,
        address = address,
        phone = phone,
    )
    emp.save()
    return redirect('home')

def Edit(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,

    }
    return redirect("/",context)

def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect("home")
    # return redirect(request, "home.html")


def Delete(request, id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    return redirect("home")

def mysite(request):
    return render(request, 'mysite.html')
