import random

filename_a = "SA.txt"
filename_b = "SB.txt"
filename_c = "SC.txt"
filename_d = "SD.txt"

number = 5

numbers_a = [random.randint(1, 100) for _ in range(number)]
numbers_b = [random.randint(1, 100) for _ in range(number)]
numbers_c = [random.randint(1, 100) for _ in range(number)]

with open(filename_a, 'w') as fa:
    fa.write(' '.join(map(str, numbers_a)))
with open(filename_b, 'w') as fb:
    fb.write(' '.join(map(str, numbers_b)))
with open(filename_c, 'w') as fc:
    fc.write(' '.join(map(str, numbers_c)))

print("Созданы исходные файлы:")
print(f"{filename_a}: {' '.join(map(str, numbers_a))}")
print(f"{filename_b}: {' '.join(map(str, numbers_b))}")
print(f"{filename_c}: {' '.join(map(str, numbers_c))}")

try:
    with open(filename_a, 'r') as fa, open(filename_b, 'r') as fb, open(filename_c, 'r') as fc:
        numbers_a = [int(x) for x in fa.read().split()]
        numbers_b = [int(x) for x in fb.read().split()]
        numbers_c = [int(x) for x in fc.read().split()]
    
    if len(numbers_a) != len(numbers_b) or len(numbers_a) != len(numbers_c):
        print("Предупреждение: файлы имеют разный размер!")
        min_length = min(len(numbers_a), len(numbers_b), len(numbers_c))
        print(f"Будет обработано только {min_length} элементов из каждого файла.")
        numbers_a = numbers_a[:min_length]
        numbers_b = numbers_b[:min_length]
        numbers_c = numbers_c[:min_length]
    
    result = []
    for a, b, c in zip(numbers_a, numbers_b, numbers_c):
        result.append(a)
        result.append(b)
        result.append(c)
    
    with open(filename_d, 'w') as fd:
        fd.write(' '.join(map(str, result)))
    
    print(f"Файл {filename_d} успешно создан!")
    print(f"Обработано {len(numbers_a)} элементов из каждого файла.")
    print(f"Всего записано {len(result)} чисел.")
    with open(filename_d, 'r') as fd:
        content = fd.read()
        print(f"Содержимое файла {filename_d}:")
        print(content)
except FileNotFoundError as e:
    print(f"Ошибка: не найден файл - {e.filename}")
except ValueError as e:
    print("Ошибка: в файлах содержатся не только целые числа")
    print("Убедитесь, что файлы содержат только целые числа, разделенные пробелами")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

'''File48. Даны три файла целых чисел одинакового размера с именами
SA, SB, SCистрокаSD.Создать новый файл с именем SD, в котором чередовались бы элементы
исходных файлов с одним и тем же номером:
A1, B1, C1, A2, B2, C2, … .'''