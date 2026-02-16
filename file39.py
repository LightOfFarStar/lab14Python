import pickle
lists = input('Введите набор чисел: ')
list_form = []
list_form = list(map(int, lists.split()))
with open ("datafile", "wb") as file:
    pickle.dump(list_form, file)
with open ("datafile", "rb") as file:
    datafile = pickle.load(file)
def resulting(data):
    result = []
    for count in range(len(data)):
        if data[count] >= 5 and data[count] <= 10:
            result.append(data[count])
            result.append(data[count])
        else:
            result.append(data[count])
    return result
print(f"Удвоенные числа от 5 до 10: {' '.join(map(str, resulting(datafile)))}")

'''File39. Дан файл целых чисел. Продублировать в нем все числа, принадлежащие диапазону5–10.'''