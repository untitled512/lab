print("Добро пожаловать в Калькулон, выберите операцию. ")
print("1. Сложение")
print("2. Умножение")
operation = input("Введите номер операции (1-2): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
if operation == '1':
 print(num1, "+", num2, "=", (num1 + num2))
elif operation == '2':
 print(num1, "*", num2, "=", (num1 * num2))
else:
 print("Некорректный ввод.")