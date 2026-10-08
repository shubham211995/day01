numbers = [2, 7, 11, 15]
target = 18


def two_sum(numbers, target):  
    output = {}
    for i, number in enumerate(numbers):
        rem = target - number
        if rem in output:
            return [output[rem], i]
        output[number] = i

print(two_sum(numbers, target))            