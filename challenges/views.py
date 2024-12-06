from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string
 
# Create your views here.
monthly_challenges = {
    "january": "Walk atleast 10,000 steps daily",
    "february": "Wakeup around 6am!",
    "march": "Eat Healthy",
    "april": "do your own research",
    "may": "Walk atleast 10,000 steps daily",
    "june": "Wakeup around 6am!",
    "july": "Eat Healthy",
    "august": "do your own research",
    "september": "Walk atleast 10,000 steps daily",
    "october":  "Wakeup around 6am!",
    "november": "Eat Healthy",
    "december": "do your own research & Walk atleast 10,000 steps daily"
}

def index(request):
     list_items = ""
     months = list(monthly_challenges.keys())
    
     for month in months:
        month_path = reverse("month-challenge", args = [month]) #path redirect to /challenges/month
        list_items += f"<li><a href=\"{month_path}\"> {month.capitalize()}</a></li>"
     #above code create <li><a href= "-----">January</a></li>

     response_data = f"<ul>{list_items}</ul>"
     return HttpResponse(response_data)


def monthly_challenge_by_month(request, month):
        months = list(monthly_challenges.keys())

        if month > len(months):
            return HttpResponseNotFound("Invalid month!")
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args= [redirect_month])  #/challenges/month(specified month)
        return HttpResponseRedirect(redirect_path)


    


def monthly_challenge(request, month):
        try:
            challenge_text = monthly_challenges[month]
            months = list(monthly_challenges.keys())
            # render fun needs first arg request, second arg template path & third arg is dict with key value pair
            return render(request,"challenges/challenge.html", {
                 "text": challenge_text,
                 "month_name": month.capitalize()
            })    
           
        except:
            return HttpResponseNotFound("<h1>Not a valid month!</h1>")
        
