
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    no_intersection = {}

    for i in range (len(arrays) - 1):
        array = arrays[i]
        next_array = arrays[i + 1]

        for num in array:
            if num in next_array:
                result.append(num)
            else:
                no_intersection[num] = (array)
                break

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
