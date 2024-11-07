from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Parent_Category(models.Model):
    parent_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_category_name = models.CharField(max_length=100, unique=True)
    parent_category_description = models.TextField(blank=True)
    parent_category_active = models.BooleanField(default=True)
    parent_category_added_date = models.DateTimeField(auto_now_add=True)
    parent_category_modified_date = models.DateTimeField(auto_now=True)
    parent_category_removed_date = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.parent_category_name
    
    class Meta:
        verbose_name_plural = 'parent_categories'

class Sub_Category(models.Model):
    sub_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_category_name = models.CharField(max_length=100)
    sub_category_description = models.TextField(blank=True)
    sub_category_active = models.BooleanField(default=True)
    sub_category_added_date = models.DateTimeField(auto_now_add=True)
    sub_category_modified_date = models.DateTimeField(auto_now=True)
    sub_category_removed_date = models.DateTimeField(blank=True, null=True, editable=False)
    parent_category = models.ForeignKey(Parent_Category, on_delete=models.CASCADE)                    

    def __str__(self):
        return (self.sub_category_name+" Parent-"+self.parent_category.parent_category_name)
    
    class Meta:
        verbose_name_plural = 'sub_categories'

class Sub_Sub_Category(models.Model):
    sub_sub_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_sub_category_name = models.CharField(max_length=100, unique=True)
    sub_sub_category_description = models.TextField(blank=True)
    sub_sub_category_active = models.BooleanField(default=True)
    sub_sub_category_added_date = models.DateTimeField(auto_now_add=True)
    sub_sub_category_modified_date = models.DateTimeField(auto_now=True)
    sub_sub_category_removed_date = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.sub_sub_category_name
    
    class Meta:
        verbose_name_plural = 'sub_sub_categories'

class Sub_Sub_Category_Sub_Category_Connector(models.Model):
    sub_sub_category_sub_category_connector_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_sub_category_sub_category_connector_added_date = models.DateTimeField(auto_now_add=True)
    sub_sub_category_sub_category_connector_modified_date = models.DateTimeField(auto_now=True)
    sub_sub_category_sub_category_connector_removed_date = models.DateTimeField(blank=True, null=True)
    sub_sub_category_sub_category_connector_active = models.BooleanField(default=True)
    sub_sub_category = models.ForeignKey(Sub_Sub_Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True)

    def __uuid__(self):
        return self.sub_sub_category_sub_category_connector_id
    
    class Meta:
        verbose_name_plural = 'sub_sub_category_sub_category_connectors'



class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)  
    product_description = models.TextField(blank=True)
    product_active = models.BooleanField(default=True)
    product_added_date = models.DateTimeField(auto_now_add=True)
    product_modified_date = models.DateTimeField(auto_now=True)
    product_removed_date = models.DateTimeField(blank=True, null=True, editable=False)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = 'products'

class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_date = models.DateField()
    order_status = models.CharField(max_length=50)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    order_payment_id = models.CharField(max_length=100)
    order_invoice_id = models.CharField(max_length=100)
    order_total_quantity = models.IntegerField()
    order_shipped_address = models.CharField(max_length=500)
    order_shipped_city = models.CharField(max_length=100)
    order_shipped_state = models.CharField(max_length=300)
    order_shipped_zip = models.CharField(max_length=10)
    order_shipped_country = models.CharField(max_length=50)

    class Meta:
        db_table = 'orders'
        managed = False
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.order_id)


class OrderDetails(models.Model):
    order_detail_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    product_name = models.CharField(max_length=300)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    product_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_details'
        managed = False
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'

    def __str__(self):
        return str(self.order_detail_id)
