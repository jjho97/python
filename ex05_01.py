def mul(*values):
    total = 1
    for i in values:
        total = total * i
    return total
print(mul(5, 7, 9, 10))
