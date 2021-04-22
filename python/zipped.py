# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))

for score in zip(*scores):
    print(sum(score) / X)
