def find_last_binary_digit(n):
    binary_string = bin(n)[2:]
    print(binary_string)
    return binary_string[-1]

print(find_last_binary_digit(104))