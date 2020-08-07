
def intersection(arrays):
    frequency_dict = dict()
    result = []

    for i in range(len(arrays)):
        for num in arrays[i]:
            if num not in frequency_dict:
                # if not there, put it there as 1 time
                frequency_dict[num] = 1
            else:
                # if already there, add 1 time
                frequency_dict[num] += 1

        # if num in every list of arrays:
        if num in frequency_dict.items() == len(arrays):
            result.append(num)
        
        return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
