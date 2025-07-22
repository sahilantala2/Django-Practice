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
    context = {'recip' : recipies}

    return render(request,'receipe.html',context)
