from itertools import product
from django.forms import modelform_factory
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.core.serializers.json import DjangoJSONEncoder


from app.models import Product, Transaction, TransactionProduct
from app.forms import ProductForm

import json

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


def deleteProduct(request, id):

    try:
        product = get_object_or_404(Product, pk=id)
        if product:
            product.delete()

        return redirect("products")
    except Product.DoesNotExist:
        raise Http404("El producto no existe")


# Transaction functions
class TransactionsIndexView(generic.ListView):
    template_name = "transactions/transactions.html"
    context_object_name = "transactions"

    def get_queryset(self):
        """Return the list of transactions"""
        return Transaction.objects.order_by("id")


class TransactionDetail(generic.DetailView):
    model = (
        Transaction,
        TransactionProduct,
    )
    template_name = "transactions/transaction-details.html"


def transactionDetail(request, id):
    products_ids = []
    products = []
    try:
        transaction = get_object_or_404(Transaction, pk=id)
        transaction_product_id = TransactionProduct.objects.filter(
            transaction_id=transaction
        ).values()

        for id_product in transaction_product_id:
            products_ids.append(id_product["product_id"])

        for i in products_ids:
            products.append(Product.objects.filter(id=i).values()[0])

    except Transaction.DoesNotExist:
        raise Http404("La venta no existe")
    return render(
        request,
        "transactions/transaction-details.html",
        {"transaction": transaction, "products": products},
    )


def newTransaction(request):
    return render(request, "transactions/new-transaction.html")


def editTransaction(request, id):
    return render(request, "transactions/edit-transaction.html")


def deleteTransaction(id):
    pass
