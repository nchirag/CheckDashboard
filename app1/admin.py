from django.contrib import admin

# Register your models here.
from .models import Parent_Category, Sub_Category, Sub_Sub_Category, Sub_Sub_Category_Sub_Category_Connector
admin.site.register(Parent_Category)
admin.site.register(Sub_Category)
admin.site.register(Sub_Sub_Category)
admin.site.register(Sub_Sub_Category_Sub_Category_Connector)
