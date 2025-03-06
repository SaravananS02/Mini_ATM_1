def processed_list(numbers):
    processed_list = []
    zero_count = 0

    for num in numbers:
        if num == 0:
            zero_count += 1
        else:
            processed_list.append(num)
    processed_list.sort()
    processed_list.extend[0] * zero_count
    return processed_list

numbers = [9,1,0,7,5,8,0,2,4,0,6,0]
result = processed_list(numbers)
print(result)
