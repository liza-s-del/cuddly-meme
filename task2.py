# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator = ','):
    first_list = first.split(separator)
    second_list = second.split(separator)
    intersection = list(set(first_list).intersection(second_list))
    intersection.sort()
    return intersection

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_common = find_common_participants(participants_first_group, participants_second_group, '|')
print(participants_common)