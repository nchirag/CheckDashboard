# checksite/urls.py
from django.contrib import admin
from django.urls import path
from app1 import views  # Import views from app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL for home view
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard view
    path('api/fake-order-data/', views.generate_fake_order_data, name='fake_order_data'),
    path('api/forecast-orders/', views.forecast_orders, name='forecast_orders'),
    path('parent_subcategory_data/', views.get_parent_subcategory_data, name='parent_subcategory_data'),
]
