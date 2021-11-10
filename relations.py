from math import pow


def tofixed(numobj, digits=2):  # Функция, возвращающая дробное число с двумя знаками после запятой(по умолчанию)
    return float(f"{numobj:.{digits}f}")


print("Программа расчитывает весовые коэффициенты")
# Ввод количества критериев
while True:  # Проверка ввода
    try:
        n = int(input("Введите количество критериев: "))
        if n <= 0:  # Проверка на положительность количества критериев
            print("Количество критериев должно быть положительным числом, не равным нулю")
        else:
            break
    except ValueError:
        print("Некорректный ввод!")
        pass

# Матрица взаимосвязей
RelationMatrix = [[0.0] * n for _ in range(n)]

# Ввод взаимосвязи критериев и заполнение матрицы взаимосвязей
for i in range(n):
    for j in range(i, n):
        if i == j:
            RelationMatrix[i][j] = 1.0
        else:
            while True:  # Проверка ввода
                try:
                    ijRelation = float(input(f"Введите отношение критерия {i+1} к критерию {j+1}: "))
                    if ijRelation <= 0:  # Проверка на положительность отношения критериев
                        print("Отношение критериев должно быть положительным числом, не равным нулю")
                    elif ijRelation >= 10:
                        print("Отношение критериев должно быть числом, меньшим 10")
                    else:
                        break
                except ValueError:
                    print("Некорректный ввод!")
                    pass
            RelationMatrix[i][j] = tofixed(ijRelation)

# Заполнение обратных взаимосвязей
for i in range(n):
    for j in range(i):
        RelationMatrix[i][j] = tofixed(pow(RelationMatrix[j][i], -1))

# Суммы матрицы
sums = []  # Суммы каждой строки матрицы
for i in range(n):
    sums.append(sum(RelationMatrix[i]))
# Сумма всех строк матрицы
sumRM = sum(sums)

# Массив весовых коэффициентов
Weight = [tofixed(sums[i]/sumRM) for i in range(n)]

# Поправка на погрешность
maxWeight = Weight[Weight.index(max(Weight))]
maxWeight = tofixed(maxWeight- (1-sum(Weight)))

print()
for i in range(n):
    print(f"Весовой коэффициент критерия {i+1} равен: {Weight[i]}")
