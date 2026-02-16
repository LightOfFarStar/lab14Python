import pickle
lists = input('Введите набор чисел: ')
list_form = []
list_form = list(map(float, lists.split()))
with open ("data", "wb") as file:
    pickle.dump(list_form, file)
with open ("data", "rb") as file:
    data = pickle.load(file)
summ = 0
for count in range(len(data)):
    if count % 2 == 1:
        summ += data[count]
print(f"Сумма четных чисел равна: {summ}")

'''File15. Дан файл вещественных чисел. Найти сумму его элементов с четными номерами.'''