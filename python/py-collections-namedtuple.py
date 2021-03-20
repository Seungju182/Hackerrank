# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    Student = namedtuple('Student', input().split())
    student_list = [Student(*input().split()) for i in range(N)]
    average = sum([int(student.MARKS) for student in student_list]) / N
    print('{:0.2f}'.format(average))
