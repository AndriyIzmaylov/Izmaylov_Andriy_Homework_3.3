# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.

# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.

# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.

# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.
# Було => стало
# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

def split_list(list_for_split):
    if not list_for_split:
        return [[], []]

    middle_index = (len(list_for_split) + 1) // 2
    splitted_list_part1 = list_for_split[:middle_index]
    splitted_list_part2 = list_for_split[middle_index:]

    return [splitted_list_part1, splitted_list_part2]


test_cases = [
    [],
    [1],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6]
]

for case in test_cases:
    print(f"Entry list: {case}")
    print(f"Result: {split_list(case)}")
    print("-" * 40)
