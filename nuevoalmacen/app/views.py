from itertools import product
from django.forms import modelform_factory
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from app.models import Product
from app.forms import ProductForm

# Create your views here.
def home(request):
    return render(request, "index.html")


# Product functions
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
    try:
        product = get_object_or_404(Product, pk=id)
    except Product.DoesNotExist:
        raise Http404("El producto no existe")
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
    try:
        product = get_object_or_404(Product, pk=id)

        if request.method == "POST":
            formaProduct = ProductForm(request.POST, instance=product)
            if formaProduct.is_valid():
                formaProduct.save()
                return redirect("products")

            else:
                return render(
                    request,
                    "products/edit-product.html",
                    {"formaProduct": formaProduct},
                )
        else:
            formaProduct = ProductForm(instance=product)

    except Product.DoesNotExist:
        raise Http404("El producto no existe")

    return render(request, "products/edit-product.html", {"formaProduct": formaProduct})


def deleteProduct(id):
    try:
        product = get_object_or_404(Product, pk=id)
        if product:
            product.delete()

        return redirect("products")
    except Product.DoesNotExist:
        raise Http404("El producto no existe")


# Transaction functions
def transactions(request):
    return render(request, "transactions/transactions.html")


def transactionDetail(request, id):
    return render(request, "transactions/transaction-detail.html")


def newTransaction(request):
    return render(request, "transactions/new-transaction.html")


def editTransaction(request, id):
    return render(request, "transactions/edit-transaction.html")


def deleteTransaction(id):
    pass
