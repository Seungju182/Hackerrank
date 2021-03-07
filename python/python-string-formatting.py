def print_formatted(number):
    # your code goes here
    width = len(str(bin(number))[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i))[2:]
        hexadecimal = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]
        output_list = [decimal, octal, hexadecimal, binary]
        print(*(x.rjust(width) for x in output_list))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
