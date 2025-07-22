from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def show(req):

    peoples = [
        {
            'name' : 'john','age' : 52
        },
        {
            'name': 'Lucy', 'age': 12
        },
        {
            'name': 'Peter', 'age': 43
        },
    ]

    return render(req,"index.html",context={'peoples' : peoples})

def contact(req):

    name_title = "Contact"

    return render(req,"contact.html",context={"name" : name_title })