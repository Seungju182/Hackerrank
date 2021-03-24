# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":

    from collections import OrderedDict

    od = OrderedDict()
    N = int(input())
    for i in range(N):
        item, space, price = input().rpartition(' ')
        od[item] = od.get(item, 0) + int(price)

    for item in od:
        print(item, od[item])
