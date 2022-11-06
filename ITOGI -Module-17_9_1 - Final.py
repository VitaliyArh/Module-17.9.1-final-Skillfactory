num_input = int(input('Введите число - '))
string_num = input('Введите любые числа через пробел - ')

def binary_search(arr, element, left, right):
    if left > right:
        return False
    if len(arr) < 2:  # если кусок массива равен 2,
        return arr  # выходим из рекурсии
    middle = (right + left) // 2
    try:
        if arr[middle] < element <= arr[middle + 1]: # Проверка соответсвия условиям поиска элемента
            return middle
        elif element < arr[middle]:
            return binary_search(arr, element, left, middle - 1)
        else:
            return binary_search(arr, element, middle + 1, right)
    except IndexError:
        return False


list_string = string_num.split()      # Преобразование введённой последовательности в список


def sort(a):          # создаём функцию sort с аргументом а для Сортировки списка по возрастанию элементов в нем
    return sorted(a)


if len(list_string) <= 1:             # проверка на соответствие
    print('Ведена не корректная последовательность')
else:
    num_list = list(map(int, list_string)) #
    print(num_list)
    num_list = sort(num_list)  # присваиваем переменной результатов вызова функции
    print(binary_search(num_list, num_input, 0, len(num_list)))

