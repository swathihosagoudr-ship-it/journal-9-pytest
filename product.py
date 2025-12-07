def product_details(name, product_id, quantity, price):
    result = (
        f"product Name: {name}\n"
        f"product ID: {product_id}\n"
        f"quantity: {quantity}\n"
        f"price: {price}"
    )
    return result
if __name__ == "__main__":
    name = "phone"
    product_id = "E201"
    quantity= 1
    price= 55000
    print(product_details(name, product_id, quantity, price))