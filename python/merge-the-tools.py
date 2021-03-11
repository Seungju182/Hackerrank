def merge_the_tools(string, k):
    # your code goes here
    splitted_input = [string[i:i+k] for i in range(0, len(string), k)]
    print(*["".join(dict.fromkeys(item)) for item in splitted_input], sep='\n')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
