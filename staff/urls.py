from django.urls import path

from . import views

app_name = "staff"

urlpatterns = [
    path("orders/", views.orders, name="orders"),
    path("orders/<int:order_id>/", views.order_detail, name="order_detail"),
    path("menu/", views.menu, name="menu"),
]
