# объявили функцию для подсчета количества символов в тексте
def hello_world():
    print(" hello_world ")


hello_world()


def check_num(a, n):
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5

def reverse_stair(n):
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(5)