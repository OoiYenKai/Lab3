import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_arr_more_than_10():
    input_arr = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111,222]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test_result = 1
    assert (test_result == result)

def test_bubble_sort_no_numbers():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test_result = 0
    assert (test_result == result)

def test_bubble_sort_no_integer():
    input_arr = ['hello']
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test_result = 2
    assert (test_result == result)
