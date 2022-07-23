from itertools import product
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from app.models import Product
from app.forms import ProductForm

# Create your views here.
def home(request):
    return render(request, "index.html")


def products(request):
    no_products = Product.objects.count()
    # products = Product.objects.all()
    products = Product.objects.order_by("id")
    return render(
        request,
        "products/products.html",
        {"no_products": no_products, "products": products},
    )


def productDetail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product-details.html", {"product": product})


def newProduct(request):
    if request.method == "POST":
        formaProduct = ProductForm(request.POST)
        if formaProduct.is_valid():
            formaProduct.save()
            return redirect("index")

        else:
            return render(
                request, "products/new-product.html", {"formaProduct": formaProduct}
            )
    else:
        formaProduct = ProductForm()

    return render(request, "products/new-product.html", {"formaProduct": formaProduct})


def editProduct(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        formaProduct = ProductForm(request.POST, instance=product)
        if formaProduct.is_valid():
            formaProduct.save()
            return redirect("products")

        else:
            return render(
                request, "products/edit-product.html", {"formaProduct": formaProduct}
            )
    else:
        formaProduct = ProductForm(instance=product)

    return render(request, "products/edit-product.html", {"formaProduct": formaProduct})


def deleteProduct(request, id):
    product = get_object_or_404(Product, pk=id)

    if product:
        product.delete()

    return redirect("products")
