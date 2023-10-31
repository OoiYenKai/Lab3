import employee_info

def test_get_employees_by_age_range():
    age_lower_limit = 20
    age_upper_limit = 30
    result = employee_info.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    test_arr = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000},
                {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
    assert (test_arr == result)

def test_calculate_average_salary():
    test_result = 60166.67
    result = employee_info.calculate_average_salary()
    assert (result == test_result)

def test_get_employees_by_dept():
    department = "Sales"
    result = employee_info.get_employees_by_dept(department)
    test_arr = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000},
                {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    assert (result == test_arr)




