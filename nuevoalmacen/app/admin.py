from django.contrib import admin

from .models import Category
from .models import Suppler
from .models import Product
from .models import Customer
from .models import Transaction
from .models import TransactionProduct
from .models import Cashregister
from .models import CashregisterProduct
from .models import Debt
from .models import DebtProduct


class TransactionProductInline(admin.StackedInline):
    model = TransactionProduct
    extra = 1


class TransactionAdmin(admin.ModelAdmin):
    inlines = [TransactionProductInline]
    list_display = ("id", "customer", "is_invoice", "total")


class CashregisterProductInline(admin.StackedInline):
    model = CashregisterProduct
    extra = 1


class CashregisterAdmin(admin.ModelAdmin):
    inlines = [CashregisterProductInline]


class DebtProductInline(admin.StackedInline):
    model = DebtProduct
    extra = 1


class DebtAdmin(admin.ModelAdmin):
    inlines = [DebtProductInline]


admin.site.register(Category)
admin.site.register(Suppler)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Cashregister, CashregisterAdmin)
admin.site.register(Debt, DebtAdmin)
