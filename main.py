from functools import total_ordering

from products import products

total_products = len(products)

total_products = len(products)

total_quantity = sum(product["quantity"] for product in products)

total_revenue = sum(product["price"] * product["quantity"] for product in products)

# Average price
average_price = sum(product["price"] for product in products) / total_products

# Most expensive product
max_product = max(products, key=lambda x: x["price"])

# Cheapest product
min_product = min(products, key=lambda x: x["price"])

# Results
print("----- Sales Data Report -----")
print("Total products:", total_products)
print("Total quantity sold:", total_quantity)
print("Total revenue:", total_revenue)
print("Average product price:", round(average_price, 2))
print("Most expensive product:", max_product["name"], f"({max_product['price']} SAR)")
print("Cheapest product:", min_product["name"], f"({min_product['price']} SAR)")

