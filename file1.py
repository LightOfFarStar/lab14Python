try:
    name = input('Введите имя файла: ')
    with open (name, "wb") as file:
        None
    print("True")
except FileNotFoundError:
    print('False')

'''File1. Дана строка S. Если S является допустимым именем файла,
то создать пустойфайлсэтимименем и вывести True.
Если файл с именем S создать нельзя, то вывести False.'''