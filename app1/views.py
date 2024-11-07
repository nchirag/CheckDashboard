from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Sum
from .models import Products, Orders, OrderDetails, Parent_Category, Sub_Category, Sub_Sub_Category
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import datetime
import random

def home(request):
    return HttpResponse("Hello, World!")

def dashboard_view(request):
    return render(request, 'app1/dashboard.html')

def generate_fake_order_data(start_date, num_records):
    """Generate fake order data."""
    dates = pd.date_range(start=start_date, periods=num_records, freq='D')
    order_totals = [random.randint(20, 100) for _ in range(num_records)]  # Random order totals
    return pd.DataFrame({'date': dates, 'total_orders': order_totals})

def train_time_series_model(order_data):
    """Train ARIMA model and forecast next 3 values."""
    order_data.set_index('date', inplace=True)
    model = ARIMA(order_data['total_orders'], order=(5, 1, 0))  # Adjust ARIMA parameters as needed
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=3)
    return forecast

def forecast_orders(request):
    print('forecast_orders called')
    
    # Generate fake order data for the last 30 days
    start_date = timezone.now() - pd.DateOffset(days=30)
    fake_data = generate_fake_order_data(start_date, 30)
    
    # Train the model on the fake data
    forecast = train_time_series_model(fake_data)

    # Prepare data for JSON response
    response_data = [
        {'date': (timezone.now() + timedelta(days=i)).strftime('%Y-%m-%d'), 'forecasted_orders': forecast[i]}
        for i in range(len(forecast))
    ]

    return JsonResponse(response_data, safe=False)

def fake_order_data(request):
    """View to generate fake order data."""
    start_date = timezone.now() - pd.DateOffset(days=30)  # Last 30 days
    fake_data = generate_fake_order_data(start_date, 30)
    
    # Prepare JSON response
    data = fake_data.to_dict(orient='records')
    return JsonResponse(data, safe=False)

def get_parent_subcategory_data(request):
    """Get the count of sub-categories for each parent category."""
    parent_data = (
        Parent_Category.objects
        .annotate(sub_category_count=Count('sub_category'))
        .values('parent_category_name', 'sub_category_count')
    )
    return JsonResponse(list(parent_data), safe=False)