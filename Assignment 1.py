def primeproduct(m):
    if m <= 0:
        return False
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0 and is_prime(i) and is_prime(m // i):
            return True
    
    return False

print(primeproduct(6))

def delchar(s, c):
    if len(c) != 1:
        return s
    
    return s.replace(c, "")

print(delchar('banana','n'))

def shuffle(l1, l2):
    shuffled = []
    min_len = min(len(l1), len(l2))
    
    for i in range(min_len):
        shuffled.append(l1[i])
        shuffled.append(l2[i])
    
    if len(l1) > len(l2):
        shuffled.extend(l1[min_len:])
    elif len(l2) > len(l1):
        shuffled.extend(l2[min_len:])
    
    return shuffled

print(shuffle([0,2,4],[1,3]))
