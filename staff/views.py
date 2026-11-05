"""Restaurant staff pages. Owner: Dilnaz.

Until the models are ready, views pass test data to the templates.
"""

from django.shortcuts import render

# Temporary test data (replace with queries to core.models later)
TEST_ORDERS = [
    {"id": 101, "customer": "Aigerim", "total": 6800, "status": "Placed"},
    {"id": 102, "customer": "Aidos", "total": 1800, "status": "Preparing"},
]


def orders(request):
    return render(request, "staff/orders.html", {"orders": TEST_ORDERS})


def order_detail(request, order_id):
    return render(request, "staff/order_detail.html", {"order_id": order_id})


def menu(request):
    return render(request, "staff/menu.html")
