m = int(input())
s1 = set(input().split())
n = int(input())
s2 = set(input().split())
result = []
result.extend(list(map(int, s1.difference(s2))))
result.extend(list(map(int, s2.difference(s1))))
result = sorted(result, reverse=True)
for i in result:
    print(i)
