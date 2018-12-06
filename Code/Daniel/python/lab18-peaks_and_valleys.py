# Ignores first and last cases of data based on definitions of peaks and valleys.

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


# Checks if the current index value is higher than the previous and next values.
# Stores index if true and returns a list of the values.
def get_peaks(data):
    peaks = []
    for i, height in enumerate(data): 
        if i == 0 or i == len(data) - 1:
            pass
        else:
            if data[i-1] < height > data[i+1]:
                peaks.append(i)
    return peaks

# Checks if the current index value is lower than the previous and next values.
# Stores index if true and returns a list of the values.
def get_valleys(data):
    valleys = []
    for i, height in enumerate(data): 
        if i == 0 or i == len(data) - 1:
            pass
        else:
            if data[i-1] > height < data[i+1]:
                valleys.append(i)
    return valleys

# Calls get_peaks() and get_valleys() and joins them together.
# Sorts by order of appearance and returns set.
def get_peaks_and_valleys(data):
    peaks = get_peaks(data)
    valleys = get_valleys(data)
    peak_and_valley = sorted(set(peaks) | set(valleys))     # Conversion to sets due to limitation of join

    return peak_and_valley

 
# Loops to create stacks based on highest value
# Loops to print an 'X' if the data is less than or equal to the highest value for that stack
def get_visual(data):
    highest = max(data)

    for i in range(highest):
        for j in data:
                if j <= highest:
                    print(' ', end='  ') 
                else:
                    print('X', end='  ')
        print('\n') 
        highest -= 1
    




peaks = get_peaks(data)
valleys = get_valleys(data)
peaks_and_valleys = get_peaks_and_valleys(data)
get_visual(data)

# print(peaks)
# print(valleys)
# print(peaks_and_valleys)