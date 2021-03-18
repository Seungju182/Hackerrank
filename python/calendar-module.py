# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


def correct_day(m, d, y):
    print(calendar.day_name[calendar.weekday(y, m, d)].upper())


if __name__ == "__main__":
    m, d, y = map(int, input().split())
    correct_day(m, d, y)
