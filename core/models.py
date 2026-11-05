"""Data models: Customer, Food_Item, Food_Order, Order_Item.

Owner: backend teammate. Keep the rules from Task 9:
- foreign keys use on_delete=models.PROTECT (ON DELETE RESTRICT)
- UNIQUE(order, food_item) on the order line
- order status: Placed / Preparing / Delivered / Cancelled
- db_table names match the Task 9 table plan
"""

from django.db import models  # noqa: F401
