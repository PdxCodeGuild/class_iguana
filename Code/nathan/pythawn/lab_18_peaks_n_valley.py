def peaks_valleys(a):
    b = []
    peaks = []
    valleys = []
    for i in range(1, len(a)-1):
        if a[i-1] == a[i+1]:
            b.append(a[i])
    for i in range(1, len(a) - 1):
        if a[i - 1] < a[i] and a[i + 1] < a[i]:
            peaks.append(a[i])
        if a[i - 1] > a[i] and a[i + 1] > a[i]:
            valleys.append(a[i])
    return b, peaks, valleys



data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3]
                    #^       ^                    ^               ^       ^
                    #p       v                    p               v       p
print(peaks_valleys(data))

