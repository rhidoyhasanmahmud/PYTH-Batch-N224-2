# Problem - 2 || Solution

def get_unique_list(original_list):
    unique_list = []

    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


original_list = [1, 2, 3, 4, 1, 2, 5]

unique_list = get_unique_list(original_list)

print(unique_list)

# Problem - 1 || Solution

def sum_all_value(values):
    total = 0

    for item in values:
        total += item

    return total


values = [10, 20, 30, 40, 50]
total_sum = sum_all_value(values)
print(total_sum)
