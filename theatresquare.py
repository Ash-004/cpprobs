n, m, a = map(int, input().split())

r = n // a
if n % a != 0:
    r += 1

c = m // a
if m % a != 0:
    c += 1

f = r * c
print(f)
