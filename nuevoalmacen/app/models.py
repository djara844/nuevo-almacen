from django.db import models


class Category(models.Model):
    name = models.CharField("Nombre", max_length=200)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Suppler(models.Model):

    TYPES_DOCUMENTS = (
        ("0", "Cédula de ciudadania"),
        ("1", "Cédula de extranjeria"),
        ("2", "NIT"),
        ("3", "Pasaporte"),
        ("4", "RUT"),
    )

    name = models.CharField("Nombre", max_length=200)
    phone = models.CharField("Teléfono", max_length=10)
    adress = models.CharField("Dirección", max_length=200)
    type_document = models.CharField(
        "Tipo de documento", max_length=1, choices=TYPES_DOCUMENTS
    )
    document = models.CharField("Número de documento", max_length=15)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "proveedores"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Nombre", max_length=200)
    price = models.FloatField("Precio")
    stock = models.IntegerField("Stock", default=1)
    code = models.CharField("Código", max_length=10)
    comments = models.CharField("Comentarios", max_length=260)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Suppler, on_delete=models.CASCADE, blank=True, default=""
    )
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


class Customer(models.Model):

    TYPES_DOCUMENTS = (
        ("0", "Cédula de ciudadania"),
        ("1", "Cédula de extranjeria"),
        ("2", "NIT"),
        ("3", "Pasaporte"),
        ("4", "RUT"),
    )

    name = models.CharField("Nombre", max_length=200)
    phone = models.CharField("Teléfono", max_length=10)
    address = models.CharField("Dirección", max_length=200)
    document_type = models.CharField(
        "Tipo de documento", max_length=1, choices=TYPES_DOCUMENTS
    )
    document = models.CharField("Número de documento", max_length=15)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class Transaction(models.Model):
    total = models.FloatField("Total")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, blank=True, default=""
    )
    is_invoice = models.BooleanField("¿Facturable?")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return str(self.id)


class TransactionProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("fecha de actualización", auto_now=True)

    class Meta:
        verbose_name = "Venta-Producto"
        verbose_name_plural = "Ventas-Prodcutos"

    def __str__(self):
        return str(self.id)
