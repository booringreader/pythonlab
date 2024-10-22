
def int_to_binary(integer_part):
    return bin(integer_part)[2:]


def frac_to_binary(fractional_part, precision=10):
    binary_frac = ""
    while fractional_part > 0 and len(binary_frac) < precision:
        fractional_part *= 2
        bit = int(fractional_part)
        if bit == 1:
            fractional_part -= bit
            binary_frac += '1'
        else:
            binary_frac += '0'
    return binary_frac


def float_to_binary(num, precision=10):

    integer_part = int(num)
    fractional_part = num - integer_part


    binary_integer = int_to_binary(integer_part)
    binary_fraction = frac_to_binary(fractional_part, precision)


    return f"{binary_integer}.{binary_fraction}"


floating_point = float(input("Enter a floating-point number: "))


binary_representation = float_to_binary(floating_point)
print(f"Binary equivalent: {binary_representation}")
