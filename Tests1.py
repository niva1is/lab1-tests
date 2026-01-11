import pytest
from Lab1 import sort_array, is_palindrome, factorial, fibonacci, find_substring, is_prime, reverse_number, int_to_roman

# 1. sort_array
def test_sort_array():
    assert sort_array([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    assert sort_array([1]) == [1]
    assert sort_array([5, 3, 2, 1, 4]) == [1, 2, 3, 4, 5]
    assert sort_array([]) == []

# 2. is_palindrome
def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("  ") == True

# 3. factorial
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    with pytest.raises(Exception):
        factorial(-1)

# 4. fibonacci
def test_fibonacci():
    with pytest.raises(Exception):
        fibonacci(-1)
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    # Добавляем 4-й тест
    assert fibonacci(2) == 1

# 5. find_substring
def test_find_substring():
    assert find_substring("Hello, world!", "world") == 7
    assert find_substring("Hello, world!", "Python") == -1
    assert find_substring("", "test") == -1
    assert find_substring("Hello", "") == 0

# 6. is_prime
def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(4) == False
    with pytest.raises(Exception):
        is_prime(-1)
    assert is_prime(13) == True

# 7. reverse_number
def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(-120) == -21
    assert reverse_number(0) == 0
    with pytest.raises(Exception):
        reverse_number(1534236469)
    # Добавляем 4-й тест
    assert reverse_number(100) == 1

# 8. int_to_roman
def test_int_to_roman():
    assert int_to_roman(1994) == "MCMXCIV"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(1) == "I"
    with pytest.raises(Exception):
        int_to_roman(-1)
    # Добавляем 4-й тест
    assert int_to_roman(1000) == "M"
