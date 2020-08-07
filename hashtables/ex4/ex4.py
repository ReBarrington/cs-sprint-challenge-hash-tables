
def has_negatives(a):

    neg = dict()
    result = []

    a.sort()
    
    for i in range(len(a)):
        if a[i] < 0:
            if a[i] not in neg:
            # number is negative but not yet recorded.
                # record in neg as 'positive: 1'
                a[i] *= -1
                neg[a[i]] = 1
        elif a[i] in neg:
            # if number has previously been stored as a negative, add 1
            neg[a[i]] += 1
    for tup in neg.items():
        if tup[1] > 1 and tup[0] not in result:
            result.append(tup[0])
        
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

