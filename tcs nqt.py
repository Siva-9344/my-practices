#1) toggled question

def toggle_bits(n):
    binary_rep = bin(n)[2:]
    toggled_binary = ""
    for bit in binary_rep:
        if bit == "1":
            toggled_binary += "0"

        else:
            toggled_binary += "1"

    result = int(toggled_binary,2)
    print(toggled_binary)
    print(binary_rep)

    return result



input_num  =int(input())
print("Input the Decimal number :",input_num)
toggled_value = toggle_bits(input_num)
print("After toggling bits :",toggled_value)

    
