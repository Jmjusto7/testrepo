def stones(n, a, b):
    minn = min(a,b)
    maxx = max(a,b)
    res = [[minn for x in range(n)] for x in range(1 << n)]
    
    half = (2**n) // 2
    
    for i in range(n):
        item = minn
        count = 0
        for j in range(1 << n):
            if count == half:
                item = maxx if item == minn else minn
                count = 0
            res[j][i] = item
            if i > 1:
                res[j][i] += res[j][i-1]
            count += 1
        half //= 2

    return sorted(set([x[n-1] for x in res]))