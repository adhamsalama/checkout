from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist
from .forms import WishlistForm
import json
from checkout.utils import paginate

# Create your views here.

def index(request):
    items = request.user.wishlist.order_by("-date")
    num = request.GET.get("page", 1)
    items_paginator = paginate(items, num)
    return render(request, "wishlist/index.html", 
                {"paginator": items_paginator["paginator"],
                "page_obj": items_paginator["page_obj"],
                "items": items_paginator["items"]})


@csrf_exempt
def get_form(request):
    form = WishlistForm()
    return render(request, "wishlist/form.html", {"form": form})


def add_wishlist(request):
    data = json.loads(request.body)
    form = WishlistForm(data)
    if form.is_valid():
        item = Wishlist(user=request.user,
                        name=form.cleaned_data["name"],
                        price=form.cleaned_data["price"],
                        link=form.cleaned_data["link"])
        item.save()
        return JsonResponse({"message": "Wishlist item created successfully."}, status=201)
    return JsonResponse({"message": "Invalid form submission."})


def delete_wishlist(request):
    item_id = json.loads(request.body)["item_id"]
    try:
        item = Wishlist.objects.get(id=item_id, user=request.user)
        item.delete()
        return JsonResponse({"message": "Wishlist item deleted"}, status=201)
    except:
        return JsonResponse({"message": "Error."})