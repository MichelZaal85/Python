def sumit(numbers):
    c = []
    numbers.sort()
    for n in nums:
        if n > 0:
            c.append(n)
            if len(c) >= 2:
                return sum(c)


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2]) if numbers else None
