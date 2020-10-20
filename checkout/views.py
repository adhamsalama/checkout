from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django import forms
from .models import User, Item, Category
from .forms import ItemForm
from .utils import paginate, error, get_categories
import json
from django.db.models import Q, Sum


# Create your views here.

@login_required
def index(request):
    if not request.user.is_authenticated:
        return render(request, "checkout/login.html")
    items = Item.objects.filter(user=request.user).order_by("-date", "-id")
    num = request.GET.get("page", 1)
    items_paginator = paginate(items, num)
    return render(request, "checkout/index.html", 
                {"paginator": items_paginator["paginator"],
                "page_obj": items_paginator["page_obj"],
                "items": items_paginator["items"],
                "categories": get_categories(request.user),
                "items_count": items.count(),
                "items_sum": items.aggregate(Sum("price"))["price__sum"] if items else 0,
                "form": ItemForm()})

@login_required
def create_item(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, "checkout/new_item.html", {"form": form})

    data = json.loads(request.body)
    form = ItemForm(data)
    if form.is_valid():
        category = data["category"]
        if not category:
            category = "None"
        item_instance = form.save(commit=False)
        category, created = Category.objects.get_or_create(name=category.lower())
        item_instance.category = category
        item_instance.user = request.user
        request.user.balance -= float(form.cleaned_data["price"])
        item_instance.save()
        request.user.save()
        #messages.success(request, "Item created successfully.")
        #return HttpResponseRedirect(reverse("checkout:view_item", kwargs={"item_id": item_instance.id}))
        return JsonResponse({"message": "Item created successfully"}, status=201)
    else:
        #print(form.cleaned_data)
        return JsonResponse({"message": "Error"})

@login_required
def edit_item(request, item_id):
    if request.method == "GET":
        try:
            item = Item.objects.get(id=item_id, user=request.user)
            form = ItemForm(instance=item, initial={"category": item.category})
            return render(request, "checkout/edit_item_form.html", {"form": form, "item_id": item_id})
        except:
            return error(request, "Item not found.")
    else:
        form = ItemForm(request.POST)
        item = Item.objects.get(id=item_id, user=request.user)
        old_price = item.price
        item.name = form.data["name"]
        item.price = form.data["price"]
        item.quantity = form.data["quantity"]
        item.date = form.data["date"]
        item.comment = form.data["comment"]
        if not request.POST["category"]:
            category = "None"
        else:
            category = request.POST["category"]
        c, created = Category.objects.get_or_create(name=category.lower())
        item.category = c
        request.user.balance += old_price - float(item.price)
        item.save()
        request.user.save()
        return JsonResponse({"message": "Item updated"}, status=201)
    
@login_required
def delete_item(request):
    item_id = json.loads(request.body)["item_id"]
    try:
        item = Item.objects.get(id=item_id, user=request.user)
        request.user.balance += item.price
        request.user.save()
        item.delete()
        return JsonResponse({"message": "Item deleted"}, status=201)
    except:
        return JsonResponse({"message": "Error"})

@login_required
def update_balance(request):
    new_balance = json.loads(request.body)["new_balance"]
    request.user.balance = new_balance
    request.user.save()
    return JsonResponse({"message": "Balance updated."}, status=201)

@login_required
def profile(request):
    return render(request, "checkout/profile.html")

@login_required
def search(request):
    q = request.GET.get("q", None)
    if q is None:
        return error(request, "Query not provided")
    try:
        category = Category.objects.get(name=q.lower())
    except:
        category = None
    results = request.user.items.filter(Q(name__contains=q)
                                |Q(price__contains=q)
                                |Q(quantity__contains=q)
                                |Q(seller__contains=q)
                                |Q(category=category)
                                |Q(comment__contains=q)
                                |Q(date__contains=q)).order_by("-date")
    num = request.GET.get("page", 1)
    items_paginator = paginate(results, num)
    return render(request, "checkout/paginator.html", 
                {"paginator": items_paginator["paginator"],
                "page_obj": items_paginator["page_obj"],
                "items": items_paginator["items"]})

@login_required
def category(request, name):
    try:
        cat = Category.objects.get(name=name.lower())
    except:
        return error(request, "Category doesn't exist.")
    items = cat.item_set.filter(user=request.user)
    num = request.GET.get("page", 1)
    items_paginator = paginate(items, num)
    return render(request, "checkout/index.html", 
                {"paginator": items_paginator["paginator"],
                "page_obj": items_paginator["page_obj"],
                "items": items_paginator["items"],
                "categories": get_categories(request.user),
                "items_count": request.user.items.count(),
                "items_sum": request.user.items.aggregate(Sum("price"))["price__sum"] if items else 0})

@login_required
def change_password(request):
    old_password = request.POST["old_password"]
    new_password = request.POST["new_password"]
    if request.user.check_password(old_password):
        request.user.set_password(new_password)
        request.user.save()
        login(request, request.user)
        messages.success(request, "Password updated successfully.")
        #return render(request, "checkout/profile.html")
        return HttpResponseRedirect(reverse("checkout:profile"))
    else:
        return error(request, "Wrong password. Please try again.")
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("checkout:index"))
        else:
            return render(request, "checkout/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "checkout/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("checkout:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "checkout/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, balance=request.POST["balance"])
            user.save()
        except IntegrityError:
            return render(request, "checkout/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("checkout:index"))
    else:
        return render(request, "checkout/register.html")
