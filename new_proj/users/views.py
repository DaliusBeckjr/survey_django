from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    print("Got Post Info..............")
    # print(request.POST)
    first_name_from_form = request.POST['first_name']
    last_name_from_form = request.POST['last_name']
    location_from_form = request.POST['location']
    fav_lang_from_form = request.POST['fav_lang']
    comment_from_form = request.POST['comment']
    context = {
        "first_name" : first_name_from_form,
        "last_name" : last_name_from_form,
        "location" : location_from_form,
        "fav_lang" : fav_lang_from_form,
        "comment" : comment_from_form
    }

    return render(request, 'show.html', context)

