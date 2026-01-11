# 1.1. Функция сортировки массива целых чисел (сортировка пузырьком)
def sort_array(arr):
    # Реализуем сортировку пузырьком
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 1.2. Функция проверки на палиндром
def is_palindrome(s):
    
    s = s.lower().replace(" ", "")  # Приводим к нижнему регистру и удаляем пробелы
    return s == s[::-1]


# 1.3. Функция вычисления факториала
def factorial(n):
    if n < 0:
        raise Exception("")  # Факториал для отрицательных чисел не существует
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 1.4. Функция нахождения числа Фибоначчи на заданной позиции
def fibonacci(n):
    
        if n <= 0:
            raise Exception("плохо")
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    


# 1.5. Функция поиска подстроки в строке
def find_substring(s, substring):
    return s.find(substring)  # Вернет индекс первого вхождения, -1 если не найдено


# 1.6. Функция проверки на простое число
def is_prime(n):
    if n <= 1:
        raise Exception("плохо")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1.7. Функция инверсии цифр числа
def reverse_number(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    
    while x != 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    
    reversed_x *= sign
    
    # Проверяем, что число остается в пределах 32 бит
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        raise Exception("плохо")
    return reversed_x


# 1.8. Функция перевода числа в римскую систему счисления
def int_to_roman(num):
    if num <= 0 or num > 3999:
        raise Exception("плохо")
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
