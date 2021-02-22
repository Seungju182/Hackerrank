if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    scores = sorted(list(set([score for name, score in students])))
    second_low = scores[1]
    for name, score in sorted(students):
        if score == second_low:
            print(name)
