import price_info



def test_total_cost():

    expected_total_cost=46.75

    result_total_cost = price_info.total_cost_shopping()

    assert (expected_total_cost == result_total_cost)



def test_cost_of_fruit():

    excepted_result = 1.20*5

    result_cost_of_fruits=price_info.cost_of_fruits('apple',5)

    assert(excepted_result == result_cost_of_fruits)