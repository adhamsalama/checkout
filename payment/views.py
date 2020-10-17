from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Payment
from .forms import PaymentForm
from checkout.utils import paginate
import json
from django.db.models import Sum


# Create your views here.

def index(request):
    payments = Payment.objects.filter(user=request.user).order_by("-date", "-id")
    num = request.GET.get("page", 1)
    payments_paginator = paginate(payments, num)
    return render(request, "payment/index.html", 
                {"paginator": payments_paginator["paginator"],
                "page_obj": payments_paginator["page_obj"],
                "payments": payments_paginator["items"],
                "form": PaymentForm(),
                "payments_sum": payments.values("value").aggregate(Sum('value'))["value__sum"] if payments else 0})


def add(request):
    if request.method == "POST":
        form = PaymentForm(json.loads(request.body))
        if form.is_valid():
            payment = Payment(user=request.user,
                            source=form.cleaned_data["source"],
                            value=form.cleaned_data["value"],
                            date=form.cleaned_data["date"])
            payment.save()
            request.user.balance += form.cleaned_data["value"]
            request.user.save()
        return JsonResponse({"message": "Payment added"}, status=201)

def delete(request):
    payment_id = json.loads(request.body)["payment_id"]
    payment = Payment.objects.get(user=request.user, id=payment_id)
    request.user.balance -= payment.value
    payment.delete()
    request.user.save()
    return JsonResponse({"message": "Payment deleted"}, status=201)