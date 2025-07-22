from http.client import HTTPResponse

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from .models import *

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')
        recepie_image = request.FILES.get('recepie_image')

        Receipe.objects.create(
            recepie_name = recepie_name,
            recepie_description = recepie_description,
            recepie_image = recepie_image
        )

        return  redirect('/receipes/')

    recipies = Receipe.objects.all()

    if request.GET.get('search'):
        recipies = recipies.filter(recepie_name__icontains = request.GET.get('search'))

    context = {'recip' : recipies}
    return render(request,'receipe.html',context)


def delete_rece(request,id):

    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')

def update_rece(request,id):

    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')
        recepie_image = request.FILES.get('recepie_image')

        queryset.recepie_name = recepie_name
        queryset.recepie_description = recepie_description

        if recepie_image:
            queryset.recepie_image = recepie_image

        queryset.save()

        return redirect('/receipes/')
    context = {'rec':queryset}


    return render(request,'update_reci.html',context)

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            user_name = user_name
        )

        user.set_password(password)
        user.save()

    return render(request,'register.html')