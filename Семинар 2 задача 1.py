number = float(input('Введите число '))
a = 0
summ = 0
b = 0
number2 = round(number % 1, 6)
summ2 = 0
while number != 0:
    a = number % 10 // 1
    summ = summ + a
    number = number // 10

while number2 != 0:
    b = number2 // 0.1
    summ2 = summ2 + b
    number2 = number2 * 10
    number2 = round(number2 % 1, 6)
print("Сумма целой части")
print(summ)
print("Сумма дробной части")
print(summ2)
print("Сумма цифр числа")    
print(summ+summ2) 
