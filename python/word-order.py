# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


def print_num_distinct_words(word_list):
    print(len(set(word_list)))


def print_occurrences(words):
    z = Counter(words)
    print(" ".join([str(value) for value in z.values()]))


if __name__ == "__main__":
    N = int(input())
    words = [input() for i in range(N)]
    print_num_distinct_words(words)
    print_occurrences(words)
