def s_m(n):
    if n < 10:
        return n
    else:
        return (n % 10) + s_m(n // 10)

print(s_m(145))
