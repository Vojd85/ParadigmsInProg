def sort_list_imperative(numbers: list) -> list:
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def sort_list_declarative(numbers: list) -> list:
    return sorted(numbers)


if __name__ == "__main__":
    arr = [3, 6, 22, 23, 5, 67, 1, 3, 8, 23 , 4, 6]
    print(sort_list_imperative(arr))
    print(sort_list_declarative(arr))