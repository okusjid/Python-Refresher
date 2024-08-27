from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
def jan1(request):
    return HttpResponse("This Works!")

monthy_challenge = {
        "jan": "Eat no meat for the entire month",
        "feb": "Walk for at least 20 minutes every day",
        "mar": "Learn Django for at least 20 minutes every day",
        "apr": "Eat no meat for the entire month",
        "may": "Walk for at least 20 minutes every day",
        "jun": "Learn Django for at least 20 minutes every day",
        "jul": "Eat no meat for the entire month",
        "aug": "Walk for at least 20 minutes every day",
        "sep": "Learn Django for at least 20 minutes every day",
        "oct": "Eat no meat for the entire month",
        "nov": "Walk for at least 20 minutes every day",
        "dec": "Learn Django for at least 20 minutes every day",
    }

def monthy_challenges(request, month):
    try:
        challenge_text = monthy_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenge_by_number(request, month):
    months = list(monthy_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    return HttpResponseRedirect(redirect_month)