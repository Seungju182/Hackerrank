# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    _, stu_eng = int(input()), set(map(int, input().split()))
    _, stu_fre = int(input()), set(map(int, input().split()))
    print(len(stu_eng.intersection(stu_fre)))
