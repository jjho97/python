from functools import total_ordering


def totnum(start, end):
    total = 0
    for i in range(start, end+1):
        total = total + i
        #print(i,  " ", total)
    return total

start = int(input("첫번째 값을 넣으세요 >"))
end = int(input("마지막값을 넣으세요 >"))
print(totnum(start, end))