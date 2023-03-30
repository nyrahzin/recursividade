def mdc(n1, n2):
    if n2 == 0:
        return n1
    else:
        return mdc(n2, n1 % n2)
def mmc(a, b):
    return (a * b) / mdc(a, b)

print(mdc(16,80))
print (mmc(4,6))