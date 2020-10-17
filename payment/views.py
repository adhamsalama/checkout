from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Payment
from .forms import PaymentForm

# Create your views here.

def index(request):
    payments = Payment.objects.filter(user=request.user).order_by("-date", "-id")
    return render(request, "payment/index.html", {"payments": payments, "form": PaymentForm()})

def add(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment(user=request.user,
                            source=form.cleaned_data["source"],
                            value=form.cleaned_data["value"],
                            date=form.cleaned_data["date"])
            payment.save()
            request.user.balance += form.cleaned_data["value"]
            request.user.save()
            print("saved")
        return HttpResponseRedirect(reverse("payment:index"))