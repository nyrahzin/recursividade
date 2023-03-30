def max(a):
    if len(a) == 1:
        return a[0]
    else:
        max_valor = max(a[1:])
        return a[0] if a[0] > max_valor else max_valor
    
def min(b):
    if len(b) == 1:
        return b[0]
    else:
        min_valor = min(b[1:])
        return b[0] if b[0] < min_valor else min_valor

def media(c):
    if len(c) == 1:
        return c[0]
    else:
        return (c[0] + media(c[1:])) / len(c)


lista = [5, 2, 8, 9, 98, 100, 546]
md = media(lista)
min_valor = min(lista)
max_valor = max(lista)
print(f'maior valor: {max_valor}')
print(f'media: {md}')
print(f'menor valor: {min_valor}')