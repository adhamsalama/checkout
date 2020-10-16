from django.core.paginator import Paginator
from django.shortcuts import render
from checkout.models import Category
from django.db.models import Sum

def paginate(items, page_number=1):
    paginator = Paginator(items, 10)
    # pages start at 0, less than zero or more than max page number gives the last page
    page_obj = paginator.get_page(page_number)
    return {"paginator": paginator, "page_obj": page_obj, "items": page_obj.object_list}

def error(request, message):
    return render(request, "checkout/error.html", {"message": message})

def get_categories(user):
    saved = Category.objects.all().order_by("name").distinct()
    cats = []
    for i in saved:
        items = i.item_set.filter(user=user) 
        if len(items) > 0:
            cats.append({"title": i, "count": items.count(), "sum": items.values("price").aggregate(Sum('price'))["price__sum"]})
    return cats