from django.urls import path
from .views import ProductItemViews

urlpatterns = [
    path('product-items/', ProductItemViews.as_view()),
    path('product-items/<int:id>', ProductItemViews.as_view()),
]