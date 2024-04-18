# Original binary string
binary_str = '1010'

# Initialize an empty list to collect toggled bits
toggled_bits = []

# Iterate over each bit in the binary string
for bit in binary_str:
    # Toggle the bit: if bit is '1', toggle to '0'; if bit is '0', toggle to '1'
    if bit == '1':
        toggled_bits.append('0')
    else:
        toggled_bits.append('1')

# Join the toggled bits list into a string
toggled_binary_str = ''.join(toggled_bits)

# Print original and toggled binary strings
print(f"Original binary string: {binary_str}")
print(f"Toggled binary string:   {toggled_binary_str}")


Original binary string: 1010
Toggled binary string:   0101


----------------------

def toggle_bits_and_convert(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    # Convert the positive integer to binary string (excluding '0b' prefix)
    binary_str = bin(n)[2:]

    # Calculate the length of the binary string
    num_bits = len(binary_str)

    # Toggle all bits in the binary string
    toggled_binary_str = ''.join('0' if bit == '1' else '1' for bit in binary_str)

    # Convert the toggled binary string back to integer
    toggled_value = int(toggled_binary_str, 2)

    return toggled_value

# Example usage with sample input and output
try:
    # Input a positive integer (e.g., 10)
    decimal_input = int(input("Enter a positive integer: "))
    
    # Call the function to toggle bits and convert
    result = toggle_bits_and_convert(decimal_input)

    # Print the result after toggling bits
    print(f"Original number: {decimal_input}")
    print(f"Binary representation: {bin(decimal_input)[2:]}")
    print(f"Toggled binary representation: {bin(result)[2:]}")
    print(f"Result after toggling bits: {result}")

except ValueError as ve:
    print(ve)
