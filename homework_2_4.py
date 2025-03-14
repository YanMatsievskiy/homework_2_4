'''Задача 4. Треугольный вопрос'''

a = int(input('Длина строны A: '))
b = int(input('Длина строны B: '))
c = int(input('Длина строны C: '))

if a == b == c:
  print('Равносторонний треугольник')
elif a + b < c or a + c < b or b + c < a:
  print('Ошибка')
elif a == b or a == c or b == c:
 print('Равнобедренный треугольник')
elif a + b > c and a + c > b and b + c > a:
  print('Обычный треугольник')
else:
  print('Ошибка')