from django.contrib import admin

from .models import Category
from .models import Suppler
from .models import Product
from .models import Customer
from .models import Transaction
from .models import TransactionProduct


admin.site.register(Category)
admin.site.register(Suppler)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(TransactionProduct)


