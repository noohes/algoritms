n = int(input())
a = set(input().split())
m = int(input())
b = set(input().split())
print(len(a.symmetric_difference(b)))