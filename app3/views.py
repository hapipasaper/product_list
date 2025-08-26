from django.shortcuts import render
from .models import Product

def product_list(request):
    qs = Product.objects.all()

    category = request.GET.get('category')
    if category:
        qs = qs.filter(category=category)

    ordering = request.GET.get('order')  # مثال: ?order=-price
    if ordering:
        qs = qs.order_by(ordering)

    return render(request, 'app3/products.html', {'products':qs})
