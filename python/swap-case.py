def swap_case(s):
    swapped_sentence = ""
    for letter in s:
        if letter.isupper():
            swapped_sentence += letter.lower()
        elif letter.islower():
            swapped_sentence += letter.upper()
        else:
            swapped_sentence += letter
    return swapped_sentence


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
