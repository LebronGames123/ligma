import employee_info


def test_get_employee_by_age_range():
    test_lower_limit = 20
    test_upper_limit = 30

    test_result = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result = employee_info.get_employees_by_age_range(test_lower_limit,test_upper_limit)

    assert (result == test_result )


def test_calculate_average_salary():

    expected_total_salary = (50000+60000+56000+70000+65000+60000)/6
    result = employee_info.calculate_average_salary()

    assert (expected_total_salary == result)

def test_get_employee_by_department():
    test_result=[{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    test_department = "Sales"
    result = employee_info.get_employees_by_dept(test_department)

    assert(test_result == result)