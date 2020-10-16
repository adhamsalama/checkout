from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
import json
from datetime import datetime
from .utils import plot_barchart, dict_max_value_index

# Create your views here.

def index(request):
    if request.method == "GET":
        # get data for current month and year and show it by default
        data = get_data(request)
        images = json.loads(data.content)
        return render(request, "dashboard/index.html", {"images": images, "today": datetime.now().strftime("%Y-%m-%d")})

def get_data(request):
    try:
        date = request.GET["date"]
        month = int(date[5:7])
        year = int(date[:4])
        day = int(date[8:])
        date_obj = datetime(year=year, month=month, day=day)
    except:
        date_obj = datetime.now()
        month = date_obj.month
        year = date_obj.year
        day = date_obj.day
    items = request.user.items.filter(date__year=year).order_by("-date")
    days = {}
    # "0": 0 is to make Jan on line value 1 instead of 0
    months = {"0": 0, "Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, "Nov": 0, "Dec": 0}
    # fill days dictionary keys with 0 to 31 and all values with 0 
    for i in range(0, 32):
        days[i] = 0
    
    for item in items:
        if item.date.strftime("%m") == date_obj.strftime("%m"):
            day = int(item.date.strftime("%d"))
            days[day] += item.price
        month = item.date.strftime("%b")
        months[month] += item.price
    max_days = dict_max_value_index(days)
    max_month = dict_max_value_index(months)

    month_img = plot_barchart(days,
                        title=f"Money spent in {date_obj.strftime('%B')} for year {year}",
                        xlabel="Day",
                        ylabel="Money Spent",
                        xmin=1,
                        highlight=date_obj.day,
                        highest_value=max_days)
    year_img = plot_barchart(months,
                        title=f"Money spent per month in {year}",
                        xlabel="Month",
                        ylabel="Money Spent",
                        xmin=1,
                        highlight=date_obj.month,
                        highest_value=max_month)
    return JsonResponse({"month_img": month_img, "year_img": year_img})

