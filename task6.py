#task6.py
def calculate_factorial(n):
    # Факториал 0 и 1 равен 1
    result = 1
    # Используем цикл для перемножения чисел от 1 до n
    for i in range(1, n + 1):
        result = result * i
    return result

# Основная часть программы
try:
    n = int(input("Введите натуральное число n: "))
    if n < 0:
        print("Ошибка: число должно быть положительным")
    else:
        print(f"Результат {n}! = {calculate_factorial(n)}")
except ValueError:
    print("Ошибка: введите целое число")