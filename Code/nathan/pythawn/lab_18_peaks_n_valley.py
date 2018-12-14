def peaks_valleys(a):
    b = []
    for i in range(1, len(a)-1):
        if a[i-1] == a[i+1]:
            b.append(a[i])
    return b



data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3]
                    #^       ^                    ^               ^       ^
                    #p       v                    p               v       p
peaks = []
valleys = []
print(peak(data))
for i in range(1, len(data)-1):
    if data[i-1] < data[i] and data[i+1] < data[i]:
        peaks.append(data[i])
    if data[i-1] > data[i] and data[i+1] > data[i]:
        valleys.append(data[i])
print(valleys)
print(peaks)

