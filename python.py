def dtb(number, base):
    binary_list = []
    while number >= base:
        temp = number % base
        binary_list.append((temp))
        number //= base
        
    if number != 0:
        binary_list.append(number)
    
    return binary_list[::-1]

def change_it(list, i):
    if list[i] == 0:
        list[i] = 1
    else:
        list[i] = 0
        
    return list
print(dtb(10, 2))
number = 10 & (1 << 1)
print(dtb(number, 2))
