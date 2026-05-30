def merge(arr1, arr2):
    '''
    Merge two sorted arrays into a single sorted array. Note: elements within and between the arrays may be duplicated.
    Time complexity: O(n + m) where n and m are the lengths of arr1 and arr2 respectively.
    Space complexity: O(n + m) for the merged array.
    '''
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            merged.append(arr2[j])
            j += 1
        else:
            merged.append(arr1[i])
            merged.append(arr2[j])
            i += 1
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged