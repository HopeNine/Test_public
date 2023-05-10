user_input = input('Введите последовательность чисел')
user_number = int(input('Введите число'))


def is_int(string):
    string = string.replace(' ', '')
    try:
        int(string)
        return True
    except ValueError:
        return False


if " " not in user_input:
    print("\nВО ВВОДЕ ОТСУТСТВУЮТ ПРОБЕЛЫ (введите числа, согласно условиям ввода.)")
    sequence_numbers = input('Введите целые числа через пробел: ')
if not is_int(user_input):
    print('\nВО ВВОДЕ СОДЕРЖАТСЯ НЕ ЦЕЛЫЕ ЧИСЛА (введите числа, согласно условиям ввода.)\n')
else:
    user_input = user_input.split()

numbers = [int(i) for i in user_input]


def sorting(array):
    if len(array) < 2:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def binary(array, number, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == number:
            return middle
        elif number < array[middle]:
            return binary(array, number, left, middle - 1)
        else:
            return binary(array, number, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


print(f'Упорядоченный по возрастанию список: {numbers}')

if not binary(numbers, user_number, 0, len(numbers)):
    element = min(numbers, key=lambda x: (abs(x - user_number), x))
    idx = numbers.index(element)
    max_idx = idx + 1
    min_idx = idx - 1
    if element < user_number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {element}, его индекс: {idx}
Ближайший больший элемент: {numbers[max_idx]} его индекс: {max_idx}''')
    elif min_idx < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {element}, его индекс: {numbers.index(element)}
В списке нет меньшего элемента''')
    elif element > user_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {element}, его индекс: {numbers.index(element)}
Ближайший меньший элемент: {numbers[min_idx]} его индекс: {min_idx}''')
    elif numbers.index(element) == 0:
        print(f'Индекс введенного элемента: {numbers.index(element)}')
else:
    print(
        f'Индекс введенного элемента: {binary(numbers, user_number, 0, len(numbers))}')
