from unicodedata import category
import uuid
from django.db import models
from .utils import product_directory_path

# Product, ProductCategory, ProductTag, ProductByTag, ProductImage

class ProductCategory(models.Model):
    name = models.CharField(max_length=255,verbose_name="Category Name")
    slug = models.SlugField(max_length=255,verbose_name="Slug", null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=255,verbose_name="Product Name")
    description = models.TextField(verbose_name="", null=True, blank=True)
    slug = models.SlugField(max_length=255,verbose_name="Slug", null=True, blank=True)
    category = models.ForeignKey('store.ProductCategory', on_delete=models.CASCADE, verbose_name="Category")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Price")
    stock = models.IntegerField(default=1, verbose_name="Stock")

    class Meta:
        ordering = ("-name", "id")
        verbose_name = "Product"
        verbose_name_plural = "Products"
        #db_table = "Patata"
    
    def __str__(self) -> str:
        return f"{self.name}, {self.price}, {self.stock}"

class ProductImage(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, verbose_name="Product")
    image = models.ImageField(upload_to=product_directory_path)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Products Images"
    
    def __str__(self) -> str:
        return f"{str(self.product)}, {self.image.name}"

class ProductTag(models.Model):
    name = models.CharField(max_length=255,verbose_name="Category Name")
    slug = models.SlugField(max_length=255,verbose_name="Slug", null=True, blank=True)

    class Meta:
        verbose_name = "Product Tag"
        verbose_name_plural = "Products Tags"

    def __str__(self) -> str:
        return f"{str(self.name)}"

class ProductByTag(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, verbose_name="Product")
    tag = models.ForeignKey('store.ProductTag', on_delete=models.CASCADE, verbose_name="Product")

