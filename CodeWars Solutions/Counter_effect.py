def counter_effect(hit_count):
    print(hit_count)
    numbers = []
    for num in str(hit_count):
        numbers.append(list(range(int(num)+ 1)))
    return numbers

