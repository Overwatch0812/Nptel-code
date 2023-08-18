def expanding(l):
    if len(l) < 2:
        return False

    prev_diff = abs(l[1] - l[0])

    for i in range(1, len(l) - 1):
        diff = abs(l[i + 1] - l[i])
        if diff <= prev_diff:
            return False
        prev_diff = diff

    return True

def sumsquare(l):
    odd=[]
    even=[]
    odd_final=0
    even_final=0
    final=[]
    for i in range(0,len(l)):
        if l[i]%2==0:
            even.append(l[i]**2)
        else:
            odd.append(l[i]**2)
    for i in range(0,len(odd)):
        odd_final=odd_final+odd[i]
    for i in range(0,len(even)):
        even_final=even_final+even[i]
    final.append(odd_final)
    final.append(even_final)
    return final

def transpose(m):
    transposed = []
    for i in range(len(m[0])):
        transposed_row = []
        for row in m:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed




