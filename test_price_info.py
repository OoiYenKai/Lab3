import price_info

def test_total_cost_of_shipping():
    test_result = price_info.total_cost_shopping()
    result = 46.75
    assert (result == test_result)

def test_cost_of_fruits():
    test_result = price_info.cost_of_fruits('apple', 10)
    result = 12.0
    assert (result == test_result)
