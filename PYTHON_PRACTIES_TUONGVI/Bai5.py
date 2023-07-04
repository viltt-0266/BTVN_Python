def count_occurrences(numbers):
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    sorted_dict = dict(sorted(count_dict.items(), key=lambda x: x[1]))
    
    return sorted_dict

def main():
    N = int(input("Nhập số lượng phần tử: "))
    numbers = [int(input("Nhập phần tử {}: ".format(i+1))) for i in range(N)]
    result_dict = count_occurrences(numbers)
    print(result_dict)

main()
