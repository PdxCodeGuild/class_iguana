#lab_18_Peaks_and_Valleys
#ok how do i return/capture the indeces of the peaks and valleys. I am returning the elements right now.

def peaks(nums):
    peaks_index = []
    for i in range(1, len(nums)-1):
        if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
            peaks_index.append(i)
            # print(nums[i])
    return peaks_index

def valleys(nums):
    valleys_index = []
    for i in range(1, len(nums)-1):
        if nums[i - 1] > nums[i] and nums[i + 1] > nums[i]:
            valleys_index.append(i)

    return valleys_index


def peaks_and_valleys(nums):
    index = []
    peaks_and_valleys = peaks(nums) + valleys(nums)
    # print(peaks_and_valleys)
    # print(nums[peaks_and_valleys])
    for number in peaks_and_valleys:
        index.append(nums[number])    #
    return index



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# print(peaks(data))
# print(valleys(data))
print(peaks_and_valleys(data))

#.index(list)