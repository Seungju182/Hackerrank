# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2, degrees


def get_theta(AB, BC):
    return int(round(degrees(atan2(AB, BC))))


if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    degree_sign = u"\N{DEGREE SIGN}"
    print(str(get_theta(AB, BC)), degree_sign, sep="")
