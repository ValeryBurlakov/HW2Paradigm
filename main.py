# императивная парадигма - функция описывает последовательность действий, выполняемых компьютером
# нам нужно последовательно выводить таблицу на экран, так как код простой, нам не нужно городить
# сложных структур данных и объектов, нет задачи создавать таблицы, нам достаточно сразу вывести результат

# Процедурный тип программирования - тут использован метод, который решает определенную задачу
# ведь нам нужно потом его вызвать для передачи данных в метод, для решения задачи
# программа организована вокруг вызова процедуры. Оборачивая скрипт в метод, это делает его
# более простым и понятным и мы сразу можем понять для чего он создан
def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, "*", j, "=", i*j)
        print()


n = int(input("Введите число n: "))
multiplication_table(n)