from product import product_details

def test_product_details():
    expected_output = (
        "product Name: phone\n"
        "product ID: E201\n"
        "quantity: 1\n"
        "price: 55000"
    )

    assert product_details("phone", "E201", 1, 55000) == expected_output