def analyze_numbers(numbers):
    plus_count = 0
    minus_sum = 0
    
    for num in numbers:
        if num > 0:
            plus_count += 1
        elif num < 0:
            minus_sum += num
            
    return (plus_count, minus_sum)





def get_even(numbers):
    even_numbers = []
    for x in numbers:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers



def swap_min_max(numbers):
    if len(numbers) == 0:
        return numbers
    
    numbers = numbers.copy()

    num_min = 0
    num_max = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[num_min]:
            num_min = i
        if numbers[i] > numbers[num_max]:
            num_max = i

    numbers[num_min], numbers[num_max] = numbers[num_max], numbers[num_min]
    return numbers



result = analyze_numbers([4, -2, 0, 7, -5, 4])
print("задание первое: ", result) # 1



numbers2 = [5, 2, 9, 1, 11]
result2 = get_even(numbers2)
print("Задание второе: ", result2) # 2

numbers3 = [5, 1, 8, 6]
result3 = swap_min_max(numbers3)
print("Задание третье:", result3) # 3