def count_vowels(text):
    vowles = "аеёиоуыэюя"
    count = 0
    for word in text.lower():
        if word in vowles:
            count += 1
    return count

print(count_vowels('Программирование'))


def positives(values):
    result = []
    for num in values:
        if num > 0:
            result.append(num)
    return result

print(positives([-2, 5, 0, 7, -1]))